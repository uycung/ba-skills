# [System name]: Software Requirements Specification (SRS)

Version: | Date: | Status: | Author: | Approver:

> The skill's frame based on BABOK, not a standard frame. ISO/IEC/IEEE 29148:2018 prescribes only the content of the SRS (9.6), not the order of sections; see `references/iso29148-content.md` if a comparison is needed. If a contract requires its own template, map into that template.

## 1. Introduction
Purpose, system scope (in/out), intended readers, how to read the document, references.
## 2. Overall description
System context, actors and roles, constraints, assumptions and dependencies.
## 3. Models
Process, state, conceptual data, data dictionary, scope/context.
## 4. Functional requirements
By functional group; each item:
| ID | Description | AC | BR | Role | Priority | Source (trace) |
|---|---|---|---|---|---|---|
Use cases when the flow is complex (name, goal, actors, preconditions, trigger, flow, postconditions).
## 5. Business rules
## 6. Interface requirements
User; external systems (interface table: two ends, information, volume, frequency, how performed); API.
## 7. Non-functional requirements
| ID | Characteristic | Measure | Threshold | Condition | How measured | Source |
|---|---|---|---|---|---|---|
## 8. Data requirements
Attributes, permitted values, retention, personal data (flagged for someone with legal expertise to review).
## 9. Transition requirements
## 10. Verification and acceptance
Verification method for each group of requirements; acceptance criteria; refer to the UAT plan.
## 11. Appendices
Traceability matrix; glossary; approval; change history.
### What is still missing
Open questions, gaps, and for each the person and the skill that can close it.
### Ready for approval?
Yes / No, with the blockers; if No, run `requirements-review` first.
