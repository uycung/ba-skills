# Coverage checks and impact analysis

Purpose per BABOK 5.1.8: requirements have clear relationships so that coverage and the effect of changes can be seen. The checklist below is proposed by the skill; it is not an official BABOK list.

## Coverage checks
| # | Check | Level |
|---|---|---|
| 1 | Which goals have no FR/story derived from them? (abandoned goals) | High |
| 2 | Which FRs/stories cannot be traced to any goal or source? (orphan requirements, possible scope creep) | High |
| 3 | Which stories have no AC? | High |
| 4 | Which ACs cannot be verified or have no test case (at the full level)? | Medium |
| 5 | Which business rules are not referenced by any story? Which stories reference a rule that does not exist? | Medium |
| 6 | Which multi-step flows lack exception flows/boundary cases? | Medium |
| 7 | Which system/feature handles personal data, payments, AI or integrations without a corresponding NFR (security, legal, performance)? Call the `nfr-writer` skill. | High |
| 8 | Which NFRs are tied to no function/goal and have no measure? | Medium |
| 9 | Do two requirements contradict each other (same object, different result)? | High |
| 10 | Are two requirements duplicates? | Low |
| 11 | Circular dependencies, or dependencies on items outside the scope? | Medium |
| 12 | Duplicate codes, unusual gaps in codes, links pointing to codes that do not exist? | Low |
| 13 | Which links fail the 5 criteria (defined, necessary, correct, unambiguous, consistent)? Is any requirement stated more than once? (BABOK 7.4) | Medium |
| 14 | Which items are treated as agreed without being approved, or were approved and then edited without going through change assessment? (BABOK 5.5) | High |

## Impact analysis when there is a change
1. Identify the changed item (code, old content → new).
2. Follow the links both ways: upwards (goals, sources: does the change still serve the goal?) and downwards (stories, AC, NFRs, tests, design, user documentation).
3. Classify affected items: must edit / needs review / not affected (give the reason).
4. State the risks: new contradictions, increased scope, effect on the schedule.
5. State who needs to re-approve (by the source/owner of each item).
6. Do not conclude the amount of effort yourself; state only how much is touched and let the team estimate.


Note: sufficient coverage does not mean the set of requirements is coherent; see section 1 of `architecture-approval-review.md`. When presenting the impact analysis above, use the five factors benefit/cost/impact/schedule/urgency (section 3 of that file) to present the impact.
