# Scope, functional decomposition, interfaces, role and permission matrix

## Scope modelling (BABOK 10.41, pp. 337–340; the opening part)
A scope model defines boundaries and places elements inside or outside. In scope (like functional decomposition), out of scope (like a context diagram), or both (Venn, use case model). Recognize four kinds of boundary: scope of control (what is being analyzed, roles, inside/outside the organization), need scope, solution scope (requirements met, value, impact of change), change scope (actions, stakeholders, events). Often combined from diagrams, matrices and text. **For phased delivery, describe the scope for each phase**.
How to do it: an In / Out (deliberate) / Undecided table with the reason for being out of scope; a context diagram showing the system in the middle with external actors/systems. The later part of section 10.41 has not been read.

## Functional decomposition (10.22, pp. 283–286; paraphrased)
Divide a process, system, functional area or deliverable into simple parts for independent analysis, estimating and tracking. It assumes that the child components **fully describe** the parent, and that **each child has only one parent**.
- The **purpose of the decomposition** decides what and how deep: measure and manage, design, analysis, estimating and forecasting, reuse, optimization, replacement, packaging.
- **Objects**: business outcomes, work to be done (WBS), processes, functions, business units, solution components, activities, products and services, decisions.
- **Stopping level**: when the analysis goal is reached; do not decompose deeper than the goal needs.
Limits: when information is missing you must decompose again; many systems cannot be adequately represented by a simple hierarchy because interactions create emergent behaviour; one object has many different ways of being decomposed.
How to do it: ask the purpose of the decomposition first; draw the tree; check each node has one parent, and the children cover the parent fully without overlap. For stories: use the decomposition approach of the Agile Extension in `story-writer` (by customer value, not by step/layer).

## Interface analysis (10.24, p. 287 onward; the opening part)
Identify who, what information (with volume), when and how often, where, why, and how for each interface. Types: user, external party (regulator), process, data between systems, API, device. Identifying them early shows which stakeholders must be invited. Suggested table: Interface | Two ends | Information exchanged | Volume | Frequency/trigger | How performed | Owner | Open questions. The sequence diagram (10.42, not read closely) is used to show the order of interactions between components.

## Roles and Permissions Matrix (10.39, pp. 333–335)
Ensures every activity has someone responsible, finds missing roles, and communicates changes. A role is a label for a group of people with a common function; an activity is tied to one or more roles through **authority**.
- Finding roles: look at the organization model, job descriptions, process handbooks, system guides; meet stakeholders. Note that the same job title can have different roles and vice versa.
- Finding activities: use functional decomposition, process models, use cases.
- Permissions: consider the security level and the workflow; confirm with stakeholders.
- Level of abstraction: project level uses **RACI** (Responsible, Accountable, Consulted, Informed); IT systems use **CRUD** (Create, Read, Update, Delete).
Skill rule: mark unknown cells "?", do not fill them in; permissions to view sensitive data go to `nfr-writer` (authorization, logging).
**Check**: every activity has at least one role; every role has at least one activity (if not, it may be superfluous); roles match the process model; activities match the use cases/stories.
