# Test case and coverage matrix template

## Test case
| ID | Source (trace) | Type | Objective | Precondition | Data | Steps | Expected result | Priority | Automated? |
|---|---|---|---|---|---|---|---|---|---|
| TC-01 | AC-02.1 | Standard | Cancel an appointment before the deadline | Customer has a booking at 10:00; the time now is 07:00 | Booking BK-001 (assumed) | 1. Open booking BK-001 2. Choose Cancel 3. Confirm | Status changes to Cancelled; the customer receives a cancellation notice | High | Yes |
| TC-02 | BR-01 | Boundary | Cancel exactly at the 2-hour threshold | Booking at 10:00; the time now is 08:00 | BK-002 | As TC-01 | Cancellation allowed (assumed threshold ≥ 2 hours, BR-01 needs confirmation) | High | Yes |
| TC-03 | BR-01 | Boundary | Cancel below the threshold | Booking at 10:00; the time now is 08:01 | BK-003 | As TC-01 | Rejected, with the message from AC-02.3 | High | Yes |

Priority column: a level proposed from business risk (high/medium/low); it is a skill convention, and the user decides.
Type column: Standard / Exception / Boundary / Bad data / Permission / State / NFR / **Proposed addition** (a case from error guessing or "what if" with no approved AC; leave the expected result empty and write the open question).

## Given-When-Then form (when the team uses BDD)
```
Scenario: Cancel a booking at exactly the 2-hour threshold
  Given booking BK-002 starts at 10:00 and the time now is 08:00
  When the receptionist chooses to cancel booking BK-002
  Then the booking moves to the status "Cancelled"
  And the customer receives a cancellation notice
```
One WHEN per scenario.

## Coverage matrix
| Source | Short description | Related TCs | Missing |
|---|---|---|---|
| AC-02.1 | Cancel before the deadline | TC-01 | |
| BR-01 | Cancellation threshold | TC-02, TC-03 | No test yet for a different time unit |
| NFR-05 | Response ≤ ? | (none yet) | Measure missing, send back to `nfr-writer` |

## "Not enough to write a test" list
| Source | Why it is not written yet | What is needed | Hand off to |
|---|---|---|---|

## UAT scenario (example)
| ID | Business task | Role | Data | Business steps | Expected result | Proves (story/AC) | Result | Notes |
|---|---|---|---|---|---|---|---|---|
| UAT-01 | Book an appointment for a regular customer and receive a reminder | Receptionist | Customer A (assumed) | Find the customer, choose the service, choose the time, confirm | The booking shows correctly; the customer receives the reminder on time | US-01 (AC-01.1–01.4) | Pass/Fail/Blocked | |
