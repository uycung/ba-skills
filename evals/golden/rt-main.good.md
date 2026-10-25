# Traceability matrix - clinic booking (medium level)

## Catalogue
| Code | Type | Summary | Source | Priority | Status | Version |
|---|---|---|---|---|---|---|
| GOAL-01 | Goal | Book online | package | - | draft | 0.3 |
| GOAL-02 | Goal | Fewer missed appointments | package | - | draft | 0.3 |
| GOAL-03 | Goal | Weekly report of free slots | package | - | draft | 0.3 |
| US-01 | Story | Book an appointment | package | - | draft | 0.3 |
| US-02 | Story | Cancel an appointment | package | - | draft | 0.3 |
| US-03 | Story | Remind the patient | package | - | draft | 0.3 |
| US-04 | Story | Reschedule an appointment | package | - | draft | 0.3 |
| US-05 | Story | Export the audit log | package | - | draft | 0.3 |
| AC-01.1, AC-01.2 | AC | of US-01 | package | - | draft | 0.3 |
| AC-02.1, AC-02.2 | AC | of US-02 | package | - | draft | 0.3 |
| AC-03.1 | AC | of US-03 | package | - | draft | 0.3 |
| AC-05.1 | AC | of US-05 | package | - | draft | 0.3 |
| BR-01, BR-02, BR-03, BR-04 | Rule | as in the package | package | - | draft | 0.3 |
| NFR-SEC-01, NFR-PERF-01 | NFR | as in the package | package | - | draft | 0.3 |

## Matrix
| GOAL | US | AC | BR | NFR | Notes |
|---|---|---|---|---|---|
| GOAL-01 | US-01, US-02, US-04 | AC-01.1, AC-01.2, AC-02.1, AC-02.2 | BR-01, BR-02 | - | US-04 has no AC |
| GOAL-02 | US-03 | AC-03.1 | BR-04 | - | |
| GOAL-03 | - | - | - | - | no story |
| - | US-05 | AC-05.1 | - | - | no goal |

## Gaps
| # | Check | Related items | Level | Proposal |
|---|---|---|---|---|
| 1 | Goal without stories (check 1) | GOAL-03 | High | GOAL-03 is abandoned: no story covers the weekly report; add a story or drop the goal |
| 2 | Orphan requirement (check 2) | US-05 | High | US-05 and AC-05.1 trace to no goal or source: possible scope creep; ask the owner for the goal |
| 3 | Story without AC (check 3) | US-04 | High | US-04 has no AC, so it cannot be tested |
| 4 | Rule not referenced (check 5) | BR-03 | Medium | No story references BR-03; link it or drop it |
| 5 | Dangling reference (check 5) | US-02, BR-09 | Medium | US-02 references BR-09, which does not exist in the package |
| 6 | NFR without a measure (check 8) | NFR-PERF-01 | Medium | "should be fast" is not measurable and tied to no function; hand to nfr-writer |

## Contradictions
- US-02 and its AC allow cancelling up to 2 hours before the start; BR-02 says up to 24 hours. They contradict each other (check 9). Needs a decision from the owner of BR-02.

## To confirm
- Which window is right for cancelling?
- Does US-05 serve a goal that is not in the package?
