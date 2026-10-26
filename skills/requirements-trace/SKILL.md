---
name: requirements-trace
description: "Build a traceability matrix and check coverage: links between goals, FRs, user stories, acceptance criteria, business rules, NFRs and tests; find coverage gaps (a goal with no story, a story with no goal or AC, a rule or NFR nobody uses, missing tests), contradictions, and the impact of a change. Use when asked to link, trace, map or check coverage, or to list the gaps of a spec, even if the stories have no codes, or the user also asks to add links or test cases (it records only links and tests that exist). Not for judging how well items are worded: that is requirements-review."
---

# Requirements Trace

Goal: link requirements to one another so you can see **what is not covered** and **what is affected if this changes**. Respond in the user's language. Works together with the `story-writer` skill (writes FRs/stories/AC) and `nfr-writer` (writes NFRs).

## Principles
1. **Link only when the link has value.** Traceability effort grows sharply with the number of requirements and the level of formality (BABOK 5.1.4.1). **Ask the user which level they need before you build anything**: light (goal ↔ story ↔ AC), medium (add NFRs and business rules), full (add design and tests). If the user did not say, ask in your reply and name the three levels; do not assume one, and do not hold back what was asked: give the catalogue, a matrix at the light level marked provisional, and the gap list (Gaps, Contradictions, To confirm) in that same reply.
2. **Never invent links.** Record only links that have a basis in the documents the user supplied; inferred links are marked "proposed, needs confirmation".
   **Never create test cases or `TC-` codes.** Tests are linked only if the user supplied them. If none exist, leave the TC cell "none", list "no tests" under the gaps, and point to `requirements-testcases`, even when the user asks you to fill every cell.
3. **Every item has a stable code** that does not change when the content is edited. Default convention: `GOAL-xx`, `FR-xx`, `US-xx` (or an epic-based code such as `ORD-12`), `AC-xx.y`, `BR-xx` (business rule), `NFR-<characteristic>-xx`, and `TC-xx` for tests that the user supplied. If the team already has a convention, use it.
4. Use the correct relationship types (see `references/relationships.md`).

## Process
1. Collect the input documents (PRD, story list, NFR table...). If codes are missing on goals, stories, AC, rules or NFRs, assign proposed codes and say so (never for tests).
2. Take the traceability level the user stated; if they stated none, ask (light/medium/full) in the reply and meanwhile build the provisional light-level matrix and the gap list; never end with the question alone.
3. Build the catalogue of items and links using `templates/trace-matrix.md`.
4. Run the coverage checks (`references/coverage-checks.md`) and list the gaps by severity.
5. If the user states a change, do an impact analysis: which items are affected directly/indirectly, what must be edited, who needs to re-approve.
6. End with: **Gaps**, **Contradictions**, **To confirm**, and the proposed next step.

## A limit to state plainly
Traceability shows that each requirement links back to a goal; it does **not** show that the set of requirements is coherent (BABOK 7.4.2). If the user needs that checked, use viewpoints/views and the 5 link criteria.

## Attributes each requirement should have
Source (who/which document asked for it), priority, complexity, status (including approved: by whom, when), version. Attributes can change even when the requirement does not (BABOK 5.2.4.2).
ISO/IEC/IEEE 29148:2018, 5.2.8.2 (the standard itself was read) gives these example attributes: a unique identifier (never changed and never reused even if the requirement is deleted), version, owner, stakeholder priority (scale 1 to 5 or High/Medium/Low), risk, rationale, difficulty, type. That list is only examples, and status, source and traceability links are not among them. Elsewhere the standard does require them in practice: in 6.4.3 it says both the source and the rationale of each requirement need to be captured, and the attribute list it quotes there from ISO/IEC/IEEE 12207 includes rationale, priority, traceability to system elements, test cases, methods of verification, inclusion in approved baselines and evaluated risk. Clause 6.5.2.2 recommends attaching the **verification method** when the requirement is created, with four values: inspection, analysis, demonstration, test; more on 29148 in the `requirements-review` skill, if installed. The rule "identifier never changed, never reused" should be applied to the IDs in the matrix.
29148 (6.4.3) gives tracing three purposes: coverage analysis (every stakeholder requirement is met, every low-level requirement is justified), compliance analysis (documenting that stakeholder requirements are satisfied) and impact analysis when requirements change. It asks for bi-directional traceability: downward to lower-level requirements, architecture, system elements and verification/test entities, and upward to parent requirements and the stakeholders that motivated them.

## Reference files
- `references/relationships.md`: relationship types and how to record them.
- `references/coverage-checks.md`: coverage checks, impact analysis.
- `references/architecture-approval-review.md`: requirements architecture, link quality, change assessment, approval, review (BABOK 7.4, 5.4, 5.5, 10.37).
- `templates/trace-matrix.md`: matrix template and gap report.

## Conventions

- Provenance of project information: `[Stated]` the user or a document says it outright (name the source); `[Inferred]` drawn from what was said; `[Assumption]` no basis yet, to be confirmed. Use a label only where the reader needs to know which one it is.
- IDs: use the project's own scheme if it has one. Otherwise default to `GOAL-xx`, `FR-xx`, `US-xx`, `AC-xx.y`, `BR-xx`, `NFR-<characteristic>-xx`, `TC-xx`, `UAT-xx`, `SH-xx`.
- An ID never changes and is never reused. An ID you choose yourself is marked "proposed". Do not create an ID for something the user has not supplied; a `TC-` code goes only to a test that exists or that `requirements-testcases` writes.
- In `nfr-writer`, the evidence types (a), (b), (c) say where a threshold comes from; they are not provenance labels.
