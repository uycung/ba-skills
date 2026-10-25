# Checklists by document type (the skill's own, based on BABOK characteristics and activities; not a BABOK list)

Use as a starting point; if the team has its own checklist, use the team's.

## Story / AC (cross-check against story-writer)
- Has a specific role, a goal, a value (the WHY is not dropped).
- One value, one deliverable slice; not split by technical layer.
- Every AC is verifiable true/false; has input, action, observable result; has cases for error, empty, duplicate, permission, mid-way cancellation.
- Business rules sit in the BR table, and the story refers to them.
- Vague words without criteria: present or not.
- NFRs are not stuffed into functional AC.
- Has an "out of scope" item when needed.

## Use case / FR
- The name has a verb and a noun; has the primary actor's goal.
- Primary and secondary actors are clear; preconditions, trigger, main flow, alternative and exception flows, postconditions (success and minimal guarantee).
- Written from the actor's viewpoint, not describing how the system works inside.

## NFR
- Every NFR has a measure, a threshold, a measurement condition, a verification method, an evidence label (a/b/c).
- Any number without a source is marked as needing a decision.
- Legal items have a source and a line that needs legal confirmation.
- Transition requirements are separate, not mixed with NFRs.
- Are there conflicting NFRs that need a trade-off decision?

## Business rules
- Atomic, declarative, one source.
- Classified as definitional or behavioural; behavioural ones have an enforcement level.
- Exceptions are recorded as separate rules.
- No contradiction with other rules; terms are in the glossary.

## Models (process, state, data, decision)
- Uses the notation that was chosen correctly.
- Complete within the model: the process has a triggering event, activities, outcome; every decision branch has an exit; states have initial and final states and every transition has an event; entities have identifiers and relationships have multiplicity; the decision table covers all combinations without overlap.
- Cross-checks: the entities in the data model appear in the process/stories; states appear in the AC; the roles in the permission matrix match the roles in the process.

## Whole document (PRD/BRD/SRS)
- Goals, scope and future state are present for validation.
- Each requirement is stated once (BABOK 7.4); codes are stable.
- Glossary; source of each requirement; priority level; open questions are listed.
- Traceability links meet: defined, necessary, correct, unambiguous, consistent (7.4.4.4).
