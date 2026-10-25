# UAT and the acceptance package

## Basis
- Acceptance criteria are the minimum conditions for a solution to be worth deploying, usually assessed as pass/fail; they are often verified by user acceptance testing (BABOK 10.1). Acceptance criteria can be written as minimum performance levels and maximum costs in contracts and UAT.
- Criteria are based on value attributes so that they stay relevant to stakeholder needs; the definition of those attributes must be agreed by all stakeholders (10.1).
- In agile, a BDD scenario acts as the acceptance criterion for a story (Agile Extension 7.2); a "Three Amigos" session between PO, tester and dev clarifies before work starts.
- ISTQB CTFL v4.0.1, 2.2.1: acceptance testing focuses on validation and on demonstrating readiness for deployment, ideally performed by the intended users. The main forms are **UAT**, **operational**, **contractual**, **regulatory**, **alpha** and **beta**. When planning, ask explicitly which form this package is; contractual and regulatory acceptance usually have criteria set by the contract/regulation, not proposed by the skill.
- ISTQB 5.1.3: entry criteria are the preconditions for starting an activity, exit criteria are what must be achieved to consider it complete; both should be defined for each test level. Example exit criteria given by ISTQB include measures of thoroughness (coverage, number of unresolved defects) and yes/no criteria. Running out of time or budget can also be an exit criterion if the stakeholders have reviewed and accepted the risk. In agile: Definition of Done (exit criteria) and Definition of Ready (entry criteria).
- **The specific items in the UAT package below are conventions and proposals of this skill, not BABOK or ISTQB.**

## How QA tests differ from UAT
| | QA tests | UAT |
|---|---|---|
| Performed by | QA / dev | Business users, stakeholder representatives |
| Language | Can be technical | Business language |
| Coverage | Each requirement, boundary cases, negative cases | End-to-end business scenarios that carry value |
| Question | Does it run to spec? | Is it usable for real work? |

## UAT package (default output in mode C)
1. **Scope**: which requirements/stories, the environment, what is out of scope.
2. **Business scenarios**: each scenario is a real piece of work a user does end to end ("Receptionist books an appointment for a regular customer and sends a reminder"), joining several stories; with the performing role, sample data and the expected result according to the AC.
3. **Participants and roles**: who runs, who observes, who decides acceptance (per `requirements-stakeholders` / RACI: exactly one Accountable).
4. **Data and environment**: fake data, accounts per role, the starting state to set up.
5. **Entry criteria** (proposal): the required stories have passed QA tests; no known blocker defects remain; environment and data are ready; users have been briefed.
6. **Exit criteria** (proposal, to be fixed by the sponsor/PO): minimum share of scenarios passed, no blocker defects remaining, remaining defects have a handling plan and an owner. **Never invent numbers**; write "to be decided".
7. **Recording**: each scenario has a result of Pass/Fail/Blocked, evidence, notes, who recorded it, and the date.
8. **Acceptance decision**: who signs, under what conditions; conditional acceptance states the defects accepted together with a deadline to resolve them. Without full consensus, manage the residual risk (in the spirit of BABOK 5.5).

## Writing UAT scenarios
- The title is a business task, not a screen name.
- Steps are at the level of business actions; the expected result is observable by the user.
- Each scenario lists the stories/ACs it proves (for traceability).
- Leave a "Comments on usability" cell for qualitative criteria; do not turn qualitative criteria into pass/fail unless the AC says so.

## Common risks (raise with the user when planning)
- UAT is used as system testing because QA was not sufficient: use the entry criteria to block it.
- Business users have no time: schedule early and put it in the stakeholder plan.
- Requirements change after the UAT is written: use the impact analysis of `requirements-trace` to update the scenarios.
