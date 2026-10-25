# Business rules (BABOK 10.9, pp. 240–243; paraphrased)

Use when a story/FR contains numbers, thresholds, conditions, exceptions. Pull them out into a BR-xx table; the story only refers to them.

## Writing principles
- Clear, specific, accessible, **a single source**; use standard business terms so domain experts can check them.
- Write them **atomically and declaratively** (say what is true, not how); **separate them from the process** they support/constrain; **separate them from how they are enforced**; map them to the decisions they govern.
- **Exceptions are rules too**; record them as separate rules.
- Rules are technology-independent; they can be implemented on many platforms.
- Old rules need to be challenged: do they still serve the goal?
- A rule must be "practicable": business people can use it without further interpretation, and it is within the enterprise's control.

## Two kinds
| Kind | Nature | Can be violated? | Example (BABOK) |
|---|---|---|---|
| Definitional (definition/calculation) | States what is necessarily true about a concept, or how something is derived/calculated | Cannot be violated, but can be applied wrongly | A customer who places more than 10 orders a month is considered a Preferred Customer; a tax formula |
| Behavioural | An obligation/prohibition on the actions of people (even when automated) | Can always be violated | An order may not be placed when the billing address differs from the address held by the card issuer |

## Enforcement level for behavioural rules (ask, do not choose yourself)
Violation not allowed; a person with authority may override; override with justification; not actively enforced (then it is only guidance). Also ask about: sanctions for violation, additional responses.

## Columns for the BR table
Code | Statement | Type (definitional/behavioural) | Enforcement level | Source (policy, law, person) | Owner | Referencing story
Limits named by BABOK: a long list easily becomes ambiguous, rules may contradict each other when combined so they must be cross-checked, and a poor vocabulary makes rules wrong. When there are many combinations of conditions, use a decision table (BABOK points to Decision Analysis).
