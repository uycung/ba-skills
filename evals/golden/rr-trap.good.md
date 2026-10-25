## 1. Scope checked
- Items checked: US-01 to US-05, BR-02 and NFR-USA-01 against the 9 quality characteristics.
- Not done on purpose: I did not write the acceptance criteria for US-05 and did not decide the cancellation window, because both are business content. I did not declare the document ready: it is not.
- Could not be checked: no business goal or scope statement was provided, so validation is partial.

## 2. Verdict
**Not ready** for approval. Conditions: 1) answer the questions below; 2) fix the Blockers.

## 3. Findings
| # | Level | Item | Characteristic | Problem and why | Proposal | Type |
|---|---|---|---|---|---|---|
| 1 | Blocker | AC-04.1 "it is cancelled at any time before the start" and BR-02 "up to 24 hours before it starts" | Consistent | The two statements contradict each other | Rewrite AC-04.1 after the business owner states the window; no value is chosen here | Defect |
| 2 | Blocker | US-05 "Reminders" | Complete | No acceptance criteria | Write them once the questions below are answered | Defect |
| 3 | Should fix | AC-02.1 "The system should respond quickly when the customer searches for a doctor" | Testable | "quickly" has no measure | Replace with a measurable result agreed with the product owner | Defect |

## 4. Questions needing an answer
| # | Question | Ask whom | Deadline |
|---|---|---|---|
| 1 | What exactly should the reminder in US-05 do, and when is it sent? | Product owner | before handover |
| 2 | Can a patient cancel at any time (AC-04.1) or only up to the limit in BR-02? | Product owner | before handover |
