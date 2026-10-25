"""Tests for scripts/validate.py. Run: python3 -m unittest discover tests

Every test works on a temporary copy of the repo, never on the real files.
"""
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())


def make_repo(tmp, skills=None):
    repo = Path(tmp) / "repo"
    repo.mkdir()
    for name in ("scripts", "docs"):
        shutil.copytree(ROOT / name, repo / name)
    for name in ("README.md", "LICENSE"):
        shutil.copy(ROOT / name, repo / name)
    (repo / "skills").mkdir()
    for s in skills or SKILLS:
        shutil.copytree(ROOT / "skills" / s, repo / "skills" / s)
    return repo


def validate(repo, *args):
    run = subprocess.run([sys.executable, str(repo / "scripts" / "validate.py"), *args],
                         capture_output=True, text=True)
    return run.returncode, run.stdout


def edit(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{old!r} not in {path}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


class RealRepo(unittest.TestCase):
    def test_default_and_standalone_pass(self):
        for args in ((), ("--standalone",)):
            with self.subTest(args=args), tempfile.TemporaryDirectory() as tmp:
                code, out = validate(make_repo(tmp), *args)
                self.assertEqual(code, 0, out)

    def test_each_skill_installed_alone_has_no_broken_references(self):
        for skill in SKILLS:
            with self.subTest(skill=skill), tempfile.TemporaryDirectory() as tmp:
                _, out = validate(make_repo(tmp, [skill]), "--standalone")
                own = [l for l in out.splitlines()
                       if l.startswith(f"ERROR skills/{skill}")]
                self.assertEqual(own, [], out)


class Mutations(unittest.TestCase):
    def check(self, mutate, expect, args=(), code=1):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp)
            mutate(repo / "skills")
            got, out = validate(repo, *args)
            self.assertEqual(got, code, out)
            if expect:
                self.assertRegex(out, expect)

    def test_cross_skill_path_warns_by_default_and_fails_standalone(self):
        def add(s):
            with open(s / "story-writer" / "SKILL.md", "a", encoding="utf-8") as f:
                f.write("\nSee `requirements-review/references/checklists.md`.\n")
        self.check(add, r"WARN .*another skill", code=0)
        self.check(add, r"ERROR .*another skill", args=("--standalone",))

    def test_link_leaving_skill_folder(self):
        def add(s):
            with open(s / "story-writer" / "SKILL.md", "a", encoding="utf-8") as f:
                f.write("\n[x](../nfr-writer/SKILL.md)\n")
        self.check(add, r"WARN .*leaves the skill folder", code=0)
        self.check(add, r"ERROR .*leaves the skill folder", args=("--standalone",))

    def test_cross_skill_path_to_missing_file_fails_by_default(self):
        def add(s):
            with open(s / "story-writer" / "SKILL.md", "a", encoding="utf-8") as f:
                f.write("\nSee `nfr-writer/references/nope.md`.\n")
        self.check(add, r"ERROR .*does not exist")

    def test_name_differs_from_folder(self):
        self.check(lambda s: edit(s / "story-writer" / "SKILL.md", "name: story-writer", "name: story-writr"),
                   r"differs from folder")

    def test_extra_frontmatter_key(self):
        self.check(lambda s: edit(s / "nfr-writer" / "SKILL.md", "\ndescription:", "\nversion: 1\ndescription:"),
                   r"frontmatter keys")

    def test_description_too_long(self):
        self.check(lambda s: edit(s / "nfr-writer" / "SKILL.md", 'description: "', 'description: "' + "x" * 1100),
                   r"limit 1024")

    def test_missing_frontmatter(self):
        def cut(s):
            p = s / "story-writer" / "SKILL.md"
            p.write_text(p.read_text(encoding="utf-8").split("\n", 1)[1], encoding="utf-8")
        self.check(cut, r"no YAML frontmatter")

    def test_broken_reference(self):
        self.check(lambda s: (s / "nfr-writer" / "references" / "thresholds.md").unlink(),
                   r"broken reference")

    def test_absolute_local_path(self):
        def add(s):
            with open(s / "story-writer" / "references" / "ac-patterns.md", "a", encoding="utf-8") as f:
                f.write("\n/Users/someone/notes\n")
        self.check(add, r"absolute local path")

    def test_fin_gives_wrong_result(self):
        self.check(lambda s: edit(s / "business-case-strategy" / "scripts" / "fin.py",
                                  "n / (1 + rate) ** t", "n / (1 + rate) ** (t + 1)"),
                   r"fin\.py npv")

    def test_invalid_yaml(self):
        self.check(lambda s: edit(s / "story-writer" / "SKILL.md", 'description: "Write', 'description: Write: x "Write'),
                   r"not valid YAML")

    def test_missing_skill_md(self):
        self.check(lambda s: (s / "story-writer" / "SKILL.md").unlink(), r"SKILL\.md is missing")

    def test_name_not_lowercase_hyphen(self):
        self.check(lambda s: edit(s / "story-writer" / "SKILL.md", "name: story-writer", "name: Story_Writer"),
                   r"not lowercase-hyphen")

    def test_broken_readme_link(self):
        def add(s):
            with open(s.parent / "README.md", "a", encoding="utf-8") as f:
                f.write("\n[x](docs/does-not-exist.md)\n")
        self.check(add, r"broken link")

    def test_fin_missing(self):
        self.check(lambda s: (s / "business-case-strategy" / "scripts" / "fin.py").unlink(), r"fin\.py")

    def test_path_prefixed_with_own_skill_name_is_not_a_cross_reference(self):
        def add(s):
            with open(s / "story-writer" / "SKILL.md", "a", encoding="utf-8") as f:
                f.write("\nSee `story-writer/references/quality-checks.md`.\n")
        self.check(add, None, args=("--standalone",), code=0)

    def test_skill_name_without_path_is_not_a_reference(self):
        def add(s):
            with open(s / "story-writer" / "SKILL.md", "a", encoding="utf-8") as f:
                f.write("\nSee the `requirements-review` skill, if installed.\n")
        self.check(add, None, args=("--standalone",), code=0)


if __name__ == "__main__":
    unittest.main()
