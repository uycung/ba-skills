# Skill evals (offline)

Behaviour tests for the skills. This first batch covers four skills: `story-writer`, `requirements-review`, `requirements-trace`, `requirements-document`. `grade.py` and the unit tests call no LLM; CI runs only the unit tests. `run.py` is the live runner: it calls `claude -p`, costs money, and is run by hand, never by CI.

## What is in the folder

| Path | Purpose |
|---|---|
| `cases/<skill>/<id>.yml` | One case: prompt, fixtures, automatic checks, manual rubric ids, and which checks the "bad" golden must fail |
| `fixtures/` | Input documents with known content (seeded defects, gaps, controls that are fine) |
| `golden/<id>.good.md`, `<id>.bad.md` | A hand-written answer that must pass, and a plausible one that must fail exactly the listed checks |
| `grade.py` | The grader (stdlib + PyYAML): `list`, `prompt <id>`, `grade <outdir>` |
| `run.py` | The live runner: `explicit` or `natural` mode, one `claude -p` per case, then `grade` |
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

To try a case by hand: print the prompt, paste it into an agent that has the skill, save the reply as `evals/out/<run>/<case-id>.md`, run `grade`.

### Live run

```bash
python3 evals/run.py explicit evals/out/<run>              # "Use the <skill> skill for this task." + the prompt
python3 evals/run.py natural  evals/out/<run>-natural      # the prompt as written: measures routing only
python3 evals/run.py explicit evals/out/<run> --cases rt-main,sw-main --force
```

Each case runs once in its own temporary folder. The skills are copied to `<tmp>/.claude/skills/`: a standalone case gets only the skills in its `install`, every other case gets all 11. The call is `claude -p --setting-sources project --model claude-sonnet-5-5 --output-format stream-json --verbose --max-budget-usd <cap> --allowedTools Read,Skill --disallowedTools Bash,Write,Edit,WebFetch,WebSearch,Agent --no-session-persistence`, with the prompt on stdin. Per case it writes `<id>.md` (the reply), `<id>.jsonl` (the raw stream) and `<id>.meta.json`:

| `meta.json` field | Source |
|---|---|
| `loaded_skills` | `skills` of the stream's `init` message (this is the isolation record that standalone cases need) |
| `skill_invoked` | `Skill` tool calls in the stream |
| `model`, `cost_usd`, `turns`, `permission_denials` | `init` and `result` messages |
| `error` | no result, a non-success result, an empty reply, a timeout; `null` otherwise |

Limits of spend: `--case-budget` (default 1.5 USD) per case, `--total-budget` (default 8) per run, and the run stops after `--max-runner-errors` (default 2) errors in a row. An interrupted run is repeated with the same command: cases that already have an output without an error are skipped.

In `natural` mode a failing case says nothing about the skill: the model may simply not have chosen it. Read `skill_invoked` first.

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
- Observed with Claude Code 2.1.310: the `init` message of `stream-json` lists the skills loaded (suite skills and built-in ones), and with `--setting-sources project` personal skills from `~/.claude/skills` are not in that list. `run.py` stores that list as `loaded_skills`.

So the grader does not assume isolation. A standalone result is **pass** only when `OUTDIR/<case-id>.meta.json` holds `{"loaded_skills": [...]}` from the runner and no other suite skill is in it; with no usable record (missing, unreadable, wrong shape) it is **unverified**; with another suite skill loaded, or without the skill under test in the record, it **fails**. See "Exit codes" below. A live runner must produce that record, or the standalone results stay unverified.

## Limits

- Automatic checks are necessary, not sufficient. A reply can pass them and still be poor; that is what `RUBRIC.md` is for.
- Pattern checks can miss a correct answer worded differently (false failure). The golden cases show one accepted wording each, not the only one; `golden/alternatives/` holds valid answers in other wording and layout, which must also pass. Add one there whenever a valid answer is rejected.
- Codes are matched in the form `US-99` (Unicode hyphens and a trailing letter are caught). `us-99`, `US 99`, `US99` and `US_99` are not recognised as codes, because a case-insensitive match would flag ordinary words such as `step-1`.
- Invented amounts are found as digits, as `3s`, and as number words only before a unit (`five wrong passwords`, `thirty minutes`); `a few` turned into `several` or an amount without a unit is not found. Numbers after `question`, `section`, `item`, `#` are treated as references.
- A one-row answer that covers two defects counts for one of them.
- `ids_all` accepts `US-01 to US-05` as a range. Anything it does not check is left to the manual rubric (for example whether a matrix link is justified when the fixture does not settle it).
- Section and table parsing assumes Markdown headings, `**Label**:` lines and pipe tables. A heading of the same or a higher level ends a section; a deeper heading or a bold label (`**High**`) inside it does not, and is still found by its own name. Heading numbers (`3.`, `11.2`) are ignored. The rest of a heading after the section name counts as text of the section (`## Verdict: Not ready`). `Open questions` is accepted for `Questions needing an answer`. Pattern checks see the text without `**`, `__`, `*`, `_` emphasis.
- Invented amounts: list numbers (`1.`, `2.3`), the first column of a table that only counts rows, labels such as `F2`, `Q4`, `A1`, and dates or clock times inside a Given/When/Then line (`10 Nov`, `09:00`, `00 minutes`) are not counted. The same date or time in any other line is. `see 11`, `N-1`, `counter to 0` and `p95` are still counted.
- Invented codes: a code that is offered as an example (`such as AES-256`, `e.g. UTF-8`) is not counted unless its prefix is a requirement prefix (`US`, `TC`, `GOAL`, ... or one used in the input): `for example TC-01` is still a made-up test case.
- The verdict is read as the first of "Not ready", "Conditional", "Ready" in the Verdict section.
- Fixtures and expectations were written by the same author as the checks; review them before trusting a score.
- One run per case does not show variation between runs.
- Nothing here tests whether a skill is chosen from a natural prompt (routing), or other hosts than Claude Code.
