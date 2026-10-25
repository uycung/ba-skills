# Verify and Validate (BABOK 7.2, 7.3, 5.5; paraphrased)

## Verify activities (7.2.4.2, pp. 143–144)
- Check compliance with the organization's BA standards (right tool, right method).
- Check correct use of model notation, templates, forms.
- Check **completeness within each model**.
- **Compare each model with related models**: an element mentioned in this model but missing from the other; elements referenced consistently.
- Check that terms are understandable to stakeholders and consistent with how the organization uses them.
- Add examples where clarification is needed.
- Checklist: a standard set of criteria or one for a specific concern; the purpose is to ensure what matters is in the final product and that the verify process is followed (7.2.4.3).
- BABOK techniques suggested: Acceptance and Evaluation Criteria (written clearly enough to build tests), Item Tracking (manage the issues found), Metrics/KPIs (measure requirements quality), Reviews.
- Result: a **verified** requirement = of sufficient quality to be a basis for further work.

## Validate (7.3.4, p. 146)
1. **Identify assumptions.** For a product that has never existed, assumptions must be made about customer reaction; stakeholders may assume the benefits will occur; the root cause cannot be proved. Assumptions must be recorded to manage risk.
2. **Define measurable evaluation criteria**: the expected benefits are already in the future state but the way to measure them may not exist; determine the baseline from the current state and numeric targets that correspond to the business objectives.
3. **Assess fit with the solution scope**: a requirement that benefits a stakeholder may still not belong in the solution. One that brings no benefit is a candidate for removal. If it does not fit, either revisit the future state and change the scope, or drop the requirement. A design that cannot be validated is a sign of missing/misunderstood requirements or that the design must change.
Inputs needed: business objectives, future state description, potential value, solution scope. If they are missing, write "partial validation".
BABOK techniques suggested: Acceptance and Evaluation Criteria, Document Analysis, Financial Analysis, Item Tracking, Metrics/KPIs, Reviews (confirm stakeholders see the need being met), Risk Analysis.
Result: a validated requirement demonstrably benefits stakeholders and matches the goal of the change; not being validated means it does not benefit the organization, or is out of scope, or both.

## Readiness gate before asking for approval (5.5; paraphrased, the specific conditions are the skill's own)
BABOK 5.5.3: the input to approval is **verified** requirements. Proposed gate:
- No Blocker findings remain.
- Contradictions are resolved or have a decider and a deadline.
- It is known who has the authority to approve and who only has influence (5.5.4.1).
- The risk from lack of consensus is recorded (5.5.4.3: absolute consensus is not needed, but where it is missing the risk must be managed).
- The form of approval matches the approach: predictive usually approves at the end of a phase or at a change control meeting; adaptive approves just before building starts (5.5.2).
The approval outcome (who, when, which version) goes into the trace; see `requirements-trace`.
