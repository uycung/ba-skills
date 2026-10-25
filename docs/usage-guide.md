# The 11 BA skills: usage guide

Vietnamese version: [usage-guide.vi.md](usage-guide.vi.md) (kept from release `v1.0.0-vi`; it describes the Vietnamese skills).

The suite helps a business analyst work with an AI agent from project start to handover: stakeholder analysis, business case, elicitation, stories and NFRs, modelling, prioritisation, traceability, review, test cases/UAT, and assembling BRD/PRD/SRS documents. Last updated 25/10/2026.

## 1. Principles shared by the whole suite

- **Sourced, not invented.** Content follows BABOK v3 and the Agile Extension v2; tests follow ISTQB CTFL v4.0.1; NFRs follow ISO/IEC 25010:2023; requirement quality adds ISO/IEC/IEEE 29148:2018. Each skill says what comes from which source and what is only its own convention.
- **No made-up numbers.** NFR thresholds, UAT exit criteria and target metrics come from the user or the product owner. If missing, the skill writes "to be confirmed".
- **Every output ends with** assumptions, open questions, and what is not enough to continue, so you can see where it is unsure.
- **Requirements point back to their source.** Each item has an ID and traces to a goal or to who raised it.
- **Vietnam legal content is reference only.** Lines marked ⚠️ are not confirmed from the original text; legal counsel must confirm.
- Replies follow the user's language.

## 2. The 11 skills

| Skill | Use when | Input | Output |
| --- | --- | --- | --- |
| `requirements-stakeholders` | Start of a project or elicitation round; you need to know who to meet and who decides | Project description, org chart, meeting notes | Stakeholder list, influence matrix, onion map, RACI, personas, engagement plan |
| `business-case-strategy` | You must justify or choose a direction for change before detailed requirements | Problem description, cost and benefit data | Current and future state, gap, risk, strategy, business case, ROI/NPV/IRR, SWOT, KPIs |
| `requirements-elicitation` | Before or after a stakeholder meeting | Meeting goal or meeting notes | Elicitation plan, question set, sourced (unconfirmed) results and a list to confirm |
| `requirements-modelling` | A text description is not clear enough | Processes, rules, data, roles | Process, state and data models, decision tables, use cases, scope, interfaces, permission matrix |
| `story-writer` | Turn a raw idea into a clear requirement | Ideas, notes, raw requirements | Stories, acceptance criteria, use cases, business-rule tables; or a review of existing stories |
| `nfr-writer` | "Fast, secure, easy to use" must become measurable | Product type, existing spec | Measurable NFRs across the 9 ISO 25010:2023 characteristics, trade-offs, a list to confirm |
| `requirements-prioritize` | Rank a backlog, fix an MVP, re-rank after a change | Requirement list with IDs and constraints | Scored table with reasons, order, release slices, unresolved conflicts |
| `requirements-trace` | Check a spec for gaps, analyse the impact of a change | PRD, stories, NFRs, tests | Traceability matrix, gaps, contradictions, impact analysis |
| `requirements-review` | Before asking for approval or handing to dev/testers | Any requirements document | Findings report with severity and a ready-to-approve verdict; or a review-session plan |
| `requirements-testcases` | Turn requirements into a test set, build UAT | Stories, AC, rules, decision tables, state models, NFRs | Traceable test cases, coverage matrix, UAT package, regression selection after a change |
| `requirements-document` | You need a package for approval, handover or contract signing | Outputs of the skills above | BRD, PRD or SRS, consistency check, list of what is missing |

## 3. Suggested order

A suggestion, not a rule. Skip a step if you already have its output.

1. **Context:** `requirements-stakeholders`, then `business-case-strategy`.
2. **Elicitation:** `requirements-elicitation` (plan first, process notes after each meeting).
3. **Write and model:** `requirements-modelling`, `story-writer`, `nfr-writer`.
4. **Decide:** `requirements-prioritize`.
5. **Control:** `requirements-trace`, `requirements-review`.
6. **Verify:** `requirements-testcases`.
7. **Package:** `requirements-document`.

When a requirement changes: `requirements-trace` (impact), `requirements-testcases` (pick regression tests), `requirements-review` (re-check after the fix).

## 4. Example prompts

| Goal | Example |
| --- | --- |
| Stakeholder analysis | "List the stakeholders and a RACI for a spa booking project; here is the description..." |
| Business case | "Build a business case for automating appointment reminders; costs and benefits as in this table..." |
| Meeting notes | "Here are notes from the meeting with the receptionist; separate what was said, what is inferred, assumptions, and a list to confirm." |
| Modelling | "Build a decision table for the cancellation rule from this description." |
| Story | "Write the story and AC for rescheduling an appointment; ask me if information is missing." |
| NFR | "Does this spec have enough NFRs? It is an internal web app with personal data." |
| Priority | "Rank these 20 stories into 3 release slices; the constraint is end of quarter." |
| Traceability | "Build the traceability matrix and show the gaps; if story S-07 is dropped, what is affected?" |
| Review | "Review this PRD and tell me if it is ready for approval." |
| Tests | "Generate test cases and a coverage matrix from these AC; boundary values with 3 values." |
| UAT | "Build a UAT package for the end-to-end booking flow." |
| Document | "Assemble a BRD from these outputs and list what is still missing." |

## 5. Sources and how far each was verified

| Source | Used for | Verification |
| --- | --- | --- |
| BABOK v3 | Most skills (elicitation, analysis, traceability, review...) | Read from the PDF and paraphrased; section numbers cited; some sections not read (see section 6) |
| Agile Extension v2 | Stories, BDD, personas, backlog | Read from the PDF and paraphrased |
| ISO/IEC 25010:2023 | NFRs | Characteristic names match the 2023 edition; the "meaning" column is the skill's own wording, not compared with the official definitions |
| ISTQB CTFL v4.0.1 | Test design: equivalence partitioning, boundary values, decision tables, state transition, UAT, ATDD | Compared with the PDF |
| ISO/IEC/IEEE 29148:2018 | Requirement quality characteristics, keywords, attributes, verification methods, BRS/StRS/SRS/SyRS content | Clauses 5.2, 6.5.2.2 and 9.2 to 9.6 compared against the standard |
| Vietnam law and EU AI Act | Legal NFRs (`skills/nfr-writer/references/legal-vn.md`) | Last verified 24/10/2026; partly read from original texts, partly from secondary sources only (marked ⚠️) |

This repository contains no PDFs or original text of these sources; the skills paraphrase and cite section numbers only.

## 6. Known limits and open items

- **Legal (⚠️):** the full text of Decree 330/2026 and Decree 142/2026 has not been read; the high-risk AI list (Decision 33/2026/QĐ-TTg) exists only as an excerpt; the status of Decree 53/2022, Decree 85/2016 and Circular 12/2022 is unconfirmed. The Decree 330 penalty bands come from secondary sources, so no figure is written into NFRs. Legal counsel must confirm before anything goes into a contract or spec.
- **BABOK / Agile Extension:** some sections have not been read (for example BABOK 10.3, 10.4, 10.6, 10.8, 10.49, 8.3, 8.4, chapters 3.1 and 3.3 to 3.5; Agile Extension chapters 1 to 6, 7.8 to 7.17 and 7.22 to 7.24).
- **Not yet run on a real document.** Try the whole suite on a real PRD or meeting notes and record where a skill does poorly.
- The skills do not replace QA, legal counsel or the decision maker: they prepare input for the person with authority to confirm.

Install and update: see the [README](../README.md#install).
