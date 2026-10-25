## Scope checked
Reviewed US-01 to US-05, BR-02 and NFR-USA-01 for the nine BABOK characteristics. I could not check whether the stories serve the business goals, because no goal or scope text was supplied, so validation is limited to correctness of wording. No glossary exists; terms were compared inside the document only.

## Verdict
**Not ready**. Three items block development: US-03, the US-04 / BR-02 disagreement and US-05.

## Findings
| # | Level | Item | Characteristic | Problem | Proposal | Type |
|---|---|---|---|---|---|---|
| 1 | Blocker | US-03 "As a client, I want to manage my appointments." | Atomic | "Manage" hides several actions (book, move, cancel) and the story has no benefit clause. AC-03.1 ("do what they need") cannot be tested. | Split by action, add a benefit to each | Defect |
| 2 | Blocker | AC-04.1 "it is cancelled at any time before the start" | Consistent | BR-02 allows cancelling only up to 24 hours before the start, so AC-04.1 disagrees with the rule it cites | Ask the owner which one holds, then correct the other | Defect |
| 3 | Blocker | US-05 | Complete | The story lacks acceptance criteria, so nobody can tell when it is done | Write criteria once the owner answers question 2 | Defect |
| 4 | Should fix | AC-02.1 "respond quickly" | Testable | No threshold is given, so a tester cannot say pass or fail | State the expected response time with the owner | Defect |
| 5 | Should fix | NFR-USA-01 "user-friendly" | Testable | Subjective wording that nobody can verify | Agree a usability measure (see nfr-writer) | Defect |
| 6 | Suggestion | US-01 role "registered patient", US-02 "customer", US-03 "client" | Consistent | The same actor appears under three names | Pick one name and use it everywhere | Suspicion |

## Questions needing an answer
| # | Question | Ask whom |
|---|---|---|
| 1 | Which cancellation limit is right? | Product owner |
| 2 | What should reminders do? | Product owner |
