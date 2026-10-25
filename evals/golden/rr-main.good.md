# Review report

**Document**: Clinic booking - stories, draft v0.2 | **Review objective**: find defects | **Question answered**: Verify

## 1. Scope checked
- Items checked: US-01 to US-05, BR-02 and NFR-USA-01 against the 9 quality characteristics and the story checklist.
- Could not be checked for lack of information: no business goal or scope statement was provided, so validation is partial; there is no glossary, so terminology is checked only for consistency inside the document.

## 2. Verdict
**Not ready** for handing to the team.
Conditions: 1) resolve the three Blockers; 2) answer the questions in section 5; 3) re-check the Should fix items.
Level criteria: Blocker = cannot be built, tested or approved without a fix.

## 3. Findings
| # | Level | Item (code/quoted text) | Characteristic | Problem and why | Proposal | Type (defect/suspicion) |
|---|---|---|---|---|---|---|
| 1 | Should fix | AC-02.1 "The system should respond quickly when the customer searches for a doctor" | Testable, Unambiguous | "quickly" gives no measure, so a tester cannot decide pass or fail | Replace with a measurable result: the search returns within [value to be confirmed] seconds under [conditions to be confirmed] | Defect |
| 2 | Blocker | US-03 "As a client, I want to manage my appointments." and AC-03.1 | Atomic, Unambiguous, Testable | "manage" covers booking, moving and cancelling; there is no value ("so that"); AC-03.1 "do what they need" cannot be tested | Split into one story per action, each with a role, a value and its own AC | Defect |
| 3 | Blocker | AC-04.1 "it is cancelled at any time before the start" and BR-02 "up to 24 hours before it starts" | Consistent | Contradiction: US-04 allows cancelling at any time, BR-02 limits it to 24 hours | Decide with the business owner which rule is meant, then align AC-04.1 and BR-02 (no value is chosen here) | Defect |
| 4 | Blocker | US-05 "Reminders" ("No acceptance criteria yet.") | Complete, Testable | The story has no AC, so it cannot be tested or estimated | Write the AC after the questions below are answered | Defect |
| 5 | Should fix | US-01 "registered patient", US-02 "As a customer", US-03 "As a client" | Consistent | Three different words for what looks like the same role | Agree one term in a short glossary and use it in all stories | Suspicion |
| 6 | Should fix | NFR-USA-01 "The system shall be user-friendly" | Testable, Unambiguous | "user-friendly" has no measure | Replace with a measurable usability criterion agreed with the product owner (nfr-writer can help) | Defect |

## 4. Recurring defect patterns
- Words without a measure ("quickly", "user-friendly", "manage", "what they need"): AC-02.1, AC-03.1, NFR-USA-01.

## 5. Questions needing an answer
| # | Question | Ask whom | Deadline |
|---|---|---|---|
| 1 | Can a patient cancel at any time (AC-04.1) or only up to the limit in BR-02? | Product owner | before handover |
| 2 | What should the reminder in US-05 do, and how will a tester know it worked? | Product owner | before handover |
| 3 | Are "patient", "customer" and "client" the same role? | Product owner | before handover |
