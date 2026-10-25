"""Offline tests for evals/grade.py, the case files and the golden answers.

Run: python3 -m unittest discover evals/tests
No LLM, no network. Three layers:
  - the case files and goldens are consistent (CaseFiles, Goldens)
  - each check type is exercised on small inputs, valid and invalid (CheckTypes)
  - mutations of a good golden fail only the check that should catch them (Mutations)
"""
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import grade  # noqa: E402

EVALS = Path(__file__).resolve().parents[1]
GOLDEN = EVALS / "golden"
CASES = grade.load_cases()
SKILLS_UNDER_TEST = {"story-writer", "requirements-review", "requirements-trace", "requirements-document"}
STANDALONE_IDS = {"sw-standalone", "rr-standalone-tracking", "rr-standalone-iso", "rt-standalone", "rd-standalone"}


def golden(case_id, which):
    return (GOLDEN / f"{case_id}.{which}.md").read_text(encoding="utf-8")


def meta_for(case):
    return {"loaded_skills": case["install"]} if case["kind"] == "standalone" else None


def make_case(checks, prompt="", kind="main", install=None, fixtures=None, skill="story-writer"):
    case = {"id": "x", "skill": skill, "kind": kind, "prompt": prompt, "fixtures": fixtures or [],
            "checks": checks, "rubric": [], "bad_expected_failures": []}
    if install:
        case["install"] = install
    return case


def run(check, text, **kw):
    check = dict(check, id="c")
    case = make_case([check], **kw)
    return grade.run_check(grade.Ctx(case, text), check)[0]


def failed_ids(case_id, text):
    case = CASES[case_id]
    return set(grade.grade_case(case, text, meta_for(case))["failed"])


class CaseFiles(unittest.TestCase):
    def test_exactly_the_planned_cases_exist(self):
        by_skill = {}
        for c in CASES.values():
            by_skill.setdefault(c["skill"], []).append(c["kind"])
        self.assertEqual(set(by_skill), SKILLS_UNDER_TEST)
        for skill, kinds in by_skill.items():
            for kind in ("main", "vague", "trap"):
                self.assertEqual(kinds.count(kind), 1, f"{skill} needs one {kind} case")
        self.assertEqual({i for i, c in CASES.items() if c["kind"] == "standalone"}, STANDALONE_IDS)
        self.assertEqual(len(CASES), 17)

    def test_every_case_is_valid(self):
        for cid, case in CASES.items():
            with self.subTest(cid):
                self.assertEqual(grade.validate_case(case), [])

    def test_every_case_has_both_goldens(self):
        for cid in CASES:
            for which in ("good", "bad"):
                self.assertTrue((GOLDEN / f"{cid}.{which}.md").is_file(), f"{cid}.{which}.md missing")

    def test_no_orphan_goldens_or_fixtures(self):
        names = {p.name for p in GOLDEN.glob("*.md")}
        expected = {f"{c}.{w}.md" for c in CASES for w in ("good", "bad")}
        self.assertEqual(names, expected)
        used = {f for c in CASES.values() for f in c.get("fixtures", [])}
        self.assertEqual({p.name for p in (EVALS / "fixtures").glob("*")}, used)

    def test_rubric_ids_match_rubric_file(self):
        defined = set(re.findall(r"^\|\s*([A-Z]{2}-\d+)\s*\|", (EVALS / "RUBRIC.md").read_text(), re.M))
        used = {r for c in CASES.values() for r in c["rubric"]}
        self.assertEqual(used, defined)

    def test_standalone_cases_install_only_what_they_name(self):
        for cid in STANDALONE_IDS:
            self.assertEqual(CASES[cid]["install"], [CASES[cid]["skill"]])
            self.assertTrue(any(c["type"] == "no_missing_resource" for c in CASES[cid]["checks"]), cid)

    def test_prompt_contains_fixture_text(self):
        prompt = grade.build_prompt(CASES["rr-main"])
        self.assertIn("US-05", prompt)
        self.assertIn("--- clinic-stories-to-review.md ---", prompt)

    def test_a_broken_case_is_reported(self):
        bad = dict(CASES["sw-main"], checks=[{"id": "a", "type": "nope"}], bad_expected_failures=["zzz"])
        errs = grade.validate_case(bad)
        self.assertTrue(any("unknown check type" in e for e in errs))
        self.assertTrue(any("unknown checks" in e for e in errs))
        bad = dict(CASES["sw-main"], checks=[{"id": "a", "type": "match", "pattern": "("}],
                   bad_expected_failures=["a"])
        self.assertTrue(any("bad regex" in e for e in grade.validate_case(bad)))
        bad = dict(CASES["rd-main"], checks=[{"id": "a", "type": "verbatim", "phrases": ["not in the input"]}],
                   bad_expected_failures=["a"])
        self.assertTrue(any("not in the input" in e for e in grade.validate_case(bad)))


class Goldens(unittest.TestCase):
    def test_good_golden_passes_every_check(self):
        for cid, case in CASES.items():
            with self.subTest(cid):
                r = grade.grade_case(case, golden(cid, "good"), meta_for(case))
                self.assertEqual(r["failed"], [], [c for c in r["checks"] if not c["ok"]])
                self.assertEqual(r["status"], "pass")

    def test_bad_golden_fails_exactly_the_listed_checks(self):
        for cid, case in CASES.items():
            with self.subTest(cid):
                r = grade.grade_case(case, golden(cid, "bad"), meta_for(case))
                self.assertEqual(set(r["failed"]), set(case["bad_expected_failures"]))
                self.assertEqual(r["status"], "fail")

    def test_bad_golden_still_looks_like_an_answer(self):
        # a bad golden that fails because it is empty would prove nothing
        for cid in CASES:
            self.assertGreater(len(golden(cid, "bad").split()), 25, cid)

    def test_standalone_isolation_states(self):
        for cid in STANDALONE_IDS:
            case, text = CASES[cid], golden(cid, "good")
            with self.subTest(cid):
                self.assertEqual(grade.grade_case(case, text, None)["status"], "unverified")
                self.assertEqual(grade.grade_case(case, text, {})["status"], "unverified")
                self.assertEqual(grade.grade_case(case, text, {"loaded_skills": case["install"]})["status"], "pass")
                other = "nfr-writer" if cid != "rt-standalone" else "story-writer"
                r = grade.grade_case(case, text, {"loaded_skills": case["install"] + [other]})
                self.assertEqual(r["status"], "fail")
                self.assertEqual(r["isolation"], "violated")
                # a skill from outside the suite does not matter for these cross-references
                r = grade.grade_case(case, text, {"loaded_skills": case["install"] + ["commit"]})
                self.assertEqual(r["status"], "pass")

    def test_non_standalone_cases_ignore_isolation(self):
        case = CASES["sw-main"]
        r = grade.grade_case(case, golden("sw-main", "good"), None)
        self.assertEqual((r["status"], r["isolation"]), ("pass", None))

    def test_failure_beats_unverified(self):
        case = CASES["rr-standalone-tracking"]
        self.assertEqual(grade.grade_case(case, golden("rr-standalone-tracking", "bad"), None)["status"], "fail")


class Parsing(unittest.TestCase):
    def test_headings_bold_labels_and_numbering(self):
        text = "## 3. Findings\nrow\n**Assumptions**: a\n**To clarify**\nq\n# Title\nx"
        self.assertEqual([k for k, _ in grade.split_sections(text)], ["findings", "assumptions", "to clarify", "title"])
        self.assertEqual(grade.get_section(text, "Assumptions").strip(), "a")
        self.assertEqual(grade.get_section(text, ["Nope", "to clarify"]).strip(), "q")
        self.assertIsNone(grade.get_section(text, "Nope"))

    def test_verdict_in_bold_does_not_split_the_section(self):
        text = "## 2. Verdict\n**Not ready** for approval.\n**Conditional**: more text\n## 3. Findings\nx"
        body = grade.get_section(text, "Verdict")
        self.assertIn("Not ready", body)
        self.assertIn("more text", body)
        self.assertEqual(grade.verdict_of(body), "Not ready")

    def test_verdict_word_order(self):
        self.assertEqual(grade.verdict_of("Conditional on a fix; then ready."), "Conditional")
        self.assertEqual(grade.verdict_of("Ready."), "Ready")
        self.assertEqual(grade.verdict_of("Not ready, but nearly ready."), "Not ready")
        self.assertIsNone(grade.verdict_of("No opinion."))

    def test_blocks_join_indented_continuations(self):
        text = "- first item\n  continues here\n- second\n| a | b |\nplain line"
        self.assertEqual(grade.blocks(text), ["- first item continues here", "- second", "| a | b |", "plain line"])

    def test_tables_with_and_without_outer_pipes(self):
        text = "| A | B |\n|---|---|\n| 1 | **x** |\n\nCode | Type\n--- | ---\nq | r"
        tables = grade.parse_tables(text)
        self.assertEqual(tables[0], (["A", "B"], [["1", "x"]]))
        self.assertEqual(tables[1], (["Code", "Type"], [["q", "r"]]))
        self.assertEqual(grade.column_cells(text, "^b"), ["x"])

    def test_numbers_ignore_ids_dates_and_list_markers(self):
        keys = grade.number_keys("1. See AC-01.2 and NFR-SEC-01 on 2026-11-02, 24 hours, 0,5 and 3.0")
        self.assertEqual(keys, {"24.0", "0.5", "3.0"})

    def test_id_pattern(self):
        self.assertEqual(grade.ID_RE.findall("NFR-SEC-01, AC-01.2. BR-09, UTF-8 and US-02/BR-02"),
                         ["NFR-SEC-01", "AC-01.2", "BR-09", "UTF-8", "US-02", "BR-02"])
        self.assertEqual(grade.ID_RE.findall("TC-xx and TC-1"), ["TC-1"])


class CheckTypes(unittest.TestCase):
    def test_sections(self):
        c = {"type": "sections", "names": [["Gaps", "Gap report"], "To confirm"], "ordered": True}
        self.assertTrue(run(c, "## Gap report\nx\n## To confirm\ny"))
        self.assertFalse(run(c, "## Gaps\nx"))
        self.assertFalse(run(c, "## To confirm\ny\n## Gaps\nx"))  # out of order
        self.assertTrue(run(dict(c, ordered=False), "## To confirm\ny\n## Gaps\nx"))
        c = {"type": "sections", "names": ["Assumptions"], "non_empty": True}
        self.assertTrue(run(c, "**Assumptions**: the old slot is kept"))
        self.assertFalse(run(c, "**Assumptions**:\n\n**To clarify**: x"))

    def test_match_and_not_match(self):
        c = {"type": "match", "pattern": r"\?", "min": 0, "max": 2}
        self.assertTrue(run(c, "one? two?"))
        self.assertFalse(run(c, "a? b? c?"))
        self.assertFalse(run({"type": "match", "pattern": "x", "min": 2}, "x"))
        self.assertTrue(run({"type": "match", "pattern": "x", "section": "S"}, "## S\nx"))
        self.assertFalse(run({"type": "match", "pattern": "x", "section": "S"}, "x\n## T\ny"))
        self.assertTrue(run({"type": "match", "pattern": "x", "section": "S", "section_optional": True, "min": 0}, "y"))
        self.assertFalse(run({"type": "not_match", "pattern": "passes"}, "It passes."))
        self.assertTrue(run({"type": "not_match", "pattern": "passes"}, "It is not ready."))

    def test_ids_subset(self):
        kw = dict(prompt="Stories US-01 and AC-01.2 exist.")
        c = {"type": "ids_subset"}
        self.assertTrue(run(c, "US-01 has AC-01.2", **kw))
        self.assertFalse(run(c, "US-01 and US-07", **kw))
        self.assertTrue(run(dict(c, extra_allowed=["US-07"]), "US-07", **kw))
        m = dict(c, new_ids="need_marker", marker="proposed")
        self.assertTrue(run(m, "Proposed codes: US-07", **kw))
        self.assertFalse(run(m, "Codes: US-07", **kw))
        self.assertTrue(run(c, "TC-xx placeholders are not codes", **kw))

    def test_ids_all(self):
        c = {"type": "ids_all", "ids": ["US-01", "AC-01.1"]}
        self.assertTrue(run(c, "US-01, AC-01.1"))
        self.assertFalse(run(c, "US-01 and AC-01.12"))  # AC-01.12 is another code
        self.assertFalse(run(c, "US-010 and AC-01.1"))
        self.assertTrue(run(dict(c, min_coverage=0.5), "US-01"))

    def test_rows_recall_and_controls(self):
        spec = {"type": "rows", "min_recall": 1.0, "max_false": 0,
                "expect": [{"id": "a", "anchor": "AC-02", "any": ["vague"]},
                           {"id": "b", "anchor": ["US-04", "BR-02"], "any": ["contradict"]}],
                "controls": [{"id": "c", "anchor": "AC-01", "flag": "Blocker"}]}
        good = "| AC-02 | vague word |\n| US-04 vs BR-02 | contradiction |\n| AC-01 | Suggestion |"
        self.assertTrue(run(spec, good))
        self.assertFalse(run(spec, "| AC-02 | vague word |"))  # one defect missed
        self.assertFalse(run(spec, "| AC-02 | fine |\n| US-04 vs BR-02 | contradiction |"))  # right code, wrong reason
        self.assertFalse(run(spec, "| US-04 | contradiction |\n| AC-02 | vague |"))  # anchor needs both codes
        self.assertFalse(run(spec, good + "\n| AC-01 | Blocker |"))  # control flagged
        self.assertTrue(run(dict(spec, min_recall=0.5), "| AC-02 | vague |"))
        cont = "| AC-02 |\n  vague continues on the next line"
        self.assertTrue(run(dict(spec, min_recall=0.5), cont))

    def test_items_resolve(self):
        c = {"type": "items_resolve", "section": "Findings", "column": "^item", "min_rows": 1}
        src = dict(prompt='US-03 says "The client can do what they need".')
        head = "## Findings\n| # | Item |\n|---|---|\n"
        self.assertTrue(run(c, head + "| 1 | US-03 |", **src))
        self.assertTrue(run(c, head + '| 1 | "The client can do what they need" |', **src))
        self.assertFalse(run(c, head + "| 1 | US-99 |", **src))  # invented code
        self.assertFalse(run(c, head + "| 1 | the search part |", **src))  # no code, no quote
        self.assertFalse(run(c, head + '| 1 | "text nobody wrote" |', **src))
        self.assertFalse(run(dict(c, min_rows=2), head + "| 1 | US-03 |", **src))

    def test_numbers_from_input(self):
        src = dict(prompt="Allowed up to 24 hours (BR-02) on 2026-11-02.")
        c = {"type": "numbers_from_input"}
        self.assertTrue(run(c, "1. Up to 24 hours before AC-01.2 on 2026-11-02.", **src))
        self.assertFalse(run(c, "Within 2 seconds", **src))
        self.assertTrue(run(dict(c, allow=[2]), "Within 2 seconds", **src))
        col = {"type": "numbers_from_input", "section": "F", "column": "^proposal"}
        text = "## F\n| Item | Proposal |\n|---|---|\n| a | within 7 seconds |\n"
        self.assertFalse(run(col, text, **src))
        self.assertTrue(run(col, "## F\n| Item | Proposal |\n|---|---|\n| 7 | reword |\n", **src))  # other column ignored

    def test_no_vague_ac(self):
        c = {"type": "no_vague_ac", "section": "AC"}
        self.assertTrue(run(c, "## AC\n1. The page shows the slot.\n2. The search returns within 3 seconds, quickly."))
        self.assertFalse(run(c, "## AC\n1. The search is fast."))
        self.assertFalse(run(c, "## AC\n- It must be easy to use."))
        self.assertFalse(run(c, "## AC\n1. Hệ thống phản hồi nhanh."))
        self.assertTrue(run(dict(c, section_optional=True), "no section here"))
        self.assertFalse(run(c, "no section here"))

    def test_story_shape(self):
        c = {"type": "story_shape"}
        self.assertTrue(run(c, "As a patient, I want to log in with my email and password, so that I can enter."))
        self.assertFalse(run(c, "As a customer, I want to log in, reset my password and see my orders, so that x."))
        self.assertFalse(run(c, "As a customer I want to log in and reset and see orders"))
        self.assertTrue(run(c, "Là khách hàng, tôi muốn xem đơn, để biết trạng thái."))

    def test_verdict(self):
        base = {"type": "verdict", "section": "Verdict", "blockers_from": {"section": "Findings", "column": "^level"}}
        findings = "## Findings\n| # | Level |\n|---|---|\n| 1 | Blocker |\n"
        self.assertTrue(run(base, "## Verdict\n**Not ready**\n" + findings))
        self.assertFalse(run(base, "## Verdict\n**Ready**\n" + findings))  # Ready with a Blocker
        self.assertTrue(run(base, "## Verdict\n**Ready**\n## Findings\n| # | Level |\n|---|---|\n| 1 | Suggestion |\n"))
        self.assertFalse(run(base, "## Verdict\nNo verdict here"))
        self.assertFalse(run(dict(base, forbid=["Conditional"]), "## Verdict\n**Conditional**\n" + findings))
        self.assertFalse(run(dict(base, expect="Not ready"), "## Verdict\n**Conditional**\n" + findings))
        self.assertFalse(run(base, findings))  # no verdict section

    def test_column_values(self):
        c = {"type": "column_values", "column": "^level", "allowed": ["Blocker", "Should fix", "Suggestion"], "min_rows": 2}
        head = "| # | Level |\n|---|---|\n"
        self.assertTrue(run(c, head + "| 1 | Blocker |\n| 2 | should fix (late) |\n"))
        self.assertFalse(run(c, head + "| 1 | Blocker |\n| 2 | Critical |\n"))
        self.assertFalse(run(c, head + "| 1 | Blocker |\n"))  # too few rows
        self.assertFalse(run(c, "no table"))

    def test_table_columns(self):
        c = {"type": "table_columns", "columns": ["^code", "^owner"], "min_rows": 1}
        self.assertTrue(run(c, "| Code | Owner |\n|---|---|\n| R1 | Ann |\n"))
        self.assertFalse(run(c, "| Code | Status |\n|---|---|\n| R1 | Open |\n"))
        self.assertFalse(run(c, "| Code | Owner |\n|---|---|\n"))  # header only
        self.assertFalse(run(c, "Code, Owner: none"))

    def test_language(self):
        vi = "Khách hàng đã đăng nhập xem danh sách đơn hàng của mình."
        self.assertTrue(run({"type": "language", "lang": "vi"}, vi))
        self.assertFalse(run({"type": "language", "lang": "vi"}, "The customer sees the list."))
        self.assertTrue(run({"type": "language", "lang": "en"}, "The customer sees the list."))
        self.assertFalse(run({"type": "language", "lang": "en"}, vi))

    def test_verbatim(self):
        c = {"type": "verbatim", "phrases": ["only the first confirmation succeeds"]}
        self.assertTrue(run(c, "AC: Only  the first\nconfirmation **succeeds**".replace("**", "")))
        self.assertFalse(run(c, "the first confirmation wins"))

    def test_distinct_terms(self):
        c = {"type": "distinct_terms", "terms": ["Inspection", "Analysis", "Test"], "min": 2}
        self.assertTrue(run(c, "inspection and test"))
        self.assertFalse(run(c, "contest of inspection"))  # "contest" is not "test"

    def test_link_requires_marker(self):
        c = {"type": "link_requires_marker", "anchor": ["US-04", "GOAL-02"], "marker": "proposed|to confirm"}
        self.assertTrue(run(c, "Nothing links them."))
        self.assertTrue(run(c, "- US-04 to GOAL-02: proposed, to confirm"))
        self.assertFalse(run(c, "| US-04 | GOAL-02 | covered |"))
        self.assertFalse(run(c, "- US-04 to GOAL-02: proposed\n- US-04 -> GOAL-02 is a fact"))

    def test_any_of(self):
        c = {"type": "any_of", "checks": [{"type": "match", "pattern": "alpha"}, {"type": "match", "pattern": "beta"}]}
        self.assertTrue(run(c, "beta"))
        self.assertFalse(run(c, "gamma"))

    def test_a_crashing_check_fails(self):
        self.assertFalse(run({"type": "rows", "expect": [{"id": "a"}]}, "text"))  # missing key
        self.assertFalse(run({"type": "match", "pattern": "x", "section": ["S"]}, "text"))

    def test_no_missing_resource(self):
        kw = dict(kind="standalone", install=["requirements-review"], skill="requirements-review")
        c = {"type": "no_missing_resource"}
        ok = [
            "Short form is in `templates/review-report.md`.",
            "See references/quality-characteristics.md.",
            "More in the requirements-document skill, if installed.",
            "requirements-review/references/iso29148.md has the list.",
            "The requirements-elicitation skill is not installed here, so the short form is used.",
            "I cannot confirm the outline against clause 9.6.",
        ]
        bad = [
            "See `requirements-elicitation/references/item-tracking.md`.",
            "See references/does-not-exist.md.",
            "See `templates/story-template.md`.",  # exists, but in a skill that is not installed
            "requirements-review/references/nope.md",
            "I could not read the requirements-document skill.",
            "Unable to find requirements-trace, so I skipped it.",
            "scripts/fin.py is not available.",
        ]
        for t in ok:
            with self.subTest(t):
                self.assertTrue(run(c, t, **kw))
        for t in bad:
            with self.subTest(t):
                self.assertFalse(run(c, t, **kw))


class Mutations(unittest.TestCase):
    """Small edits to a good golden must fail the check built to catch them, and only that one."""

    def check(self, case_id, mutate, expected):
        good = golden(case_id, "good")
        mutated = mutate(good)
        self.assertNotEqual(mutated, good, "mutation did not change the text")
        self.assertEqual(failed_ids(case_id, mutated), set(expected))

    def test_review_verdict_ready_with_blockers(self):
        self.check("rr-main", lambda t: t.replace("**Not ready**", "**Ready**"), {"verdict-consistent"})

    def test_review_flags_a_fine_item(self):
        row = "| 7 | Should fix | AC-01.2 \"only the first confirmation succeeds\" | Concise | Wordy | Shorten | Suspicion |\n"
        self.check("rr-main", lambda t: t.replace("\n## 4.", "\n" + row + "\n## 4.", 1), {"seeded-defects-found"})

    def test_review_drops_two_seeded_defects(self):
        def drop(t):
            return "\n".join(l for l in t.splitlines() if not l.startswith(("| 5 |", "| 6 |")))
        self.check("rr-main", drop, {"seeded-defects-found"})

    def test_review_tolerates_one_missed_defect(self):
        def drop(t):
            return "\n".join(l for l in t.splitlines() if not l.startswith("| 6 |"))
        self.assertEqual(failed_ids("rr-main", drop(golden("rr-main", "good"))), set())

    def test_review_right_code_wrong_reason(self):
        def hollow(t):
            t = t.replace("Contradiction: US-04 allows cancelling at any time, BR-02 limits it to 24 hours", "Needs a rewrite")
            t = t.replace('US-05 "Reminders" ("No acceptance criteria yet.")', 'US-05 "Reminders"')
            return t.replace("The story has no AC, so it cannot be tested or estimated", "Unclear")
        mutated = hollow(golden("rr-main", "good"))
        self.assertNotEqual(mutated, golden("rr-main", "good"))
        self.assertIn("seeded-defects-found", failed_ids("rr-main", mutated))  # two codes kept, two reasons gone

    def test_review_proposal_invents_a_number(self):
        self.check("rr-main", lambda t: t.replace("within [value to be confirmed] seconds", "within 2 seconds"),
                   {"proposals-add-no-numbers"})

    def test_review_finding_cites_text_nobody_wrote(self):
        self.check("rr-main", lambda t: t.replace('| AC-02.1 "The system should respond quickly when the customer searches for a doctor" |',
                                                  '| The search screen |'), {"findings-point-at-input"})

    def test_review_unknown_level(self):
        self.check("rr-main", lambda t: t.replace("| Should fix | AC-02.1", "| Major | AC-02.1"),
                   {"severity-vocabulary"})

    def test_review_vague_case_overclaims(self):
        self.check("rr-vague", lambda t: t + "\nThe story passes.", {"no-overclaim"})

    def test_review_vague_case_loses_the_limits(self):
        self.check("rr-vague", lambda t: re.sub(r"- Could not be checked.*", "- Everything was checked.", t), {"scope-states-limits"})

    def test_trace_invented_code(self):
        self.check("rt-main", lambda t: t.replace("| - | US-05 |", "| - | US-09, US-05 |"), {"no-invented-codes"})

    def test_trace_catalogue_misses_an_item(self):
        self.check("rt-main", lambda t: t.replace("| BR-01, BR-02, BR-03, BR-04 |", "| BR-01, BR-02, BR-04 |"),
                   {"catalogue-lists-every-item"})

    def test_trace_flags_a_covered_goal(self):
        self.check("rt-main", lambda t: t.replace("## Contradictions", "| 7 | Orphan | GOAL-01 | High | no goal |\n\n## Contradictions"),
                   {"seeded-gaps-found"})

    def test_trace_unfounded_link_stated_as_fact(self):
        def fact(t):
            return re.sub(r"- You asked me to link.*", "- US-04 is linked to GOAL-02, as you asked.", t)
        self.check("rt-trap", fact, {"unfounded-link-is-marked"})

    def test_trace_invented_test_codes(self):
        self.check("rt-trap", lambda t: t + "\n| TC-01 | US-04 |", {"no-invented-test-codes"})

    def test_trace_codes_without_marker(self):
        self.check("rt-vague", lambda t: t.replace("proposed", "assigned").replace("Proposed", "Assigned"),
                   {"codes-are-marked-proposed", "says-codes-are-proposed"})

    def test_document_changes_the_wording(self):
        self.check("rd-main", lambda t: t.replace("only the first confirmation succeeds", "the first confirmation wins"),
                   {"wording-kept"})

    def test_document_invents_a_requirement(self):
        self.check("rd-main", lambda t: t + "\n- FR-10 The system shall respond within 2 seconds.", {"no-invented-codes"})

    def test_document_fills_an_empty_section(self):
        self.check("rd-trap", lambda t: t.replace("Not yet available. Needed: stakeholder list, from the business owner (requirements-stakeholders).",
                                                  "Patients and the clinic manager."), {"gaps-stay-visible"})

    def test_document_trap_new_number(self):
        self.check("rd-trap", lambda t: t.replace("NFR-PERF-01 The system should be fast.",
                                                  "NFR-PERF-01 The system should be fast, under 3 seconds."),
                   {"no-invented-numbers"})

    def test_document_raw_notes_become_a_document(self):
        self.check("rd-vague", lambda t: t + "\n- FR-01 Patients shall book online.", {"no-requirement-codes-made-up"})

    def test_document_asks_too_many_questions(self):
        self.check("rd-vague", lambda t: t + "\n4. When? 5. Why?", {"at-most-three-questions"})

    def test_story_nfr_inside_ac(self):
        self.check("sw-main", lambda t: t.replace("the system rejects it", "the system answers within 3 seconds and rejects it"),
                   {"nfr-not-in-ac"})

    def test_story_invented_threshold(self):
        self.check("sw-trap", lambda t: t.replace("2. When a wrong password is entered",
                                                  "2. After 5 wrong passwords the account is locked.\n3. When a wrong password is entered"),
                   {"no-invented-threshold"})

    def test_story_vague_ac(self):
        self.check("sw-trap", lambda t: t.replace("then the customer reaches the account page", "then the page opens fast"),
                   {"no-vague-ac"})

    def test_story_generic_role(self):
        self.check("sw-main", lambda t: t.replace("As a registered patient,", "As a user,"),
                   {"specific-role", "not-generic-user"})

    def test_story_reply_in_the_wrong_language(self):
        self.check("sw-vague", lambda t: "As a customer, I want to see my orders. " * 4 + "\n**Assumptions**: orders are listed",
                   {"vietnamese"})

    def test_standalone_cites_a_file_that_is_not_there(self):
        self.check("rr-standalone-tracking", lambda t: t + "\nSee requirements-elicitation/references/item-tracking.md.",
                   {"no-missing-resource"})
        self.check("rr-standalone-tracking", lambda t: t + "\nSee `references/missing-file.md`.", {"no-missing-resource"})

    def test_standalone_may_cite_its_own_files(self):
        case_id = "rr-standalone-tracking"
        self.assertEqual(failed_ids(case_id, golden(case_id, "good") + "\nShort form: `templates/review-report.md`."), set())

    def test_standalone_loses_the_task(self):
        def no_tracking(t):
            return t.split("## 5. Tracking items")[0]
        self.check("rr-standalone-tracking", no_tracking, {"tracking-table"})

    def test_standalone_claims_compliance(self):
        self.check("rr-standalone-iso", lambda t: t + "\nThe outline is fully compliant.", {"no-claim-of-compliance"})

    def test_standalone_asks_no_keyword_question(self):
        self.check("rd-standalone", lambda t: re.sub(r"Question:.*", "Shall is used throughout.", t),
                   {"asks-which-keyword-convention"})

    def test_standalone_verification_method_outside_the_four(self):
        self.check("rt-standalone", lambda t: t.replace("| Test |", "| Review |"), {"method-per-requirement"})

    def test_standalone_story_review_loses_the_table(self):
        self.check("sw-standalone", lambda t: t.split("Rewritten")[1] and "Rewritten" + t.split("Rewritten")[1],
                   {"review-table", "names-the-characteristics"})


class Independence(unittest.TestCase):
    """Guards that do not depend on the expectations written next to the goldens."""

    def test_alternative_valid_answers_pass(self):
        # written after the checks, in other words and layouts than the goldens
        files = sorted((GOLDEN / "alternatives").glob("*.md"))
        self.assertGreaterEqual(len(files), 4)
        for f in files:
            case = CASES[f.name.split(".")[0]]
            with self.subTest(f.name):
                r = grade.grade_case(case, f.read_text(encoding="utf-8"), meta_for(case))
                self.assertEqual(r["failed"], [], [c for c in r["checks"] if not c["ok"]])

    def test_the_source_text_alone_never_satisfies_an_expectation(self):
        # a finding that only quotes the item must not count as having found the problem
        for cid, case in CASES.items():
            lines = []
            for name in case.get("fixtures", []):
                lines += (EVALS / "fixtures" / name).read_text(encoding="utf-8").splitlines()
            lines += case["prompt"].splitlines()
            for chk in case["checks"]:
                for e in chk.get("expect", []) if chk["type"] == "rows" else []:
                    anchors = grade.as_list(e["anchor"])
                    for line in lines:
                        if all(re.search(a, line, re.I) for a in anchors):
                            with self.subTest(f"{cid}/{e['id']}"):
                                self.assertFalse(any(re.search(k, line, re.I) for k in e.get("any", [])),
                                                 f"quoting {line!r} already satisfies {e['id']}")

    def test_blockers_cannot_be_missed_even_when_recall_is_met(self):
        # severity from the skill's own text: Blocker = cannot be built, tested or approved
        # (requirements-review); High rows of references/coverage-checks.md (requirements-trace)
        by_case = {cid: {c["id"]: {e["id"] for e in c["expect"] if e.get("required")}
                         for c in case["checks"] if c["type"] == "rows" and "expect" in c}
                   for cid, case in CASES.items()}
        self.assertEqual(by_case["rr-main"]["seeded-defects-found"],
                         {"generic-unfinished-story", "contradiction-with-rule", "missing-ac"})
        self.assertEqual(by_case["rt-main"]["seeded-gaps-found"],
                         {"abandoned-goal", "orphan-story", "story-without-ac", "window-contradiction"})

    def test_missing_a_blocker_fails_but_missing_an_optional_finding_does_not(self):
        good = golden("rr-main", "good")
        no_contradiction = "\n".join(l for l in good.splitlines() if not l.startswith("| 3 |"))
        no_terminology = "\n".join(l for l in good.splitlines() if not l.startswith("| 5 |"))
        self.assertEqual(failed_ids("rr-main", no_contradiction), {"seeded-defects-found"})
        self.assertEqual(failed_ids("rr-main", no_terminology), set())
        good = golden("rt-main", "good")
        no_orphan = "\n".join(l for l in good.splitlines() if not l.startswith("| 2 |"))
        no_br03 = "\n".join(l for l in good.splitlines() if not l.startswith("| 4 |"))
        self.assertEqual(failed_ids("rt-main", no_orphan), {"seeded-gaps-found"})
        self.assertEqual(failed_ids("rt-main", no_br03), set())

    def test_one_stuffed_row_counts_once(self):
        stuffed = ("## Findings\n| # | Level | Item |\n|---|---|---|\n"
                   "| 1 | Blocker | AC-02.1 US-03 AC-04.1 BR-02 US-05 customer client NFR-USA-01 "
                   "vague measur contradict no AC missing terminology |\n")
        c = {"type": "rows", "section": "Findings", "min_recall": 0.5, "expect": [
            {"id": "a", "anchor": "AC-02", "any": ["vague"]}, {"id": "b", "anchor": "US-03", "any": ["vague"]},
            {"id": "c", "anchor": "US-05", "any": ["missing"]}, {"id": "d", "anchor": "BR-02", "any": ["contradict"]}]}
        self.assertFalse(run(c, stuffed))
        separate = stuffed + "| 2 | Blocker | US-03 vague |\n| 3 | Blocker | US-05 missing |\n"
        self.assertTrue(run(c, separate))

    def test_one_row_can_serve_two_expectations_only_if_another_row_serves_the_other(self):
        c = {"type": "rows", "expect": [{"id": "a", "anchor": "X-1", "any": ["bad"]},
                                        {"id": "b", "anchor": "X-1", "any": ["bad"]}]}
        self.assertFalse(run(c, "- X-1 is bad"))
        self.assertTrue(run(c, "- X-1 is bad\n- X-1 is also bad"))
        # matching is by assignment: the first row fits both, the second only fits b
        c = {"type": "rows", "expect": [{"id": "a", "anchor": "X-1", "any": ["bad"]},
                                        {"id": "b", "anchor": "X-1", "any": ["bad", "worse"]}]}
        self.assertTrue(run(c, "- X-1 is bad\n- X-1 is worse"))

    def test_invented_amounts_are_found_in_every_spelling(self):
        src = dict(prompt="The account should lock after a few wrong passwords.")
        c = {"type": "numbers_from_input"}
        for bad in ["after five wrong passwords", "for thirty minutes", "for ten-minute", "after 5 wrong passwords",
                    "within 3s", "within 3 sec", "for 1,000 users", "for twenty users"]:
            with self.subTest(bad):
                self.assertFalse(run(c, bad, **src))
        for ok in ["two stories", "one appointment", "see question 2", "item 3 above", "#4", "the 9 quality characteristics".replace("9", "nine")]:
            with self.subTest(ok):
                self.assertTrue(run(c, ok, **src))
        self.assertTrue(run(c, "after five wrong passwords", prompt="lock after five wrong passwords"))

    def test_look_alike_codes_are_still_codes(self):
        src = dict(prompt="Stories US-01 and AC-01.2 exist.")
        c = {"type": "ids_subset"}
        for bad in ["US\u201199", "US\u201399", "US-99a", "US-099"]:
            with self.subTest(bad):
                self.assertFalse(run(c, bad, **src))
        self.assertTrue(run(c, "US\u201101 is fine", **src))

    def test_code_ranges_count_as_listed(self):
        c = {"type": "ids_all", "ids": ["US-01", "US-02", "US-03", "GOAL-01"]}
        self.assertTrue(run(c, "US-01 to US-03 and GOAL-01"))
        self.assertTrue(run(c, "US-01..US-03, GOAL-01"))
        self.assertFalse(run(c, "US-01 to US-02 and GOAL-01"))
        self.assertFalse(run(c, "US-03 to US-01, GOAL-01"))  # a backwards range lists nothing

    def test_new_codes_need_the_marker_next_to_them(self):
        c = {"type": "ids_subset", "new_ids": "need_marker", "marker": "proposed"}
        self.assertTrue(run(c, "I propose, as proposed codes: US-01, US-02"))
        self.assertFalse(run(c, "US-01 is the booking story.\n\nNothing else was proposed."))
        self.assertTrue(run(c, "| Code | Status |\n|---|---|\n| US-01 | proposed |"))

    def test_links_check(self):
        c = {"type": "links", "together": [["G-1", "US-1"]], "never": [["G-1", "US-3"]]}
        self.assertTrue(run(c, "| G-1 | US-1, US-2 |"))
        self.assertFalse(run(c, "| G-2 | US-1 |"))
        self.assertFalse(run(c, "| G-1 | US-1, US-3 |"))
        self.assertFalse(run(c, "| G-1 | US-10 |"))  # US-10 is not US-1

    def test_a_refusal_that_names_the_word_is_not_a_claim(self):
        c = {"type": "not_match", "pattern": r"\bpasses\b", "unless_negated": True}
        self.assertTrue(run(c, "I cannot tell you the document passes."))
        self.assertTrue(run(c, "It is not ready, so it does not say it passes."))
        self.assertFalse(run(c, "I cannot sign off yet.\nThe document passes."))
        self.assertFalse(run(c, "The document passes."))

    def test_a_measured_amount_excuses_a_vague_word_but_a_bare_digit_does_not(self):
        c = {"type": "no_vague_ac", "section": "AC"}
        self.assertTrue(run(c, "## AC\n1. The search returns within 3 seconds, quickly."))
        self.assertFalse(run(c, "## AC\n1. When 2 patients search, the system answers quickly."))


class LiveOutputFixes(unittest.TestCase):
    """Fixes made after grading the first live run (Sonnet 5.5). Each one is tested both ways:
    a valid answer is no longer rejected, and the invention it must still catch is still caught."""

    # --- markdown emphasis is dropped before a pattern is applied
    def test_emphasis_is_ignored_by_patterns(self):
        c = {"type": "match", "pattern": r"\bAs an? [\w ]{0,25}patient\b"}
        self.assertTrue(run(c, "**As a** registered patient, I want x"))
        self.assertTrue(run(c, "*As a* patient, I want x"))
        self.assertTrue(run(c, "__As a__ patient"))
        self.assertFalse(run(c, "**As a** user, I want x"))  # still the wrong role
        generic = {"type": "not_match", "pattern": r"\bAs a user\b"}
        self.assertFalse(run(generic, "**As a** user, I want x"))  # and the generic role is still seen through bold

    def test_emphasis_stripping_leaves_bullets_math_and_names_alone(self):
        self.assertEqual(grade.strip_emphasis("* item *kept* and **bold** and __b__"), "* item kept and bold and b")
        self.assertEqual(grade.strip_emphasis("2 * 3 * 4"), "2 * 3 * 4")
        self.assertEqual(grade.strip_emphasis("snake_case_name and 5*6"), "snake_case_name and 5*6")

    def test_invention_inside_bold_is_still_caught(self):
        c = {"type": "numbers_from_input"}
        self.assertFalse(run(c, "**within 5 seconds**", prompt="Be quick."))

    # --- numbers: list numbering and example data are not made-up figures
    def test_list_numbers_and_labels_are_not_figures(self):
        c = {"type": "numbers_from_input"}
        src = dict(prompt="Allowed up to 24 hours.")
        for ok in ["2.3 Scope", "| 1 | Add the benefit (F2) |", "See Q4 and A1", "10. Missing attributes",
                   "Resolve items 1\u20137 in section 11", "see questions 3 to 5"]:
            with self.subTest(ok):
                self.assertTrue(run(c, ok, **src))
        self.assertTrue(run(c, "Given the move in AC1 and AC 3 (see A2)", **src))
        for bad in ["P95 under 2 seconds", "after 4 failed attempts", "| x | 10 minutes |", "F2 within 7 seconds"]:
            with self.subTest(bad):
                self.assertFalse(run(c, bad, **src))

    def test_dates_and_times_in_given_when_then_are_example_data(self):
        c = {"type": "numbers_from_input"}
        src = dict(prompt="A move is allowed up to 24 hours before the start.")
        for ok in ["- Given an appointment on 10 Nov at 09:00, more than 24 hours away",
                   "- When the patient moves it to 14:30 on Nov 12, 2027",
                   "- Given it starts in exactly 24 hours 00 minutes",
                   "- Then the slot of 3rd March 9:15 am is free",
                   "- Then:\n  - the patient holds Mon 14:00\n  - and no longer holds Fri 10:00"]:
            with self.subTest(ok):
                self.assertTrue(run(c, ok, **src))
        for bad in ["The reminder is sent at 08:00 every Monday",  # not an example line
                    "- Given an appointment on 10 Nov, when it is moved within 5 seconds",
                    "- Given a patient, when the move takes 10 minutes",
                    "- Then the account locks after 3 wrong passwords",
                    "- Then:\n  - it is accepted\n- Notes:\n  - the cut-off is 10:00"]:  # a sibling list is not under the Then
            with self.subTest(bad):
                self.assertFalse(run(c, bad, **src))

    def test_what_the_input_already_allows_is_unchanged(self):
        c = {"type": "numbers_from_input"}
        src = dict(prompt="Given a slot on 2026-11-02 at 09:00, show it.")
        self.assertTrue(run(c, "The reminder cites 09:00.", **src))  # the input has it

    # --- sections: the title carries text, aliases, sub-sections
    def test_verdict_can_sit_on_the_heading(self):
        c = {"type": "verdict", "section": "Verdict", "blockers_from": {"section": "Findings", "column": "^level"}}
        findings = "## Findings\n| # | Level |\n|---|---|\n| 1 | Blocker |\n"
        self.assertTrue(run(c, "## Verdict: Not ready\nfour blockers\n" + findings))
        self.assertTrue(run(c, "## 2. Verdict \u2013 Conditional\n" + findings))
        self.assertFalse(run(c, "## Verdict: Ready\n" + findings))  # still contradicts the Blocker
        self.assertFalse(run(c, "## Verdict\nNo opinion\n" + findings))
        self.assertFalse(run(dict(c, forbid=["Not ready"]), "## Verdict: Not ready\n" + findings))

    def test_title_text_counts_for_the_section(self):
        c = {"type": "match", "section": ["NFRs found"], "pattern": "nfr-writer"}
        self.assertTrue(run(c, "## NFRs found (hand off to nfr-writer)\n- fast"))
        self.assertFalse(run(c, "## NFRs found\n- fast"))
        self.assertFalse(run(c, "## Other (nfr-writer)\n## NFRs found\n- fast"))  # another section's title

    def test_equivalent_section_names(self):
        c = {"type": "sections", "names": [["Questions needing an answer", "Questions"]]}
        self.assertTrue(run(c, "## Open questions\n1. Is it 24 hours?"))
        self.assertTrue(run({"type": "sections", "names": ["Questions needing an answer"]}, "**Open questions for the owner:**\n- x?"))
        self.assertFalse(run(c, "## Open items\n1. x"))
        self.assertFalse(run({"type": "sections", "names": ["Findings"]}, "## Open questions\n1. x"))

    def test_sub_sections_do_not_cut_the_section(self):
        text = "## Gaps\n**High**\n- GOAL-03 has no story\n**Low**\n- x\n### Detail\ny\n## To confirm\nz"
        self.assertIn("GOAL-03", grade.get_section(text, "Gaps"))
        self.assertIn("y", grade.get_section(text, "Gaps"))
        self.assertNotIn("z", grade.get_section(text, "Gaps"))  # a peer heading still ends it
        self.assertEqual(grade.get_section(text, "High").strip(), "- GOAL-03 has no story")  # a sub-section is still found by name
        self.assertEqual(grade.get_section(text, "Detail").strip(), "y")
        c = {"type": "rows", "section": "Gaps", "expect": [{"id": "g", "anchor": "GOAL-03", "any": ["no story"]}]}
        self.assertTrue(run(c, text))
        self.assertFalse(run(c, "## Gaps\n**High**\n- x\n## To confirm\n- GOAL-03 has no story"))  # the finding is elsewhere

    def test_a_nested_section_with_a_matching_name_is_not_counted_twice(self):
        text = "## Gaps\n### Gaps in detail\n1. a\n2. b\n"
        c = {"type": "match", "section": "Gaps", "pattern": r"^\d+\.", "flags": "m", "max": 2}
        self.assertTrue(run(c, text))

    def test_a_name_matches_whole_words_of_a_title(self):
        text = "## ACC-01 Log in\nx\n**AC:**\n1. y\n## Acceptance criteria\nz"
        self.assertNotIn("x", grade.get_section(text, "AC"))  # `ACC-01 Log in` is not the section AC
        self.assertIn("y", grade.get_section(text, "AC"))
        self.assertIsNotNone(grade.get_section("## Gaps in detail\nq", "Gaps"))
        self.assertIsNotNone(grade.get_section("## Ready for approval? No.\nq", "Ready for approval"))
        self.assertIsNone(grade.get_section("## Gapsx\nq", "Gaps"))

    def test_section_numbers_in_headings(self):
        text = "## 11. Appendices\n### 11.2 What is still missing\n- gaps\n### 11.3 Ready for approval?\nNo."
        self.assertIn("gaps", grade.get_section(text, "What is still missing"))
        self.assertIsNotNone(grade.get_section(text, "Ready for approval"))
        self.assertIsNone(grade.get_section("## 2024 plans\nx", "plans"))  # a year is not numbering

    # --- codes: an example standard is not a made-up requirement
    def test_codes_offered_as_examples(self):
        src = dict(prompt="REQ-03 The patient data shall be encrypted.")
        c = {"type": "ids_subset"}
        for ok in ["It names no algorithm, such as AES-256 or SHA-1.", "e.g. UTF-8 text", "for example ISO-8601 dates",
                   "ví dụ như AES-256"]:
            with self.subTest(ok):
                self.assertTrue(run(c, ok, **src))
        for bad in ["Add TC-01 for this", "for example TC-01 covers it", "such as US-99", "Use AES-256 here",
                    "the likelihood AES-256", "such as AES-256.\nTC-02 covers it"]:
            with self.subTest(bad):
                self.assertFalse(run(c, bad, **src))


class FiveStrictChecks(unittest.TestCase):
    """The five strict spots found in the first live run; each is tested both ways."""

    def test_second_the_ordinal_is_not_seconds(self):
        c = CASES["sw-main"]["checks"]
        c = next(x for x in c if x["id"] == "nfr-not-in-ac")
        body = "## Acceptance criteria\n"
        for ok in ["5. Second appointment with the same doctor", "The second move is refused"]:
            with self.subTest(ok):
                self.assertTrue(run(c, body + ok))
        for bad in ["1. The move completes within 3 seconds", "1. Done in 3-second", "1. It takes 2.5 secs", "1. It answers in seconds",
                    "1. Done in 3 sec"]:
            with self.subTest(bad):
                self.assertFalse(run(c, body + bad))

    def test_parameters_and_counter_reset_are_not_figures(self):
        c = {"type": "numbers_from_input"}
        src = dict(prompt="Lock after a few wrong passwords.")
        for ok in ["Given N\u22121 wrong passwords, when the Nth is sent", "after N-1 failures", "the counter resets to 0",
                   "a correct login sets the failure count back to 0"]:
            with self.subTest(ok):
                self.assertTrue(run(c, ok, **src))
        for bad in ["after 5 wrong passwords", "within 0 seconds", "locks for 10 minutes", "the limit is 3-1", "retry after 0 tries",
                    "returns 1 result"]:
            with self.subTest(bad):
                self.assertFalse(run(c, bad, **src))

    def test_quoted_message_is_not_a_vague_requirement(self):
        c = {"type": "no_vague_ac"}
        self.assertTrue(run(c, '5. When nothing matches, show "Không tìm thấy đơn hàng phù hợp"'))
        self.assertTrue(run(c, '5. The page shows \u201cNo suitable doctor\u201d'))
        self.assertFalse(run(c, '5. The result is phù hợp and the page says "None"'))
        self.assertFalse(run(c, '5. The search is fast, as in "fast".'))

    def test_cant_is_cannot(self):
        c = {"type": "match", "pattern": "cannot be tested"}
        self.assertTrue(run(c, "The story can't be tested."))
        self.assertTrue(run(c, "The story can\u2019t be tested."))
        self.assertTrue(run(c, "The story cannot be tested."))
        self.assertFalse(run(c, "The story can be tested."))
        self.assertFalse(run(c, "The story couldn't be tested."))

    def test_no_ac_for_a_rule_is_not_a_missing_ac(self):
        ctl = next(x for x in CASES["rt-main"]["checks"] if x["id"] == "seeded-gaps-found")["controls"][0]
        c = {"type": "rows", "controls": [ctl]}
        self.assertTrue(run(c, "| 10 | Missing cases | US-01 has no AC for BR-01 (a second booking) | Medium |"))
        self.assertFalse(run(c, "| 3 | Story with no AC | US-01 | High |"))
        self.assertFalse(run(c, "| 3 | Story with no AC. | US-01 has no AC. | High |"))
        self.assertFalse(run(c, "| 1 | Orphan | US-01 | High |"))


class Isolation(unittest.TestCase):
    def status(self, meta, cid="rt-standalone"):
        return grade.grade_case(CASES[cid], golden(cid, "good"), meta)

    def test_only_a_record_that_shows_the_skill_and_nothing_else_passes(self):
        self.assertEqual(self.status({"loaded_skills": ["requirements-trace"]})["status"], "pass")
        self.assertEqual(self.status({"loaded_skills": ["requirements-trace", "commit"]})["status"], "pass")

    def test_a_record_without_the_skill_under_test_is_not_proof(self):
        for loaded in ([], ["commit"], ["story-writer"]):
            with self.subTest(loaded):
                r = self.status({"loaded_skills": loaded})
                self.assertEqual((r["status"], r["isolation"]), ("fail", "violated"))

    def test_other_suite_skills_loaded_fail(self):
        r = self.status({"loaded_skills": ["requirements-trace", "nfr-writer"]})
        self.assertEqual((r["status"], r["isolation"]), ("fail", "violated"))

    def test_unusable_records_are_unverified(self):
        for meta in (None, {}, {"loaded_skills": None}, {"loaded_skills": "requirements-trace"},
                     {"loaded_skills": [["requirements-trace"]]}, {"loaded_skills": [1]}, {"unreadable": True}, [], "x"):
            with self.subTest(meta):
                r = self.status(meta)
                self.assertEqual((r["status"], r["isolation"]), ("unverified", "unverified"))

    def test_names_are_exact(self):
        self.assertEqual(self.status({"loaded_skills": ["Requirements-Trace"]})["status"], "fail")

    def test_two_skill_runs_keep_each_case_separate(self):
        r = self.status({"loaded_skills": ["requirements-review"]}, "rr-standalone-iso")
        self.assertEqual(r["status"], "pass")
        r = self.status({"loaded_skills": ["requirements-trace"]}, "rr-standalone-iso")
        self.assertEqual(r["status"], "fail")


class StatusMatrix(unittest.TestCase):
    """Every mix of results: exit code, printed summary, automatic.json and the files written agree."""

    def run_grade(self, passing=(), failing=(), unverified=(), allow_missing=False):
        import contextlib
        import io
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            for cid in passing:
                (out / f"{cid}.md").write_text(golden(cid, "good"), encoding="utf-8")
            for cid in failing:
                (out / f"{cid}.md").write_text(golden(cid, "bad"), encoding="utf-8")
            for cid in unverified:
                (out / f"{cid}.md").write_text(golden(cid, "good"), encoding="utf-8")
            for cid in list(passing) + list(failing):
                if CASES[cid]["kind"] == "standalone":
                    (out / f"{cid}.meta.json").write_text(json.dumps({"loaded_skills": CASES[cid]["install"]}))
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = grade.main(["grade", str(out)] + (["--allow-missing"] if allow_missing else []))
            auto = {r["id"]: r["status"] for r in json.loads((out / "automatic.json").read_text())}
            return code, buf.getvalue(), auto

    def summary(self, text):
        return re.search(r"(\d+) pass, (\d+) fail, (\d+) unverified isolation, (\d+) missing", text).groups()

    def test_only_passes(self):
        code, text, auto = self.run_grade(passing=["sw-main", "rt-standalone"])
        self.assertEqual((code, self.summary(text)), (3, ("2", "0", "0", "15")))  # 15 outputs missing
        self.assertEqual(set(auto.values()), {"pass"})

    def test_a_failure(self):
        code, text, auto = self.run_grade(passing=["sw-main"], failing=["rr-main"])
        self.assertEqual((code, self.summary(text)[:3]), (1, ("1", "1", "0")))  # fail outranks missing
        self.assertIn("FAIL       rr-main", text)
        self.assertEqual(auto, {"sw-main": "pass", "rr-main": "fail"})

    def test_unverified_is_not_a_pass(self):
        code, text, auto = self.run_grade(passing=["sw-main"], unverified=["rt-standalone"])
        self.assertEqual((code, self.summary(text)[:3]), (3, ("1", "0", "1")))  # missing outranks unverified
        self.assertIn("UNVERIFIED rt-standalone", text)
        self.assertEqual(auto["rt-standalone"], "unverified")
        code, _, _ = self.run_grade(passing=["sw-main"], unverified=["rt-standalone"], allow_missing=True)
        self.assertEqual(code, 2)  # a subset run: unverified is still not 0

    def test_failure_and_unverified_together(self):
        code, text, auto = self.run_grade(failing=["rr-main"], unverified=["rt-standalone"])
        self.assertEqual((code, self.summary(text)[:3]), (1, ("0", "1", "1")))
        self.assertEqual(auto, {"rr-main": "fail", "rt-standalone": "unverified"})

    def test_a_failing_standalone_case_with_no_record_is_a_failure_not_unverified(self):
        code, _, auto = self.run_grade(unverified=["rt-standalone"], failing=[])
        self.assertEqual(auto["rt-standalone"], "unverified")
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "rt-standalone.md").write_text(golden("rt-standalone", "bad"), encoding="utf-8")
            self.assertEqual(grade.main(["grade", tmp]), 1)

    def test_missing_outputs_are_never_a_zero_by_default(self):
        code, text, _ = self.run_grade(passing=["sw-main"])
        self.assertEqual((code, self.summary(text)), (3, ("1", "0", "0", "16")))
        self.assertIn("MISSING    rr-main", text)

    def test_priority_is_fail_then_missing_then_unverified_then_pass(self):
        # fail + missing + unverified
        code, text, auto = self.run_grade(failing=["rr-main"], unverified=["rt-standalone"])
        self.assertEqual((code, self.summary(text)[:3]), (1, ("0", "1", "1")))
        # missing + unverified (no fail)
        self.assertEqual(self.run_grade(unverified=["rt-standalone"])[0], 3)
        # fail + missing (no unverified)
        self.assertEqual(self.run_grade(failing=["rr-main"])[0], 1)
        # unverified only, on a complete run
        every = [c for c in CASES if c != "rt-standalone"]
        code, text, _ = self.run_grade(passing=every, unverified=["rt-standalone"])
        self.assertEqual((code, self.summary(text)), (2, ("16", "0", "1", "0")))
        # fail + unverified on a complete run
        every = [c for c in CASES if c not in ("rt-standalone", "rr-main")]
        code, text, _ = self.run_grade(passing=every, failing=["rr-main"], unverified=["rt-standalone"])
        self.assertEqual((code, self.summary(text)), (1, ("15", "1", "1", "0")))

    def test_allow_missing_only_ignores_missing(self):
        self.assertEqual(self.run_grade(passing=["sw-main"], allow_missing=True)[0], 0)
        self.assertEqual(self.run_grade(failing=["rr-main"], allow_missing=True)[0], 1)
        self.assertEqual(self.run_grade(unverified=["rt-standalone"], allow_missing=True)[0], 2)
        self.assertEqual(self.run_grade(allow_missing=True)[0], 0)  # nothing graded, nothing wrong, but nothing proven

    def test_nothing_graded(self):
        code, text, auto = self.run_grade()
        self.assertEqual((code, self.summary(text), auto), (3, ("0", "0", "0", "17"), {}))

    def test_only_a_complete_proven_run_exits_zero(self):
        every = list(CASES)
        code, text, auto = self.run_grade(passing=every)
        self.assertEqual((code, self.summary(text)), (0, ("17", "0", "0", "0")))
        self.assertEqual(set(auto.values()), {"pass"})


class ContinuousIntegration(unittest.TestCase):
    def test_ci_runs_only_offline_tests(self):
        wf = (EVALS.parent / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        runs = re.findall(r"^\s*- run: (.*)$", wf, re.M)
        self.assertIn("python3 -m unittest discover evals/tests", runs)
        self.assertEqual(sorted(r for r in runs if "evals" in r), ["python3 -m unittest discover evals/tests"])
        for banned in ("claude", "anthropic", "secrets.", "grade.py grade", "api_key", "api-key"):
            self.assertNotIn(banned, wf.lower(), banned)


class CommandLine(unittest.TestCase):
    def test_grade_writes_automatic_and_manual_files_separately(self):
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "sw-main.md").write_text(golden("sw-main", "good"), encoding="utf-8")
            (out / "rr-main.md").write_text(golden("rr-main", "bad"), encoding="utf-8")
            (out / "rt-standalone.md").write_text(golden("rt-standalone", "good"), encoding="utf-8")
            code = grade.main(["grade", str(out)])
            self.assertEqual(code, 1)  # rr-main fails
            auto = {r["id"]: r for r in json.loads((out / "automatic.json").read_text())}
            self.assertEqual(auto["sw-main"]["status"], "pass")
            self.assertEqual(auto["rr-main"]["status"], "fail")
            self.assertEqual(auto["rt-standalone"]["status"], "unverified")
            manual = json.loads((out / "manual.json").read_text())
            self.assertEqual(set(manual), set(auto))
            self.assertTrue(all(v is None for sheet in manual.values() for v in sheet.values()))
            self.assertNotIn('"score"', (out / "automatic.json").read_text())

    def test_exit_codes_never_report_unverified_as_a_pass(self):
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "rt-standalone.md").write_text(golden("rt-standalone", "good"), encoding="utf-8")
            self.assertEqual(grade.main(["grade", str(out), "--allow-missing"]), 2)  # isolation unproven
            (out / "rt-standalone.meta.json").write_text(json.dumps({"loaded_skills": ["requirements-trace"]}))
            self.assertEqual(grade.main(["grade", str(out), "--allow-missing"]), 0)
            self.assertEqual(grade.main(["grade", str(out)]), 3)  # the other 16 outputs are missing
            (out / "rt-standalone.meta.json").write_text("{not json")
            self.assertEqual(grade.main(["grade", str(out), "--allow-missing"]), 2)  # an unreadable record proves nothing
            (out / "rt-standalone.md").write_text(golden("rt-standalone", "bad"), encoding="utf-8")
            self.assertEqual(grade.main(["grade", str(out), "--allow-missing"]), 1)  # a failure outranks unverified

    def test_a_complete_run_passes_only_with_proof_of_isolation(self):
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            for cid, case in CASES.items():
                (out / f"{cid}.md").write_text(golden(cid, "good"), encoding="utf-8")
                if case["kind"] == "standalone":
                    (out / f"{cid}.meta.json").write_text(json.dumps({"loaded_skills": case["install"]}))
            self.assertEqual(grade.main(["grade", str(out)]), 0)
            (out / "rd-standalone.meta.json").unlink()
            self.assertEqual(grade.main(["grade", str(out)]), 2)

    def test_list_succeeds(self):
        self.assertEqual(grade.main(["list"]), 0)


if __name__ == "__main__":
    unittest.main()
