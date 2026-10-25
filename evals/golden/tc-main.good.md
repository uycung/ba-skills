## Test cases for US-01 and US-02

| ID | Source | Test | Expected |
|---|---|---|---|
| TC-01 | AC-01.1 | A registered patient confirms a free slot | The slot is marked taken and a confirmation is shown |
| TC-02 | AC-01.2 | Two patients confirm the same slot | Only the first succeeds; the second sees "This slot has just been taken" |
| TC-03 | BR-01 | A patient books a second appointment with the same doctor on the same day | The expected result is not stated in the package |
| TC-04 | AC-02.2 | An appointment starting in less than 2 hours | The Cancel button is not shown |

Coverage: US-01 has three tests, US-02 one. Sample data is an assumption: fake names and numbers only.

## Not enough to write a test
- BR-09 is cited by US-02 but is not defined, so no test can use it.
- US-02 and AC-02.1 say 2 hours but BR-02 says 24 hours: a conflict, so the cancellation boundary has no test yet.
