# Choosing the document type and mapping sources

## How to choose (BABOK 4.4 asks about the reader; mapping the document type is the skill's convention)
| Ask | Effect |
|---|---|
| Who reads it? | Executives, business users, dev/QA, contractors, regulators |
| What do they need to decide or do? | Approve investment, approve scope, build, test, sign a contract, check compliance |
| Level of detail and formality? | A formal document on a template, a light informal version, or a presentation |
| Are there contractual/regulatory/organizational template constraints? | A mandatory template beats the skill's frame |
| Which activity does it support? | Estimating, design, testing, training, operations |

| Type | For | Focus | Main parts |
|---|---|---|---|
| **BRD** (business requirements document) | Sponsor, leaders, investment approvers; the solution team planning | **Why** the change and its **value**: need, objectives, scope, stakeholders, business requirements, constraints, success criteria, risks | Business, stakeholder (high level), transition at a high level |
| **PRD** (product requirements document) | The product team: PO, design, dev, QA | **What for whom**: problem, users/personas, goals and indicators, scope, requirements by value, release | Stakeholder, solution (story/AC), main NFRs |
| **SRS** (software requirements specification) | Dev, QA, architects, contractors; testing and contracts | **What the system must do and what quality it must reach**, verifiable detail | Solution FR + NFR, interfaces, data, rules, transition |
These three names are industry conventions. ISO/IEC/IEEE 29148 uses the names BRS, StRS, SyRS, SRS and prescribes the content (see `iso29148-content.md`); BRD is close to BRS, SRS shares the name, PRD has no direct counterpart; organizations may use other names or merge them. Several documents can be produced from the same source repository (each type a slice).

## Section → source skill map
| Document section | Taken from | Skill |
|---|---|---|
| Background, need, current state | Current state analysis (6.1) | `business-case-strategy` |
| Objectives, SMART targets, value | Future state (6.2), KPIs (10.28) | `business-case-strategy` |
| In/out scope | Scope model (10.41) | `requirements-modelling` |
| Stakeholders, RACI | Stakeholder analysis (3.2, 10.43) | `requirements-stakeholders` |
| Terminology | Glossary (10.23 if there is one; or the user's glossary) | every skill |
| Business requirements | Objectives, success criteria | `business-case-strategy` |
| Stakeholder requirements | Elicitation results | `requirements-elicitation` |
| Functional requirements, stories, use cases, AC | | `story-writer`, `requirements-modelling` |
| Business rules | BR table, decision tables | `story-writer`, `requirements-modelling` |
| Non-functional requirements | Measurable NFRs | `nfr-writer` |
| Process/state/data models | | `requirements-modelling` |
| Interfaces | Interface analysis | `requirements-modelling` |
| Transition requirements | Conversion data, training, ongoing operation; phase transition plan | `business-case-strategy` + `story-writer` |
| Priority and release | Prioritization table, release plan | `requirements-prioritize` |
| Traceability | Matrix, impact | `requirements-trace` |
| Acceptance criteria, UAT plan | | `requirements-testcases` |
| Assumptions, constraints, dependencies, risks | | every skill; `business-case-strategy` for risks |
| Open questions | | every skill |

## Light version for agile
When the team does not want a long document: a **product summary sheet** (problem, users, goals and indicators, scope) + a **backlog** (stories with AC complete to the level of preparation) + the necessary models + the rule table and NFRs. Agile Extension v2 stresses elaborating only stories that are near their turn and using examples/models as support; do not build a long PRD for stories whose turn has not come. The level of detail follows the chosen BA approach (3.1).
