# Deriving tests from requirements

The "basis" lines say what comes from BABOK/Agile Extension, what comes from ISTQB CTFL v4.0.1 (checked against the PDF; paraphrased), and what is common practice or a skill convention.

Shared ISTQB terminology: a **coverage item** is the thing to be reached (partition, boundary value, rule column, state, transition). Coverage = number of coverage items reached by at least one test / total number of coverage items. Report coverage in exactly those units; never say "100% covered" without naming which coverage item.

## 1. Acceptance criteria in Given-When-Then form
Basis: Agile Extension 7.2 (BDD scenarios serve as AC and as tests; one WHEN; GIVEN/THEN can be joined with AND).
- Each scenario = at least one test; a scenario with several THENs is still one test if it has the same single WHEN.
- Ask "what if" for each GIVEN: missing data, wrong format, a different permission, a different state, two people at once. This is how missing scenarios are exposed (Agile Extension 7.2.2); record the extra cases found as proposed additional AC, and **do not** treat them as approved.
- AC in rule form (a list of conditions): one test per line.

## 2. Business rules with thresholds (BR)
Basis: ISTQB CTFL v4.0.1, 4.2.1 and 4.2.2.
- **Equivalence partitioning (EP)**: divide the data into partitions that the test object is expected to process the same way; in theory of the technique one test per partition is enough. Partitions do not overlap and are not empty; they apply to inputs, outputs, configuration, internal values, time and interface parameters. Valid and invalid partitions: the definition of "valid" can differ between groups, so ask the requirement rather than deciding yourself. EP coverage is counted over partitions, including invalid ones.
- Several input parameters: the simplest criterion is **Each Choice** — each partition of each parameter appears at least once; it does **not** consider combinations across parameters. When combinations are needed, use a decision table or state clearly that it is a risk decision.
- **Boundary value analysis (BVA)**: applies only to ordered partitions. Two versions: **2-value** (the boundary value and its nearest neighbour in the adjacent partition) and **3-value** (the boundary value and both neighbours). 3-value is stricter: the ISTQB example is the condition "x ≤ 10" wrongly implemented as "x = 10": the 2-value pair (10, 11) does not catch the defect, while x = 9 of the 3-value version is likely to catch it. Skill default: use 3-value for rules with thresholds and say that you chose it; use 2-value when the user asks for a compact set.
- Example rule "cancel at least 2 hours ahead" (assuming the unit is minutes, threshold 120): 3-value = 119, 120, 121. This example is the skill's illustration, not ISTQB's.
- Definition rules (not behaviour) are usually verified with classification examples, not flows.
- Source note: the v4.0.1 release notes say something was added about handling invalid partitions in 4.2.1, but the 4.2.1 text in the PDF that was read does not contain that sentence. The practice "each test contains only one invalid value" because it avoids defect masking is reasonable, and ISTQB states a similar principle for invalid transitions in 4.2.4, but do not cite it as text of 4.2.1.

## 3. Decision tables
Basis: a decision table is a compact way to represent all the rules of a decision (BABOK 10.17); tests are derived per ISTQB CTFL v4.0.1, 4.2.3.
- Rows are conditions and actions; each **column** is a decision rule. ISTQB notation: conditions T (true), F (false), "–" (does not affect the outcome), N/A (infeasible for that rule); actions X (happens), blank (does not happen). A **limited-entry** table uses only Boolean values; an **extended-entry** table lets conditions/actions take multiple values (ranges, partitions, discrete values).
- The coverage items are the **feasible columns**. **Each feasible column = one test** (a concrete combination of conditions + the result). Coverage = columns exercised / feasible columns.
- A full table has columns for every combination; dropping infeasible columns and merging columns where the condition has no effect gives a collapsed table. The number of rules grows exponentially as conditions are added; when there are too many, use a collapsed table or a risk-based approach and say that you did. Collapsing algorithms are outside the syllabus.
- A strength ISTQB names: it exposes combinations that are easy to miss and exposes gaps or contradictions in the requirements. So a combination with no column, or two contradicting columns, is an **open question**; do not guess the result.
- A "–" cell (does not affect): pick another value of that condition in at least one test to confirm that it really has no effect (this is the skill's practice, not an ISTQB requirement).

## 4. State model / state table
Basis: a state table lists every transition (BABOK 10.44.3.4); tests are derived per ISTQB CTFL v4.0.1, 4.2.4.
- A transition is labelled "event [guard condition] / action"; the guard and action can be omitted if there are none. A test is usually a sequence of events leading through a sequence of states, and **one test can cover several transitions**. A state table differs from a diagram in that empty cells show clearly which transitions are invalid.
- Three coverage criteria (choose one and state it in the report):
  - **All states**: the coverage item is the state. The weakest; often met without running all transitions.
  - **Valid transitions** (also called 0-switch): the coverage item is each valid transition. The most common; meeting it includes all-states coverage. Skill default.
  - **All transitions**: run every valid transition and **attempt** the invalid ones; includes both criteria above. ISTQB says this should be the minimum for mission-critical and safety-critical software.
- **Each valid transition = one test** (starting state, event, condition, end state, accompanying action).
- **Invalid transitions**: for each state, try an event that is not in the table and expect it to be rejected. **Each test tries only one invalid transition** to avoid defect masking (one defect hiding another). Write these only when the requirement states the reaction; otherwise ask.
- Check the actions permitted in each state (for example editing after cancellation).
- Final state: check that no transition leaves it.

## 5. Use cases
Basis: main flow, alternative flows, exception flows, postconditions that hold for every flow (BABOK 10.47).
- One test for the main flow; one test for each alternative flow; one test for each exception flow.
- For each test, check the postconditions (success and at minimum: security, data integrity).
- Preconditions are not checked within the use case (10.47); if behaviour when a precondition is false needs checking, that is a test of another requirement.

## 6. Non-functional requirements
Basis: measurable criteria, so each NFR needs a measure, a condition and a measurement method (from `nfr-writer`).
- Each measurable NFR = one test with the threshold, load/condition, measurement tool and environment.
- An NFR without a measure: do not write a test; hand off to `nfr-writer`.
- Parts that need specialist expertise (load, security, accessibility): state the test type and hand off to QA/specialists; the BA states the requirement and threshold and does not design the technical scenario.
- Legal NFRs (personal data and so on): state only what has to be demonstrated and hand it to someone with legal expertise to confirm.

## 7. Data and the data dictionary
- Every permitted value, length, format and mandatory flag = valid/invalid tests at the boundary.
- Relationships (multiplicity) = tests for the minimum and maximum counts (0, 1, many) if the requirement states them.

## 8. Permissions (role matrix)
- Each CRUD cell marked "allowed" = a positive test; each cell marked "not allowed" = a negative test (expect rejection). A "?" cell = an open question.

## 9. Experience-based techniques (added after the formal techniques)
Basis: ISTQB CTFL v4.0.1, 4.4. Use when requirements are missing or vague, or to supplement the techniques above; they do not replace them.
- **Error guessing** (4.4.1): based on how the application has worked, the kinds of mistakes developers make, and defects in similar systems. Suggested defect groups: input, output, logic, calculation, interface, data. Error-guessing cases **have no requirement source**, so give them the type "Proposed addition"; the expected result is an open question for the BA/PO, not something the skill dictates.
- **Exploratory** (4.4.2): design, execution and evaluation happen at the same time; it can be session-based with a time box, a charter and a debrief. ISTQB says it is useful when the specification is thin or missing, or when time is short. The skill only proposes the charter (goal, scope, duration); the testers do the running.
- **Checklist-based** (4.4.3): checklist items should be questions that check each item separately; ISTQB advises against putting in a checklist items that can be automated, items that belong to entry/exit criteria, or items that are too general. The quality checklist of `requirements-review` or the ISO 25010 characteristics can serve as a basis; state that this is a checklist and not a requirement.

## 10. Acceptance criteria formats and ATDD
Basis: ISTQB CTFL v4.0.1, 4.5.1 to 4.5.3; Agile Extension 7.2.
- AC are the conditions under which stakeholders accept a story and can be treated as test conditions. ISTQB names two common forms: **scenario-oriented** (Given/When/Then) and **rule-oriented** (a checklist or an input-output table); a team may use another form if it is clear and unambiguous. Rule form: one test per line (see section 1).
- AC should describe both positive and negative scenarios (4.5.2). If an AC has only the happy path, put it in "To clarify".
- **ATDD** (4.5.3): tests are created before implementation, from a workshop with several viewpoints (customer, dev, tester). ISTQB suggests this order: positive tests first, then negative, then non-functional characteristics. The tests cover every feature of the story, do not go beyond the story, and no two tests describe the same feature. Use these three criteria to self-check the test set (linked to `test-quality.md`).
- A story that is hard to write tests for (stakeholders do not know how to verify it) signals a story that is unclear or lacks value under INVEST (4.5.1): hand it back to `story-writer`.
