# Checking test quality and coverage

This checklist belongs to the skill (it refers to BABOK 10.1 for verifiable pass/fail requirements and 5.1 for Validate traceability; the coverage-by-technique part is based on ISTQB CTFL v4.0.1).

## Check each test
- Has an ID, a source (at least one requirement ID), and a one-sentence objective.
- One main idea; no two independent results mixed together (split them).
- Preconditions are enough for someone else to re-run it; the data is concrete (not a generic "valid data").
- Steps are repeatable; the expected result is **observable** and measurable (not "the system handles it correctly").
- The expected result matches the source requirement word for word; if the test adds something the requirement does not say, that signals a missing requirement: record it as a question.
- The test type is sensible (standard, exception, boundary, bad data, permission, state, NFR).
- Does not depend on the result of another test unless the order is stated.

## Check coverage
1. Every agreed requirement (AC, BR, measurable NFR, state transition, decision-table row) has ≥ 1 test.
2. Every BR with a threshold has tests on both sides.
3. Every exception flow of a use case has a test.
4. Every valid state transition has a test; every state with a forbidden action has a negative test (if the requirement states it).
5. Every role has at least one positive and one negative permission test (if a permission matrix exists).
6. No orphan tests (tests that point to no source).
7. Measurable NFRs have a measurement method; non-measurable NFRs have been sent back.
8. Every story has a test that proves end-to-end value, not just tests of the individual ACs.

## Coverage by technique (ISTQB CTFL v4.0.1 units, section 4.2)
When reporting the coverage of a technique, state the coverage item and the formula; do not say a generic "100% covered":
| Technique | Coverage item | Coverage = |
|---|---|---|
| Equivalence partitioning | partitions (including invalid ones) | partitions exercised / total partitions |
| 2-value BVA | boundary values | boundaries exercised / total boundaries |
| 3-value BVA | boundary values and their neighbours | items exercised / total items |
| Decision table | feasible columns | columns exercised / total feasible columns |
| State transition | states; valid transitions; all transitions (including invalid) | per the chosen criterion |
For a test set derived from a story, also check against ATDD (4.5.3): the tests cover every feature of the story, do not go beyond the story, and no two tests describe the same feature.

## Coverage report
A table: source | number of tests | missing types | notes. End with:
- number of requirements with tests / total agreed requirements;
- requirements without tests and why (vague AC, missing values, awaiting a decision);
- what QA must add.
Do not convert this into an "adequate" percentage for the whole set; coverage by requirement does not guarantee that all defects are caught.

## Signs the item must go back to requirement writing
- An AC without concrete values.
- Two ACs giving different results for the same condition.
- A decision table with missing or overlapping combinations.
- A state in a test that is not in the state model.
- Terms in a test that differ from the glossary.
