# Review report template

**Document**: ... | **Version/date** ... | **Review objective**: ... | **Question answered**: Verify / Validate / both

## 1. Scope checked
- Items checked: ... Characteristics / checklist used: ...
- Could not be checked for lack of information: ... (for example no business goal yet, so validation is partial)

## 2. Verdict
**Not ready / Conditional / Ready** for: validation / approval / handing to the team.
Conditions: 1) ... 2) ...
Number of findings: Blocker n, Should fix n, Suggestion n. Level criteria: Blocker = cannot be built/tested/approved without a fix.

## 3. Findings
| # | Level | Item (code/quoted text) | Characteristic | Problem and why | Proposal | Type (defect/suspicion) |
|---|---|---|---|---|---|---|

## 4. Recurring defect patterns
- ... (appears in n items: ...)

## 5. Questions needing an answer
| # | Question | Ask whom | Deadline |
|---|---|---|---|

## 6. Tracking items
Code | Type | Description | Raised by/date | Owner | Deadline | Status

## Example of one finding line (illustration, composed by the skill)
| 3 | Should fix | AC-01.2 "the system handles a duplicate correctly" | Unambiguous, Testable | Gives no observable result, so a tester cannot write the test | Rewrite: "Only the first person to confirm receives the appointment; the next person sees a message that the slot has just been taken" | Defect |
