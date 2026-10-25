# Data models, concept models, data dictionary

## Concept model (BABOK 10.11, pp. 245–246; paraphrased)
Start from a glossary of the core nouns of the domain; prefer definitions independent of design, not biased towards data or technology; a rich vocabulary to express rules in natural language. Noun concepts are connected by standard verb phrases (verb concepts) to serve as building blocks of rule sentences. Suits when: knowledge needs organizing, there are many rules, stakeholders are put off by the "technical" feel of a data model, the domain is regulated. **Different from a data model**: the goal is semantics, not consolidating and simplifying data.

## Data model (10.15, pp. 256–260)
- Three levels: **conceptual** (technology-independent, business vocabulary), **logical** (normalized, tied to the solution design), **physical** (database organization, performance, concurrency, security). BAs usually do the conceptual one; logical/physical is for the implementer.
- Elements: **Entity/Class** (physical, organizational, abstract or an event; BABOK's example: Appointment; each instance has a unique identifier), **Attribute** (name, valid values/meaning, description; detail lives in the data dictionary; permitted values may come from business rules), **Relationship** (and **cardinality**: the minimum and maximum number of occurrences on each side, usually 0, 1, many; read in both directions: "each X relates to (min, max) Y"), **Diagram** (ERD or class diagram), an object diagram illustrates real instances with sample values.
**How to do it with the skill**
1. List the nouns from the glossary/documents; remove those that are attributes or synonyms.
2. For each entity: identifier, main attributes.
3. Ask about relationships in both directions and multiplicity (can one booker have several appointments? can one appointment have several patients?). Unknowns: "?".
4. Add a concrete example (an object diagram as a table of sample values) so experts can check it easily.
**Check**: every entity has an identifier; every relationship has multiplicity in both directions; no attribute duplicated in two entities; the entities in the model appear in the process/stories/BR and vice versa; names match the glossary.
**Security/legal warning**: mark entities and attributes that are personal or sensitive data and hand them to `nfr-writer` (do not assign a sensitivity level by law yourself).

## Data dictionary (10.12, pp. 247–250)
Standardizes the definitions of data elements and permitted values; usually accompanies an ERD, can be extracted from the data model; can be a spreadsheet.
- A **primitive element** records: Name (unique), Aliases (names stakeholders use), Values/Meanings (a list of values or a format, number of characters; abbreviated values must be explained), Description.
- A **composite element** uses: Sequence (order, the + symbol), Repetition, Optional.
BABOK example: Customer Name = First Name + Middle Name + Family Name.
**Suggested columns**: Name | Aliases | Type (primitive/composite) | Values/format | Mandatory | Description | Source/related rule (BR) | Personal data note.
**Check**: names are unique; composite elements contain only defined elements; abbreviated values are explained; no definition contradicts the glossary.
