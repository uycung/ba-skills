# How to write acceptance criteria and use cases

## Two forms of AC
1. **List of rules** (simple, fast): each line is one verifiable condition. Use when the behaviour is linear or the rules are about data.
2. **Given/When/Then** (BABOK 10.48.3 names this a common form): Given = initial state, When = one action, Then = an observable result. Use when there is context/state. One When per scenario; Then states the result explicitly (message, data state, page change); avoid "the system works correctly".
Choose one form for each story; do not mix them.

## Boundary cases to probe for each story
- Data: empty, one element, maximum, over the maximum, special characters, duplicates, wrong format.
- Permission/role: a person without permission, expired session, several people editing at once.
- State: acting when the object is in an invalid state (cancelled, locked, deleted).
- Interruption: network lost midway, double click, going back, cancelling.
- Integration: the external system is slow/failing/returns something unusual.
- Error messages: say what went wrong and what to do next.
- Audit trail: is logging/auditing needed (if yes → see the security NFR).
Skip items that do not apply; items that are unclear go into "To clarify".

## Use case (BABOK 10.47, pp. 356–358)
Elements: name (verb + goal), primary and secondary actors (an actor is an external person/system, not an event), preconditions (true before it starts, not checked within the use case), trigger, main flow (the shortest successful path), alternative flows (still reach the goal by another route), exception flows (do not reach the goal, how the system responds), postconditions/guarantees (true in every flow; success guarantee and minimal guarantee on failure).
BABOK caution: business rules and decisions should be managed separately and referenced; do not record every UI interaction step by step; a use case does not discuss solution design.

## Business rule table (proposed)
| Code | Rule | Source/owner | Applies to story |
Use when there are conditions, thresholds, formulas. The story just says "per BR-03".

## Acceptance criteria per BABOK 10.1 (pp. 217–220; paraphrased)
- **Acceptance criteria** are the minimum conditions for a solution to be worth deploying/accepting; usually used when only one solution is considered and written as **pass/fail**. **Evaluation criteria** are used to rank several options, so they are a continuous/discrete scale. Do not mix the two: the story for one function uses acceptance criteria.
- They must be **verifiable true/false**. BABOK says you may need to **split requirements down to atomic form** to write test cases. An AC containing two conditions is split in two.
- The root is **value attributes** (attributes of value whose definition the stakeholders agreed). An AC based on an attribute whose meaning nobody has agreed goes into "To clarify".
- When a requirement is a contractual obligation, the AC are hard to change later (a limit BABOK names): settle them carefully before signing.
- Verification method: usually through UAT. Each AC should be able to answer "who checks, with what data, observing what".

## Given-When-Then per Agile Extension 7.2 (p. 60)
Each scenario: one situation (GIVEN, extended with AND), **exactly one triggering event** (WHEN), a result (THEN, possibly several ANDs). Each scenario is one concrete example with real figures. For coverage: ask "what if..." for each GIVEN. When there are too many combinations of conditions, switch to a decision table instead of increasing the number of scenarios.
