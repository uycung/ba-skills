# Traceability - clinic booking (medium)

## Catalogue
GOAL-01, GOAL-02, GOAL-03; US-01 to US-05; AC-01.1, AC-01.2, AC-02.1, AC-02.2, AC-03.1, AC-05.1; BR-01, BR-02, BR-03, BR-04; NFR-SEC-01, NFR-PERF-01.

## Matrix
| Item | Traces to | Covered by |
|---|---|---|
| GOAL-01 | - | US-01, US-02, US-04 |
| GOAL-02 | - | US-03 |
| GOAL-03 | - | nothing |
| US-05 | no goal | AC-05.1 |

## Gap report
1. GOAL-03 is not covered by any story, so the weekly report would never be built.
2. US-05 has no source goal: an orphan, possibly scope creep.
3. US-04 is without acceptance criteria.
4. BR-03 is not referenced by any story (unreferenced rule).
5. US-02 points to BR-09, which is not defined anywhere.
6. NFR-PERF-01 ("fast") is not measurable.

## Contradictions
US-02 and AC-02.1 give 2 hours for cancelling while BR-02 gives 24 hours: they conflict.

## To confirm
Which cancel window applies?
