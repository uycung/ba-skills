# Requirements architecture, approval, review (BABOK 7.4 pp. 148–151; 5.5 pp. 95–97; 5.4 pp. 93–94; 10.37 pp. 326–329; paraphrased)

## 1. Traceability cannot prove coherence (7.4.2)
Traceability shows that each requirement links back to a goal; it does **not prove** that the set of requirements forms a working solution. The requirements architecture is the structure of all the requirements so that they support one another. The report of this skill must therefore say: "sufficient traceability coverage" ≠ "the requirement set is coherent".
- Each requirement is **stated exactly once** in the architecture (7.4.3). Duplication is a defect to be merged.
- **Viewpoint** (a representation convention for a group of stakeholders) and **view** (the actual requirements under that viewpoint). Example viewpoints: process, data, user interaction, audit/security, business model. No single viewpoint is enough; cramming too much into one viewpoint makes it messy.
- Completeness: nothing missing, nothing contradictory, including dependencies that could prevent the goal from being reached. Repeating elicitation/analysis helps expose gaps.
- **The BA information architecture** (which kinds of information link to which: requirements, designs, models, elicitation results) should be defined **before** building a tool/repository.

## 2. Quality criteria for each link (7.4.4.4)
| Criterion | Ask |
|---|---|
| Defined | Is there a link, and is the link type recorded? |
| Necessary | Is the link needed to understand the whole? (do not link just to look complete) |
| Correct | Do the two items really have the relationship recorded? |
| Unambiguous | Are there no two contradictory links for the same pair of items? |
| Consistent | Do they use the same standard description set of the viewpoint? |
Use as additional check 13 in `coverage-checks.md`.

## 3. Assessing a requirement change (5.4.4)
In the impact analysis, state the five BABOK factors explicitly: **benefit**, **cost** (including rework and opportunity cost: features that must be sacrificed), **impact** (number of customers/processes affected), **schedule** (existing delivery commitments), **urgency** (including regulatory and safety reasons). The outcome is one of: approve, reject, defer, decided by the person with authority under the governance process; record it and notify all stakeholders. Always consider legal/regulatory information and the solution scope. The skill only **prepares the facts**; it does not decide.

## 4. Approval (5.5.4)
- Approval applies only to requirements that have been **verified for quality** (an input of 5.5). Do not send drafts for signature.
- The form depends on the approach: predictive usually approves at the end of a phase or at a change control meeting; adaptive usually approves just before building starts.
- Know who has the authority to approve/veto and who only has influence. Seek consensus before asking for approval; absolute consensus is not required, but where consensus is missing **record a risk**.
- Record the approval decision (who, when, which version) and notify the status. Suggested columns for the matrix: Approval status | Approver | Date | Version.
- An approved requirement is a baselined product; any later change must go through change assessment.

## 5. Review (10.37)
A review targets the **work product**, not the people. Decide beforehand: the objective (find defects, check compliance with a standard, confirm completeness and correctness, reach consensus, solve a problem, educate, measure quality), the technique, and the participants.
| Technique | Form | When to use |
|---|---|---|
| Inspection | Formal: overview, individual examination, logging defects, consolidation, tracking fixes | Critical work products, defect-finding objective |
| Formal walkthrough | Formal: individual examination + group consolidation | Peers or stakeholders |
| Single issue review | Formal: one issue or one standard | Resolving a specific point |
| Informal walkthrough | BA presents a draft and asks for comments | A work in progress |
| Desk check | One outside person reads and gives feedback | Fast, low effort |
| Pass around | Several people look in turn or on a shared copy | Many people, different times |
| Ad hoc | Ask a colleague to take a look | Very light |
Roles: Author (answers, fixes), Reviewer, Facilitator (neutral, preferably not the author), Scribe (records defects, opinions, open questions). If senior people take part, the facilitator watches that others are not discouraged from speaking honestly.
Limits: a rigorous review costs effort, so reserve it for critical work products; light reviews give less assurance; feedback by email struggles to resolve conflicts.
