# ISO/IEC/IEEE 29148:2018, clause 9: BRS, StRS, SyRS and SRS content, compared with the skill's frame

Source: the standard ISO/IEC/IEEE 29148:2018(E) supplied by the user; clauses 9.2, 9.3, 9.4, 9.5 and 9.6 were read in full. The section names below are paraphrased.

## What to remember first
1. **The standard prescribes content, not the structure of sections.** The order and the way sections are divided are chosen by the project's information management policy (9.3.1, 9.4.1, 9.5.1, 9.6.1). So the skill's `templates/` frame is not "wrong against the standard" when the order differs; what must be checked is **that each content item the standard requires has a place somewhere**.
2. The standard uses the names BRS, StRS, SyRS, SRS. "BRD" and "PRD" are industry names, not names in the standard; BRD is close to BRS/StRS, PRD has no direct counterpart.
3. The skill's frame is still designed by the skill based on BABOK. The tables below only show which items of the standard already have a place and which do not.
4. If a contract or the organization requires conformance with 29148, this is a content checklist, not evidence of conformance. The person responsible for compliance must confirm.

## General content (9.2), applying to text documents
Identification (title, revision notice: version, date, approver, change list); front matter (table of contents, list of figures, list of tables); definitions; references (full name, number, date, issuing organization, where to obtain; preferably separate documents with mandatory requirements from documents for reference only); abbreviations. The skill's templates already have version, terms, change history; they do not mention the list of figures/tables or separating "mandatory" references from "reference-only" ones.

## BRS, clause 9.3 (18 items) → the skill's BRD
| Standard | Content | Place in the skill's BRD |
|---|---|---|
| 9.3.2 | Business purpose: reason and context, how the system contributes to the goals | §2 Background and need |
| 9.3.3 | Business scope: business domain, activities in scope, external entities, system scope and assumptions | §4 Scope |
| 9.3.4 | Business overview: internal parts and external entities, relationships (a diagram is advisable) | No place of its own; put in §4 with a context diagram |
| 9.3.5 | Main stakeholders and influence | §5 |
| 9.3.6 | Business environment: market trends, laws and regulations, social responsibility, technology platforms | Partly in §2; **not separated** |
| 9.3.7 | Mission, objectives | §3 |
| 9.3.8 | Business model: products/services, territory, channels, partners, finance and revenue | **Not yet available** |
| 9.3.9 | Information environment: project portfolio, long-term systems plan, enterprise-level database configuration | **Not yet available** |
| 9.3.10 | Business processes (numbered, activity-chain diagram) | No place in the BRD; process models are in SRS §3 / `requirements-modelling` |
| 9.3.11 | Business policies and rules (naming, numbering, referenced from processes) | SRS §5; the BRD has none |
| 9.3.12 | Business operational constraints (for example finished within a day) | §10 (not separated from project constraints) |
| 9.3.13 | Operational modes: overload, manual when the system is not available | **Not yet available** |
| 9.3.14 | Business operational quality | Could go into §6 or business-level NFRs; no place of its own |
| 9.3.15 | Business structure: organization, roles, geography, resource sharing | **Not yet available** (partly in §5) |
| 9.3.16 | High-level operational concept: policies and constraints, description of the proposed system, modes, user groups, support environment | §9 Options and recommendation (approximately) |
| 9.3.17 | High-level operational scenarios | **Not yet available** |
| 9.3.18 | Other life-cycle concepts: acquisition, deployment, support, retirement | §8 transition (partly) |
| 9.3.19 | Project constraints: cost and schedule | §10 |
Consequence: the skill's BRD leans towards business analysis per BABOK (need, objectives, scope, solution, risks). If a contract demands a BRS per 29148, add the "Not yet available" items above or state the reason for omitting them.

## StRS, clause 9.4 (18 items) → the skill's BRD and PRD
The StRS (stakeholder requirements specification) is the BRS's close relative: most of its items repeat 9.3, with "system" in place of "business". The differences: it has **no** "business structure" item (9.3.15), turns "business processes" into **system processes** (9.4.10), and adds **user requirements** (9.4.15), which is its main new content.
| Standard | Content | Place in the skill's frame |
|---|---|---|
| 9.4.2 | Stakeholder purpose: why the organization is pursuing the change, how the proposed system contributes to the business objectives | BRD §2 |
| 9.4.3 | Stakeholder scope: business domain by name, range of activities and external entities (showing what is outside is helpful), scope of the system and the assumptions about which activities it supports | BRD §4 |
| 9.4.4 | Overview: major internal divisions and external entities and how they relate (a diagram is recommended) | No place of its own; context diagram in BRD §4 |
| 9.4.5 | Stakeholders or classes of stakeholders and how they relate to development and operation | BRD §5 |
| 9.4.6 | Business environment: external and internal factors (market trends, laws and regulations, social responsibility, technology base) | Partly BRD §2; **not separated** |
| 9.4.7 | Mission, goals and objectives: business results the system should obtain | BRD §3 |
| 9.4.8 | Business model: how the goal is expected to be reached (products and services, geographies, channels, partners, finance and revenue model; the standard's note points to the OMG Business Motivation Model) | **Not yet available** |
| 9.4.9 | Information environment: project portfolio, long-term system plan, organization-level database configuration, treated as constraints | **Not yet available** |
| 9.4.10 | System processes: how, and in what context, the system supports the business activities; each named and numbered, shown as a sequence of activities | No place in the BRD; process models are in SRS §3 / `requirements-modelling` |
| 9.4.11 | System operational policies and rules: how the business rules will be addressed in the functional requirements of the SyRS and SRS; named, numbered, referenced from the business processes | SRS §5 (business rules); the BRD has none |
| 9.4.12 | Operational constraints: conditions and functional requirements imposed on the system while it carries out the business process (may lead to performance requirements) | BRD §10 (not separated) |
| 9.4.13 | Operational modes and states | **Not yet available**; state models come from `requirements-modelling` |
| 9.4.14 | System operational quality: required quality level (performance, compatibility, reliability, security, maintainability, portability); points to ISO/IEC 25010 | BRD §6 or business-level NFRs from `nfr-writer`. Note: the 2018 text uses the 2011 characteristic names (for example "portability"); the skill uses ISO/IEC 25010:2023 names (Flexibility replaces Portability) |
| 9.4.15 | User requirements: requirements for use that are the basis for design and evaluation: use-related quality (including usability), user-system interaction requirements, constraints on design freedom; the **context of use** must be stated; usability objectives are measurable effectiveness, efficiency, satisfaction | BRD §7 (summary); detail in PRD §2 and §5 (`story-writer`, `requirements-elicitation`). **Context of use is not separated** |
| 9.4.16 | Operational concept: high level, without design detail: policies and constraints, description of the proposed system, modes of operation, user classes and other personnel, support environment | BRD §9 (approximately) |
| 9.4.17 | Operational scenarios: examples of how users, operators and maintainers interact with the system in important contexts of use; named, numbered, referenced from the business processes in 9.3.10 | **Not yet available**; scenarios and use cases from `requirements-modelling` |
| 9.4.18 | Other detailed concepts: acquisition, deployment, support, retirement | BRD §8 (partly) |
| 9.4.19 | Project constraints (cost and schedule), "if appropriate" | BRD §10 |
Consequence: for an StRS, the BRD alone is not enough; **BRD + PRD together** cover most of it (the PRD carries users and requirements). Missing: business model, information environment, modes and states, operational scenarios, context of use.

## SyRS, clause 9.5 (18 items, some with sub-clauses) → the skill's SRS
The SyRS describes a **system** (software plus hardware, people, environment), while the skill's SRS frame is built for software. Software-only products can answer most items; for the hardware- or physical-oriented ones, record "not applicable: software-only product" explicitly instead of leaving them out silently.
| Standard | Content | Place in the skill's SRS |
|---|---|---|
| 9.5.2 | System purpose: why the system is developed or modified | §1 |
| 9.5.3 | System scope: system named; the earlier needs analysis stated as a brief, clear expression of the user's problem; what the system will and will not do; application, top-level benefits, objectives and goals | §1 (add a short problem statement and a will / will-not list) |
| 9.5.4.1 | System context: major elements including human elements and how they interact, with diagrams, all significant interfaces crossing the boundary | §2 and §6; context diagram |
| 9.5.4.2 | System functions: major capabilities, conditions, constraints | §4 (summary paragraph at the head) |
| 9.5.4.3 | User characteristics: each type of user, operator, maintainer (by function, location, device type), number in each group, nature of use, capabilities. The note says to keep them consistent with the SRS | §2 (actors); user characteristics not separated |
| 9.5.5 | Functional requirements applicable to system operation | §4 |
| 9.5.6 | Usability and quality in use: measurable effectiveness, efficiency, satisfaction, avoidance of harm in specific contexts of use | §7 |
| 9.5.7 | Performance: dynamic actions, endurance and life expectancy, operational session duration and planned utilization rate, performance per operational phase and mode | §7 (endurance and life expectancy mostly concern equipment) |
| 9.5.8 | System interfaces: among system elements (including the human element) and with external entities (including other systems); interdependencies and constraints such as protocols, special devices, standards, fixed formats; bidirectional flows | §6 |
| 9.5.9.1 | Human system integration: allocation of functions to personnel, personnel-equipment interaction, areas where human error would be especially serious | **Not yet available**; partly §7 (user error protection) |
| 9.5.9.2 | Maintainability, in quantitative terms: time, rate, complexity, maintenance action indices, accessibility of components | §7 |
| 9.5.9.3 | Reliability, in quantitative terms with the conditions under which it must be met; may include an apportionment model | §7 |
| 9.5.9.4 | Other quality requirements: compatibility, portability | §7 |
| 9.5.10 | System modes and states, with diagrams where appropriate | §3 (state models) |
| 9.5.11.1 | Physical requirements: weight, volume, dimensions, construction, materials, markings | Not applicable to software-only; record it |
| 9.5.11.2 | Adaptability: growth, expansion, capability, contraction | §7 (scalability) |
| 9.5.12 | Environmental conditions: natural, induced, electromagnetic, self-induced, threat, cooperative; also legal/regulatory, political, economic, social and business environments | Physical conditions: not applicable to software-only; record it. Legal and business environment: §2 |
| 9.5.13 | Security: the facility housing the system and the operational security of the system (access limits, log-on, data protection and recovery) | §7 |
| 9.5.14 | Information management: types and amounts of information received, stored, exported; protections on it; backup and archiving | §8 |
| 9.5.15 | Policy and regulation: requirements derived from organizational policies and external regulations (multilingual support, labour policies, protection of personnel information, health and safety) | §2 (constraints), §5, §7; legal items via `nfr-writer` |
| 9.5.16 | Life cycle sustainment: quality activities, support facilities, spares, technical documentation, training, initial support | §9 (partly); **not separated** |
| 9.5.17 | Packaging, handling, shipping, transportation, storage | Not applicable to software-only; record it |
| 9.5.18 | Verification: approaches and methods planned, preferably in parallel with 9.5.5 to 9.5.17 | §10 |
| 9.5.19 | Assumptions and dependencies to be considered when allocating and deriving lower-level requirements | §2 |
Consequence: a software-only product covers most of the SyRS with the existing SRS frame. The gaps are human system integration, life cycle sustainment, user characteristics and the explicit "not applicable" records. A hardware or embedded system needs the physical, environmental and packaging items filled by the people who own them; the skill cannot invent them.

## SRS, clause 9.6 (19 items) → the skill's SRS
| Standard | Content | Place in the skill's SRS |
|---|---|---|
| 9.6.2 | Software purpose | §1 |
| 9.6.3 | Scope: product name, what it does, applications and benefits, **consistent with higher-level specifications** | §1 (add a sentence checking consistency with the higher-level document, if any) |
| 9.6.4 | Product perspective: relation to other products/systems; constraints on system, user, hardware, software, communication interfaces; memory; operations (including backup and recovery); site adaptation; interfaces with services (SaaS, cloud) | §2 and §6; **not yet available**: memory, special operations, site adaptation |
| 9.6.5 | Product functions: a summary of the main functions; use cases, user stories, scenarios can also be used | §4 (should have a summary paragraph at the head of the section) |
| 9.6.6 | User characteristics (level, experience, disabilities, expertise); describes the reasons for the later requirements, **not requirements** | §2 (actors); user characteristics not separated |
| 9.6.7 | Supplier limitations: regulations, hardware, interfaces, parallel operation, audit, safety and security, etc. | §2 (constraints) |
| 9.6.8 | Assumptions and dependencies: factors that change the requirements if they change, not design constraints | §2 |
| 9.6.9 | Allocation of requirements to software elements; state requirements that can be deferred to a later version | **Not yet available**; the "deferred" part could use the Priority/phase column |
| 9.6.10 | Specific requirements: per the characteristics in 5.2, cross-references to the previous version, unique identification, describe all inputs, outputs, functions | §4 |
| 9.6.11 | External interfaces: name, purpose, source/destination, range of values/accuracy, units, timing, relationships, data and command formats, data items | §6 (the skill's interface table lacks: value range, units, format) |
| 9.6.12 | Functions: input validation, sequence of operations, response to abnormal situations (errors, recovery), effect of parameters, output-input relationships and formulas | §4, §5 |
| 9.6.13 | Usability and quality in use (measurable effectiveness, efficiency, satisfaction, freedom from harm) | §7 |
| 9.6.14 | Performance: static figures (concurrent users, data volume), dynamic (transactions over time, normal and peak load); must be measurable | §7 |
| 9.6.15 | Logical database: kinds of information, frequency of use, access rights, entities and relationships, integrity constraints, security, retention | §8 |
| 9.6.16 | Design constraints from external standards, regulations, the project | §2 |
| 9.6.17 | Standards compliance: report formats, data naming, accounting, audit trail | §7/§8 (data and legal obligations); no section of its own |
| 9.6.18 | Software system attributes (examples named: reliability, availability, security, maintainability, portability). The standard says this is a partial list, and a requirement should not be put in merely because it is "good design" | §7 |
| 9.6.19 | Verification: approach and methods, preferably in parallel with 9.6.10 to 9.6.18 | §10 |
| 9.6.20 | Supporting information (data samples, survey results...); must state clearly whether it is part of the requirements | §11 |
Note when using: 9.6.6 and 9.6.20 stress that the descriptive parts are **not requirements**; when assembling, mark clearly which paragraphs are description and which are requirements.

## How to use in the skill
- When creating a BRD/SRS for a user with no mandatory template: use the skill's frame as before; do not say it is "per 29148".
- When the user says it must follow 29148: choose the right document first (BRS 9.3, StRS 9.4, SyRS 9.5 or SRS 9.6; ask which one the contract names), then run its table above as a checklist, list the "Not yet available" content, ask whether the user wants to add it or record the reason for omitting it; annotate the document "content was compared with clause 9.x of ISO/IEC/IEEE 29148:2018 (state which); the person responsible for compliance must confirm".
- When writing each requirement sentence: use the keyword convention and the list of words to avoid in the `requirements-review` skill (its 29148 reference), if installed; otherwise ask the user which keyword convention the project uses.
