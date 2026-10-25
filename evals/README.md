# Skill evals (offline)

Behaviour tests for the skills. This first batch covers four skills: `story-writer`, `requirements-review`, `requirements-trace`, `requirements-document`. Nothing here calls an LLM; CI runs only the unit tests of the grader.

## What is in the folder

| Path | Purpose |
|---|---|
| `cases/<skill>/<id>.yml` | One case: prompt, fixtures, automatic checks, manual rubric ids, and which checks the "bad" golden must fail |
| `fixtures/` | Input documents with known content (seeded defects, gaps, controls that are fine) |
| `golden/<id>.good.md`, `<id>.bad.md` | A hand-written answer that must pass, and a plausible one that must fail exactly the listed checks |
| `grade.py` | The grader (stdlib + PyYAML): `list`, `prompt <id>`, `grade <outdir>` |
| `RUBRIC.md` | Manual criteria, scored by a person |
| `tests/test_grade.py` | Unit tests of the grader, cases and goldens |

## Cases: 17

For each skill, three kinds: **main** (full input), **vague** (missing or unclear input), **trap** (the input pushes the skill to break one of its own hard rules). Plus five **standalone** cases, one for each cross-skill pointer fixed in Phase 1: the skill must finish its task, and must not cite a file or skill that is not installed. A pointer that only says "if installed" is not an error.

## Automatic and manual are kept apart

- `grade.py grade OUTDIR` reads `OUTDIR/<case-id>.md` and writes `OUTDIR/automatic.json`. It also creates an empty `OUTDIR/manual.json`, the sheet for the criteria in `RUBRIC.md`.
- A case passes when every automatic check passes. Manual scores never change that status.

## Checks that carry the weight

The checks look at structure and facts, not only at whether a word appears:

- **Seeded defects and gaps** (`rows`): each known defect must appear in a row of its own that names its code and gives a matching reason (one stuffed row counts once); items that are fine (controls) must not be flagged Blocker or Should fix. Findings marked `required: true` must all be found; `min_recall` then applies to all of them. Required = Blocker in `requirements-review` (cannot be built, tested or approved) and the High rows of `requirements-trace/references/coverage-checks.md`; the rest may be missed up to the recall threshold. The reason words are chosen so that quoting the source line does not satisfy them (a unit test enforces it).
- **Where `required` comes from.** `rt-main`: sourced, the four High rows (1 abandoned goal, 2 orphan, 3 story without AC, 9 contradiction) of `skills/requirements-trace/references/coverage-checks.md`; the three optional ones are its Medium rows (5, 8). `rr-main` and `rr-standalone-tracking`: the skill only defines Blocker ("cannot be built/tested/approved without a fix"), so which seeded defect is a Blocker is the author's judgement, not a sourced fact. US-03 (no action, no value, AC cannot be tested), the AC-04.1 / BR-02 contradiction and US-05 (no AC) were taken as Blockers; AC-02.1 and NFR-USA-01 ("cannot be tested" in a weaker sense) and the terminology split were taken as optional. These are severities for these fixtures, confirmed by the owner (2026-10-25); they are not a general rule for other projects, where the same defect may be rated differently.
- **Matrix links** (`links`): the true goal-story links of the fixture must appear together in a matrix row and the false ones must not.
- **No invention** (`ids_subset`, `numbers_from_input`, `link_requires_marker`): codes, numbers and links must come from the input, or be marked proposed.
- **Findings point at the input** (`items_resolve`): every finding cites a code or a quote that exists in the fixture.
- **Report logic** (`verdict`): a report with a Blocker cannot say Ready.
- **Structure and vocabulary** (`sections`, `table_columns`, `column_values`): required sections in order, required table columns, severity and method values from the allowed set.
- **Wording kept** (`verbatim`) and **language** (`language`).
- **Standalone** (`no_missing_resource`): paths that do not exist in the installed skill, paths into a skill that is not installed, and "could not read X" about another skill all fail.

## Running

```bash
python3 evals/grade.py list                      # validate the cases
python3 evals/grade.py prompt sw-main            # the exact prompt, fixtures appended
python3 evals/grade.py grade evals/out/<run>     # grade saved outputs
python3 -m unittest discover evals/tests         # what CI runs (offline)
```

To try a case by hand today: print the prompt, paste it into an agent that has the skill, save the reply as `evals/out/<run>/<case-id>.md`, run `grade`.

## Exit codes of `grade`

By priority, the first that applies:

| Code | Meaning |
|---|---|
| 1 | At least one graded case failed a check (or violated isolation) |
| 3 | No case failed, but an output file is missing, so not all 17 cases were graded |
| 2 | No case failed and nothing is missing, but a standalone case is `unverified` (no proof of which skills were loaded) |
| 0 | All 17 cases were graded and passed, standalone ones with a valid isolation record |

`--allow-missing` is for grading a subset by hand: missing outputs are still listed but ignored for the code, so a subset can end 0, 1 or 2. Exit 0 from a subset says nothing about the cases that were not run. `unverified` and a partial run are never reported as a pass.

## Isolation of standalone cases: what is and is not established

For a standalone case only the named skill may be installed. A temporary folder does **not** guarantee that:

- Claude Code loads personal skills from `~/.claude/skills` in every project, plus project, nested, plugin and `--add-dir` skills (Claude Code skills documentation, checked for this batch).
- The documentation lists no setting that turns off personal skills as a group. Per-skill control exists (`skillOverrides`, `Skill(...)` permission rules).
- `claude --help` says `--bare` skips hooks, plugin sync, CLAUDE.md discovery and OAuth/keychain login (it needs an API key); it does not say whether personal skills are skipped. `--disable-slash-commands` disables all skills.
- Not found in the documentation read: whether the headless `stream-json` init message lists the loaded skills. It has not been tried, because this batch does not run `claude -p`.

So the grader does not assume isolation. A standalone result is **pass** only when `OUTDIR/<case-id>.meta.json` holds `{"loaded_skills": [...]}` from the runner and no other suite skill is in it; with no usable record (missing, unreadable, wrong shape) it is **unverified**; with another suite skill loaded, or without the skill under test in the record, it **fails**. See "Exit codes" below. A live runner must produce that record, or the standalone results stay unverified.

## Limits

- Automatic checks are necessary, not sufficient. A reply can pass them and still be poor; that is what `RUBRIC.md` is for.
- Pattern checks can miss a correct answer worded differently (false failure). The golden cases show one accepted wording each, not the only one; `golden/alternatives/` holds valid answers in other wording and layout, which must also pass. Add one there whenever a valid answer is rejected.
- Codes are matched in the form `US-99` (Unicode hyphens and a trailing letter are caught). `us-99`, `US 99`, `US99` and `US_99` are not recognised as codes, because a case-insensitive match would flag ordinary words such as `step-1`.
- Invented amounts are found as digits, as `3s`, and as number words only before a unit (`five wrong passwords`, `thirty minutes`); `a few` turned into `several` or an amount without a unit is not found. Numbers after `question`, `section`, `item`, `#` are treated as references.
- A one-row answer that covers two defects counts for one of them.
- `ids_all` accepts `US-01 to US-05` as a range. Anything it does not check is left to the manual rubric (for example whether a matrix link is justified when the fixture does not settle it).
- Section and table parsing assumes Markdown headings, `**Label**:` lines and pipe tables. Sub-headings end a section early.
- The verdict is read as the first of "Not ready", "Conditional", "Ready" in the Verdict section.
- Fixtures and expectations were written by the same author as the checks; review them before trusting a score.
- One run per case does not show variation between runs.
- Nothing here tests whether a skill is chosen from a natural prompt (routing), or other hosts than Claude Code.
