# Checks when assembling

The list belongs to the skill, based on: requirements quality (7.2.4), link quality criteria (7.4: defined, necessary, correct, unambiguous, consistent), and approval (5.5).

## Consistency
1. **IDs**: no duplicates, no wrong jumps, every reference `AC-xx`, `BR-xx`, `NFR-xx` exists in the document.
2. **Terms**: one concept one name; the glossary matches everywhere.
3. **Scope**: goals, in/out scope and requirements do not contradict; no requirement lies outside the stated scope.
4. **Figures and thresholds**: the same number everywhere (for example the cancellation deadline, the response time).
5. **Priority**: the same scale as `requirements-prioritize`; no contradiction with the release plan.
6. **Roles**: role names match the stakeholder list and the permission matrix.
7. **States**: state names in stories match the state model.
8. **Rules**: each rule appears once in the BR table; stories/use cases refer to it.
9. **Data**: attributes in stories match the data dictionary.

## Completeness by type
- **BRD**: has the need, measurable (SMART) objectives, scope, stakeholders, success criteria, constraints, risks, high-level transition requirements.
- **PRD**: problem, users (research-based or labelled as a hypothesis), goals and indicators, scope, requirements with AC, main NFRs, release, risks, open questions.
- **SRS**: every FR has a verifiable AC; every NFR is measurable; interfaces; data; rules; transition.
Every type: assumptions, constraints, dependencies, open questions; an approval section; change history.

## Traceability
- Every solution requirement traces to at least one business requirement or goal; every goal has requirements pointing to it.
- No orphan requirements, no uncovered goals (see `requirements-trace`).
- Every AC/NFR has a test or is marked "no test yet" (`requirements-testcases`).

## Status, version, baseline
- Every item has a status: Draft / Reviewed / Approved / Awaiting clarification.
- Version number and date; change history: who, what, why.
- **Baseline**: the point at which a set of requirements is frozen so work can continue; later changes go through impact assessment (5.4: benefit, cost, impact, schedule, urgency). The BABOK glossary says a requirements package can be the baseline of a set of requirements.
- Never put the status "Approved" without confirmation from the approver.

## Approval (5.5)
The input is verified requirements. Approval varies: predictive approves at the end of a phase or at a change control meeting; adaptive approves just before building starts. Full agreement is not needed; where there is no consensus the risk must be managed. The approval section of the document records: who (role, the Accountable person per the RACI), the scope of approval, the date, accompanying conditions, objections. Do not fill it in on their behalf.

## Signs of a document that is "thick but empty"
- Every section has words but no source.
- Generic statements about quality ("the system must be stable") with no measure.
- The same idea repeated in several sections.
- An empty assumptions section.
