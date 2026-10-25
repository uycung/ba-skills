# Nine quality characteristics (BABOK v3, section 7.2.4.1, p. 143; definitions paraphrased, check questions and typical defects are the skill's own)

BABOK says an acceptable requirement usually shows **many** (not necessarily all nine) of the characteristics, and the "enough" level depends on the method, phase and audience. Do not demand that every item reach every characteristic at the maximum level.

| Characteristic | Meaning | Check question | Typical defect | Fix |
|---|---|---|---|---|
| Atomic | Stands on its own, understood independently of other requirements | Must another item be read to understand it? Does it contain two conditions/two behaviours in one sentence? | "The system allows booking and cancelling and rescheduling" | Split into separate items, one code each |
| Complete | Enough to proceed at a level of detail suited to the phase | Missing role, condition, exception, input/output data, error message? | Only the happy path; missing "what if there is no capacity" | Add it or put it into the to-clarify list; state the expected level of completeness |
| Consistent | Matches stakeholder needs, does not contradict other items | Do two items say different things about the same object? Does a term change meaning? | Item A: cancel at least 4 hours before; item B: cancel at any time | State the contradicting pair and who decides |
| Concise | No superfluous content | Is there a sentence that helps nobody understand or do anything? Repetition? | Explaining project history inside every requirement | Delete or move to the background section |
| Feasible | Within the agreed risk, schedule and budget, or enough to experiment | Does a technical/legal/resource constraint make it impossible? | "100% match for every dentist on every legacy device" | Ask the technical team; propose an experiment or narrow it |
| Unambiguous | Clear enough to tell whether a solution meets it | Would two readers understand it differently? Words like fast, easy, suitable, complete, etc. without criteria? | "Display quickly", "friendly" | Add an observable criterion; for NFRs make it measurable (nfr-writer) |
| Testable | There is a way to verify it has been met | Can a tester write a pass/fail test? Is there an input, an action, an observable result? | "The system handles it correctly" | State the data state, the message, where it is displayed |
| Prioritized | Ranked, grouped or negotiated against other items | Does it have a priority level and a basis? | Everything is "high" | requirements-prioritize |
| Understandable | Uses terms familiar to the reader | Can the document's users understand it without explanation? Are abbreviations explained? | Developer terms in a document for receptionists | Add a glossary, change the words |

Note: BABOK says the "enough" level of Complete depends on the method and the point in the life cycle, and the acceptable level of verification for Testable depends on the requirement's level of abstraction (7.2.4.1). A high-level item can be checked at a high level.

## Additions from ISO/IEC/IEEE 29148:2018 (not part of BABOK)
The standard has nine characteristics of an individual requirement (5.2.5), among which **Necessary, Appropriate, Correct, Conforming** have no separate name in BABOK, and five characteristics of the whole set (5.2.6). When reviewing you can additionally ask: is the requirement still needed (Necessary); is it stating a solution instead of a need (Appropriate); have stakeholders confirmed it is the right need (Correct). Record the finding under the nearest BABOK characteristic, with the label "(29148)" if it rests on a characteristic that exists only in the standard. The list of vague word groups in 5.2.7 serves Unambiguous and Testable. Details and clause numbers: `iso29148.md`.

## How to score
For each item, mark the characteristics that are **violated** (do not mark each cell "pass" for brevity; list the characteristics that were checked in the scope). A defect that recurs across many items: merge it into one "defect pattern" finding with an example and a count, instead of listing a hundred lines.
