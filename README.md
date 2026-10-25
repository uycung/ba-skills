# ba-skills

Eleven [Agent Skills](https://agentskills.io) for business analyst work: stakeholder analysis, business case, requirements elicitation, modelling, user stories, NFRs, prioritisation, traceability, review, test cases/UAT, and assembling BRD/PRD/SRS documents.

The skills follow the open Agent Skills format (a folder with a `SKILL.md`), so they work in any agent that supports it, not only Claude. They are written in English and reply in the language of the user. Content is grounded in BABOK v3, the Agile Extension v2, ISO/IEC 25010:2023, ISTQB CTFL v4.0.1 and ISO/IEC/IEEE 29148:2018, paraphrased with section numbers cited (no source text is included). A guide in Vietnamese is in [docs/usage-guide.vi.md](docs/usage-guide.vi.md); the original Vietnamese skills are kept at tag [`v1.0.0-vi`](https://github.com/uycung/ba-skills/tree/v1.0.0-vi).

Full usage guide: [docs/usage-guide.md](docs/usage-guide.md).

## The 11 skills

| Skill | Use when | Input | Output |
| --- | --- | --- | --- |
| [`requirements-stakeholders`](skills/requirements-stakeholders) | Start of a project or elicitation round; who to meet, who decides | Project description, org chart, meeting notes | Stakeholder list, influence matrix, onion map, RACI, personas, engagement plan |
| [`business-case-strategy`](skills/business-case-strategy) | Justify or choose a direction for change before detailed requirements | Problem description, cost and benefit data | Current/future state, gap, risk, strategy, business case, ROI/NPV/IRR, SWOT, KPIs |
| [`requirements-elicitation`](skills/requirements-elicitation) | Before or after a stakeholder meeting | Meeting goal or notes | Elicitation plan, questions, sourced (unconfirmed) results, list to confirm |
| [`requirements-modelling`](skills/requirements-modelling) | A text description is not clear enough | Processes, rules, data, roles | Process, state and data models, decision tables, use cases, scope, interfaces, permission matrix |
| [`story-writer`](skills/story-writer) | Turn a raw idea into a clear requirement | Ideas, notes, raw requirements | Stories, acceptance criteria, use cases, business-rule tables; or a review of existing stories |
| [`nfr-writer`](skills/nfr-writer) | "Fast, secure, easy to use" must become measurable | Product type, existing spec | Measurable NFRs over the 9 ISO 25010:2023 characteristics, trade-offs, list to confirm |
| [`requirements-prioritize`](skills/requirements-prioritize) | Rank a backlog, fix an MVP, re-rank after a change | Requirements with IDs and constraints | Scored table with reasons, order, release slices, open conflicts |
| [`requirements-trace`](skills/requirements-trace) | Find spec gaps, analyse the impact of a change | PRD, stories, NFRs, tests | Traceability matrix, gaps, contradictions, impact analysis |
| [`requirements-review`](skills/requirements-review) | Before approval or handover to dev/testers | Any requirements document | Findings with severity and a ready-to-approve verdict |
| [`requirements-testcases`](skills/requirements-testcases) | Turn requirements into tests, build UAT | Stories, AC, rules, decision tables, state models, NFRs | Traceable test cases, coverage matrix, UAT package, regression selection |
| [`requirements-document`](skills/requirements-document) | Package requirements for approval, handover or contract | Outputs of the skills above | BRD, PRD or SRS, consistency check, list of gaps |

## Recommended order

A suggestion, not a rule:

1. Context: `requirements-stakeholders`, `business-case-strategy`
2. Elicitation: `requirements-elicitation`
3. Write and model: `requirements-modelling`, `story-writer`, `nfr-writer`
4. Decide: `requirements-prioritize`
5. Control: `requirements-trace`, `requirements-review`
6. Verify: `requirements-testcases`
7. Package: `requirements-document`

## Install

**Install the whole set.** The skills reference each other by name (for example `requirements-trace` and `story-writer`), so installing a single skill leaves dangling references.

### With `npx skills`

```bash
npx skills add uycung/ba-skills --list   # shows the 11 skills
npx skills add uycung/ba-skills          # installs them
```

### Manual copy

```bash
git clone https://github.com/uycung/ba-skills.git
cd ba-skills
mkdir -p ~/.claude/skills
cp -R skills/* ~/.claude/skills/
```

Use `.claude/skills/` inside a project to scope them to that project, or the skills directory of another agent that supports the Agent Skills format. Start a new session so the agent discovers them.

### claude.ai (zip upload)

Each skill is uploaded as a zip with one top-level folder named like the skill:

```bash
cd skills
for d in */; do zip -rq "${d%/}.zip" "${d%/}" -x '*.DS_Store'; done
```

Then upload each zip in the Skills section of claude.ai settings (a plan with Skills support is required). The author has not tested this against the current claude.ai interface.

### Optional: the author's `install-global-skills`

The author keeps one physical copy of every skill in `~/.agents/skills/<name>/` and lets Claude Code (`~/.claude/skills`) and Antigravity (`~/.gemini/config/skills`) read it through directory symlinks, using a personal skill called `install-global-skills`. That skill is not part of this repo; you can reproduce the layout with `cp -R skills/* ~/.agents/skills/` and the symlinks.

### Update

```bash
git pull
```

then repeat the install you used, or run `npx skills add uycung/ba-skills` again. `cp -R` overwrites files but does not delete files removed upstream; delete the old skill folders first if you want a clean copy (back them up if you edited them).

### Quick check

`skills/business-case-strategy/scripts/fin.py` takes a JSON file path. With

```json
{"discount_rate":0.1,"years":[{"year":0,"benefits":0,"costs":100},{"year":1,"benefits":40,"costs":10},{"year":2,"benefits":60,"costs":10},{"year":3,"benefits":80,"costs":10}]}
```

the correct result is NPV ≈ 21.187, ROI ≈ 0.3846, IRR ≈ 0.2013, payback ≈ 2.2857 years.

## Sources and how far each was verified

| Source | Verification |
| --- | --- |
| BABOK v3, Agile Extension v2 | Read from the PDF, paraphrased, section numbers cited; some sections not read |
| ISO/IEC 25010:2023 | Characteristic names match the 2023 edition; the "meaning" wording is the skill's own, not compared with the official definitions |
| ISTQB CTFL v4.0.1 | Compared with the PDF |
| ISO/IEC/IEEE 29148:2018 | Clauses 5.2, 6.5.2.2 and 9.2 to 9.6 compared against the standard |
| Vietnam law, EU AI Act | See the warning below |

This repo contains no PDFs or original text of these sources. More detail: [docs/usage-guide.md](docs/usage-guide.md#5-sources-and-how-far-each-was-verified).

> **Legal notice.** [`skills/nfr-writer/references/legal-vn.md`](skills/nfr-writer/references/legal-vn.md) is reference information, **not legal advice**. It was last verified on 24/10/2026 and contains items marked ⚠️ that are **unverified** against the original text (for example Decree 330/2026, Decree 142/2026, the status of Decree 53/2022). Legal counsel must confirm before it goes into a contract or spec.

## Known limits

- The suite has not yet been run on a real PRD or meeting notes.
- The skills prepare input for the person with authority to confirm; they do not replace QA, legal counsel or the decision maker.
- They do not fill in numbers (NFR thresholds, UAT criteria, targets); missing values are written as "to be confirmed".
- Some BABOK and Agile Extension sections have not been read (list in the usage guide).

## License

[MIT](LICENSE).
