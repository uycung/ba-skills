| Item | Problem | Why it is a problem | How to rewrite |
|---|---|---|---|
| "As a user" | Generic role | Not Appropriate or Correct: nobody can say whose need this is | Name the role, for example "registered patient" |
| "manage my appointments easily and send notifications" | Two capabilities and a vague word | Not Singular and not Unambiguous: "manage" and "easily" cannot be tested | One story per capability; replace "easily" with an observable result |
| "so that things are better" | No value stated | Not Necessary: nothing shows why it should be built | State the benefit, for example not having to phone the clinic |
| "The system works correctly" | AC cannot be verified | Not Verifiable and not Complete: no input and no observable result | Write input, action and result, for example "when a slot is booked, a confirmation with doctor and time is shown" |

Rewritten (first slice):
As a registered patient, I want to see my upcoming appointments, so that I know when I have to come.
- Given a registered patient with two booked slots, when the patient opens "My appointments", then both are listed with doctor, date and time.

More notes on 29148: the requirements-review skill, if installed.
