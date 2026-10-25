# Quality criteria and defect list

## 1. The nine characteristics of a good requirement (BABOK v3, section 7.2.4, p. 143)
Paraphrased, read from the copy of BABOK v3 supplied by the user.
| Characteristic | Ask during self-check |
|---|---|
| Atomic | Understandable on its own, without reading other sentences? Says only one thing? |
| Complete | Detailed enough for the team to take the next step (design, code, test) at this stage? |
| Consistent | Does it contradict another requirement or a known stakeholder need? |
| Concise | Is any word superfluous, without affecting behaviour? |
| Feasible | Can it be done within the agreed risk, time and budget? |
| Unambiguous | From the result, can you tell pass from fail? |
| Testable | Is there a way to check whether it has been met? |
| Prioritized | Ranked against other requirements? |
| Understandable | Uses the reader's own terms? |
Note per BABOK: the final quality is decided by the stakeholders; the "sufficient" level of detail depends on the method and the phase.

## 2. INVEST for stories (Agile Extension v2, section 7.21.2, p. 103; paraphrased)
Independent (deliverable independently of other features), Negotiable (the team negotiates how to deliver), Valuable (states value to the customer), Estimable (the team can estimate it from experience), Sized appropriately (finished within one iteration, generally the smaller the better), Testable (stakeholders can verify it objectively). The Agile Extension says not every backlog item must be written as a user story.
Note: the main BABOK Guide v3 does not have INVEST; the Agile Extension does. Attributing its origin to a specific author is knowledge from outside the documents, and we do not rely on it.

## 3. Story frame (BABOK v3, section 10.48.3, p. 360; Agile Extension 7.21, pp. 103–104)
BABOK says there is no mandatory structure. Common form: Who (role/persona), What (the action/behaviour/feature/quality needed), Why (the benefit). Add: an optional title (verb + goal), a "conversation" (the extra discussion during implementation), and acceptance criteria to bound the story's scope. Limits to remember: a story is a tool for quick recording and short-term prioritization, not a substitute for long-term knowledge storage or detailed analysis; additional documents may be needed for governance and baselines.

## 4. Common defects and fixes
| Defect | Sign | Fix |
|---|---|---|
| Vague words | fast, easy, friendly, reasonable, complete, flexible, "etc." | Replace with an observable condition; if it is a quality (performance, usability) → move to an NFR with a measure |
| Solution instead of need | "use a dropdown", "add button X" before the goal is clear | Write the user's goal first; leave interface detail to design/prototype |
| Fake story | "As a developer, I want to refactor...", "As the system, I want..." | Write it as a technical task or attach it to a story with user value |
| Generic role | "As a user..." | Use a specific role and distinguish permissions |
| Story too large | many "and/or", several roles, more than about 8 AC | Split by vertical slice (one flow through all layers), not by technical layer |
| AC with only the happy path | no errors, empty, duplicate, permission, mid-way cancellation | Probe boundary cases (see ac-patterns.md) |
| Several rules in one sentence | "If A or B and not C..." | Convert to a decision table/rule table |
| Business rule buried in operation steps | numbers, thresholds, conditions in the middle of the flow | Pull out a rule table with codes (BR-xx), the story references them |
| No observable result | "the system handles it correctly" | State the data state, the message, where it is displayed |
| No "out of scope" | arguments at acceptance | State plainly what is deliberately not done |

## 5. Additions from Agile Extension v2 (pp. 102–105)
- **3C**: Card (a short card), Conversation (the discussion; a story deliberately does not contain everything), Confirmation (confirmed through acceptance criteria, which bound the story's scope and are the basis for acceptance/regression/exploratory tests).
- Two sentence templates: "As a <role>, I need to <feature> so that <goal or value>" and "In order to <value>, as a <role>, I need to <behaviour>". The optional title takes the form verb + goal.
- **Limits** named by AE: too many stories bloat the backlog; stories breed more stories so information must be kept current; teams easily fall into individual stories and lose sight of the vision/roadmap; teams easily get into the habit of skipping the value (WHY) and looking only at the feature (WHAT). Look for these defects at the end of a review.
- Many teams supplement stories with analysis models: data models, business rules, UAT, mock-ups, context diagrams, state diagrams.
- **Definition of Ready / Done** (AE glossary p. 5, no section of its own): a set of criteria the team agrees and displays to treat a backlog item as "ready to start" or "done". Ask the team whether they have one; if so, check the story against it.
- **ISO/IEC/IEEE 29148:2018, 5.2.4 NOTE 2** (the standard itself was read): in agile, requirements may be expressed as user stories without using "shall". The standard still requires a good requirement to have the characteristics in 5.2.5 (Necessary, Appropriate, Unambiguous, Complete, Singular, Feasible, Verifiable, Correct, Conforming); a story together with its AC is assessed against those characteristics when the organization's requirements conform to 29148. Cross-reference notes: `requirements-review/references/iso29148.md`.
