#!/usr/bin/env python3
"""Validate the skills in skills/.

Checks, per skill folder:
  - SKILL.md exists and starts with YAML frontmatter holding exactly `name` and `description`
  - `name` is lowercase-hyphen and equals the folder name
  - `description` is a non-empty string of at most 1024 characters
  - relative paths such as `references/x.md`, `templates/x.md`, `scripts/x.py` and
    `<other-skill>/references/x.md` mentioned in any .md file of the skill exist
  - no absolute local home-directory paths in any text file
Repo-wide:
  - relative Markdown links in README.md and docs/*.md resolve
  - scripts/fin.py gives the expected NPV, ROI, IRR and payback on a fixed input

A reference to another skill (`requirements-review/references/iso29148.md`) is a
warning, because it only works when the whole set is installed. With --standalone
it is an error, to check that each skill works when installed alone.

Usage: python3 scripts/validate.py [--standalone]
Needs PyYAML (pip install pyyaml). Exit code 1 when any error is found.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MAX_DESCRIPTION = 1024
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
SUBDIRS = "references|templates|scripts"
# `references/x.md` or `other-skill/references/x.md`, inside backticks
PATH_RE = re.compile(r"`(?:([a-z0-9-]+)/)?((?:%s)/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+)`" % SUBDIRS)
LOCAL_PATH_RE = re.compile(r"(?<![\w.-])(/Users/|/home/)[A-Za-z0-9_.-]+")
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
TEXT_SUFFIXES = {".md", ".py", ".json", ".txt", ".yml", ".yaml"}

FIN_INPUT = {
    "discount_rate": 0.1,
    "years": [
        {"year": 0, "benefits": 0, "costs": 100},
        {"year": 1, "benefits": 40, "costs": 10},
        {"year": 2, "benefits": 60, "costs": 10},
        {"year": 3, "benefits": 80, "costs": 10},
    ],
}
FIN_EXPECTED = {"npv": 21.187, "roi": 0.3846, "irr": 0.2013, "payback_year": 2.2857}

errors, warnings = [], []


def rel(p):
    return p.relative_to(ROOT).as_posix()


def check_frontmatter(skill_dir):
    path = skill_dir / "SKILL.md"
    if not path.is_file():
        errors.append(f"{rel(skill_dir)}: SKILL.md is missing")
        return
    m = FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
    if not m:
        errors.append(f"{rel(path)}: no YAML frontmatter at the top of the file")
        return
    try:
        meta = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        errors.append(f"{rel(path)}: frontmatter is not valid YAML ({str(e).splitlines()[0]})")
        return
    if not isinstance(meta, dict):
        errors.append(f"{rel(path)}: frontmatter is not a mapping")
        return
    if set(meta) != {"name", "description"}:
        errors.append(f"{rel(path)}: frontmatter keys are {sorted(meta)}, expected ['description', 'name']")
    name, desc = meta.get("name"), meta.get("description")
    if not isinstance(name, str) or not NAME_RE.match(name):
        errors.append(f"{rel(path)}: name {name!r} is not lowercase-hyphen text")
    elif name != skill_dir.name:
        errors.append(f"{rel(path)}: name {name!r} differs from folder {skill_dir.name!r}")
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{rel(path)}: description is missing or not text")
    elif len(desc) > MAX_DESCRIPTION:
        errors.append(f"{rel(path)}: description is {len(desc)} characters, limit {MAX_DESCRIPTION}")


def check_references(skill_dir, standalone):
    for md in sorted(skill_dir.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for m in PATH_RE.finditer(text):
            other, sub = m.group(1), m.group(2)
            if other is None:
                target = skill_dir / sub
            elif other == skill_dir.name:
                target = skill_dir / sub
            else:
                target = SKILLS / other / sub
                msg = f"{rel(md)}: reference to another skill `{other}/{sub}`"
                if not target.exists():
                    errors.append(f"{msg} does not exist")
                    continue
                (errors if standalone else warnings).append(
                    msg + " (works only when the whole set is installed)")
                continue
            if not target.exists():
                errors.append(f"{rel(md)}: broken reference `{m.group(0).strip('`')}`")


def check_local_paths():
    files = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix in TEXT_SUFFIXES
             and ".git" not in p.relative_to(ROOT).parts]
    for p in files:
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if LOCAL_PATH_RE.search(line):
                errors.append(f"{rel(p)}:{n}: absolute local path")


def check_doc_links():
    docs = [ROOT / "README.md"] + sorted((ROOT / "docs").glob("*.md"))
    for doc in docs:
        if not doc.is_file():
            continue
        for m in LINK_RE.finditer(doc.read_text(encoding="utf-8")):
            href = m.group(1)
            if re.match(r"[a-z][a-z0-9+.-]*:", href):
                continue
            if not (doc.parent / href).exists():
                errors.append(f"{rel(doc)}: broken link ({href})")


def check_fin():
    script = SKILLS / "business-case-strategy" / "scripts" / "fin.py"
    if not script.is_file():
        errors.append(f"{rel(script)}: missing, cannot run the smoke test")
        return
    with tempfile.TemporaryDirectory() as tmp:
        inp = Path(tmp) / "input.json"
        inp.write_text(json.dumps(FIN_INPUT), encoding="utf-8")
        run = subprocess.run([sys.executable, "-I", str(script), str(inp)],
                             capture_output=True, text=True)
    if run.returncode != 0:
        errors.append(f"fin.py exited with {run.returncode}: {run.stderr.strip()[:200]}")
        return
    try:
        got = json.loads(run.stdout)
    except json.JSONDecodeError:
        errors.append("fin.py output is not JSON")
        return
    for key, want in FIN_EXPECTED.items():
        val = got.get(key)
        if not isinstance(val, (int, float)) or abs(val - want) > 5e-4:
            errors.append(f"fin.py {key} = {val}, expected about {want}")


def main():
    standalone = "--standalone" in sys.argv[1:]
    if not SKILLS.is_dir():
        sys.exit("skills/ not found")
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for d in skill_dirs:
        check_frontmatter(d)
        check_references(d, standalone)
    check_local_paths()
    check_doc_links()
    check_fin()
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"{len(skill_dirs)} skills checked, {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
