# Choosing a model (BABOK 7.1.4.1, pp. 138–139; pairing questions with models is the skill's suggestion)

## Two forms of representation
- **Matrix**: when the structure is complex but uniform, divisible into elements that apply to every row (data dictionary, traceability, gap analysis, prioritization, attributes).
- **Diagram**: to show complexity that is hard to put in words, draw domain boundaries, classification and hierarchy, the components of a data object and relationships.

## Five groups of models (BABOK) and techniques
| Group | What the model shows | Techniques |
|---|---|---|
| People and roles | Organizations, groups, roles and their relationship to the solution | Organizational Modelling, Roles and Permissions Matrix, Stakeholder List/Map/Personas |
| Rationale | Why the change | Decision Modelling, Scope Modelling, Business Model Canvas, Root Cause Analysis, Business Rules Analysis |
| Activity flow | Sequences of actions, events | Process Modelling, Use Cases and Scenarios, User Stories |
| Capability | Features/functions of the organization or solution | Business Capability Analysis, Functional Decomposition, Prototyping |
| Data and information | Characteristics and exchange of information | Data Dictionary, Data Flow Diagrams, Data Modelling, Glossary, State Modelling, Interface Analysis |
Use the combination that best fits the stakeholders and the context; each technique has its own strengths and weaknesses and gives a different viewpoint.

## Choosing by question (the skill's suggestion)
| The user's question | Model |
|---|---|
| "How does the work run now / how will it run?" | Process (as-is / to-be), lanes by role |
| "What states does X (order, appointment, file) pass through, and who can do what in each state?" | State |
| "What must the system store and how do the things relate?" | Conceptual data + data dictionary |
| "The same term, but everyone understands it differently" | Glossary / concept model |
| "When A, B, C, what is the result?" | Decision table |
| "What does the user do to reach the goal, including when something fails?" | Use case and scenarios |
| "What is in and what is out?" | Scope (context diagram, in/out table) |
| "What parts does this function consist of?" | Functional decomposition |
| "What does the system exchange with other systems/people?" | Interface analysis, sequence diagram |
| "Who can do what?" | Role and permission matrix (RACI, CRUD) |

## Levels of abstraction (7.1.4.4)
Not every stakeholder needs the whole model. Several viewpoints can be built for the same need, but the meaning and purpose must be preserved across every representation. How the BA works (predictive or agile) also affects the level of detail and the type of model.

## Requirements analysis while modelling (7.1.4.2)
Decompose the information, then see: what must change, what must stay the same, which components are missing, which are superfluous, which constraints and assumptions have an effect. The level of detail depends on stakeholders' understanding, the risk of misunderstanding, organizational standards, contractual and regulatory obligations.

## Requirement attributes (7.1.4.3)
Besides the model, record the requirement's attributes/metadata (chosen when planning BA information management) and classify by the requirements classification schema (business, stakeholder, solution, transition).
