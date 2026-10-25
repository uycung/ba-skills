---
name: requirements-prioritize
description: "Help a BA prioritize requirements/stories on evidence: choose criteria, score with reasons, handle stakeholder conflicts, propose an order and release slices; use when ranking a backlog, fixing an MVP, or re-prioritizing after a change."
---

# Requirements Prioritize

Framework from BABOK v3 section 5.3 (Prioritize Requirements) and 10.33 (Prioritization). Respond in the user's language. The skill **proposes and explains**; the user and the stakeholders decide.

## Principles
1. **Prioritization is a judgment of relative value**; each stakeholder may value different things. Bring conflicts into the open, do not hide them (BABOK 5.3.4.2).
2. **Agree the criteria first, score afterwards.** The basis for prioritization is agreed by the relevant stakeholders (5.3.4.1). If the user tells you to skip the criteria or not to ask about them, still state the criteria you used as proposals, mark the ranking as provisional until the stakeholders agree them, and say who agrees.
3. **Never invent numbers.** Every score carries a reason/evidence; cost comes from the delivery team; if it is not available, write "not estimated".
4. **Legal/policy constraints come before other wishes**; do not give a "weight" to something mandatory (BABOK notes that regulatory compliance can outrank stakeholder benefit).
5. **Priorities change over time**: at first at a high level of abstraction, later in more detail; the technical team may reorder by implementation sequence, and stakeholders adjust again once they know the cost (5.3.4.3).
6. Watch for bias: stakeholders may (deliberately or not) report priorities to influence the result; the solution team may inflate difficulty (10.33.4.2).

## Process
1. Collect the list of items to rank (with codes) and the context: objective, phase, constraints (deadline, budget, regulation).
2. **Choose and agree criteria** from `references/criteria.md`; do not use more than 4–5 criteria at once.
3. **Separate the mandatory group** (legal compliance, contract, mandatory technical dependencies) from the group that needs scoring.
4. **Score** using `templates/prioritization-table.md`; each score carries a reason and the source of the information. Mark a score, an estimate or a criterion that the stakeholders have not confirmed `[Assumption]` (`[Inferred]` when it is drawn from what was said).
5. **Check dependencies** (use the depends relationship from `requirements-trace`): an item with high priority that depends on a low one needs adjusting.
6. **Propose an order and slices** (for example releases 1/2/3, or by a fixed time box/budget, BABOK 10.33.3.3), and state the **trade-offs**: what is gained, what is lost.
7. State **unresolved conflicts** and the questions that need a decision, and who decides.
8. Record the **date and basis** of this prioritization so it can be reassessed when the context changes.

## Reference files
- `references/criteria.md`: criteria, methods, biases, multi-phase backlog, factors for assessing a change.
- `templates/prioritization-table.md`: table and report template.

## Conventions

- Provenance of project information: `[Stated]` the user or a document says it outright (name the source); `[Inferred]` drawn from what was said; `[Assumption]` no basis yet, to be confirmed. Use a label only where the reader needs to know which one it is.
- IDs: use the project's own scheme if it has one. Otherwise default to `GOAL-xx`, `FR-xx`, `US-xx`, `AC-xx.y`, `BR-xx`, `NFR-<characteristic>-xx`, `TC-xx`, `UAT-xx`, `SH-xx`.
- An ID never changes and is never reused. An ID you choose yourself is marked "proposed". Do not create an ID for something the user has not supplied; a `TC-` code goes only to a test that exists or that `requirements-testcases` writes.
- In `nfr-writer`, the evidence types (a), (b), (c) say where a threshold comes from; they are not provenance labels.
