# Review techniques and roles (BABOK 10.37, pp. 326–329; paraphrased)

The three dimensions of a review session: objective, technique, participants. The objective must be communicated to everyone **before** the session.

## Objectives (10.37.3.1)
Find defects; check compliance with a standard; ensure completeness and correctness; build consensus on direction; answer questions, solve problems, explore options; educate readers; measure product quality.

## Techniques (10.37.3.2)
| Technique | Formal? | How | Suits when |
|---|---|---|---|
| Inspection | Yes | Overview, each person examines individually, logs defects, consolidation, tracks fixes | Critical work products, defect-finding objective; usually peers, also used for stakeholders |
| Formal walkthrough (team review) | Yes | Individual examination + group consolidation | Peers or stakeholders |
| Single issue review (technical review) | Yes | Examine one issue or one standard closely first, then meet to resolve | A specific point (for example compliance with one standard) |
| Informal walkthrough | No | The BA presents a draft and asks for comments; viewers prepare little | Work in progress |
| Desk check | No | One person who did not take part in writing reads it and gives spoken/written feedback | Fast, economical |
| Pass around | No | Several people comment in turn or on a shared copy | Many people, different times |
| Ad hoc | No | Ask a colleague to take a look | Very light |
Limits named by BABOK: a rigorous review costs effort, so reserve it for critical work products; a light review with one or two people gives less assurance; with desk check/pass around it is hard to know whether the viewer really looked; feedback by email gets messy when disagreement needs resolving.

## Roles (Table 10.37.1)
- **Author**: answers questions, listens to feedback, fixes after the session.
- **Reviewer**: a peer or stakeholder; examines before the session and records defects, suggestions (for a defect-finding review).
- **Facilitator**: neutral (preferably not the author), keeps the session on objective, ensures each part is discussed, checks that viewers prepared.
- **Scribe**: neutral, good communication skills, records defects, suggestions, issues, open questions.
If senior people take part, the facilitator watches that others are not discouraged from speaking honestly.

## Suggestions for choosing (the skill's own)
- Contract specifications, legal requirements, security NFRs: inspection or formal walkthrough.
- A story for the next sprint: informal walkthrough with dev and tester (the BABOK Agile Extension says the three parties look at examples together, see story-writer).
- A rule to be settled with legal: single issue review.
- A first draft: desk check.
## Structure of a session (suggested, following the steps of BABOK 10.37.2)
Overview of the product and objective; documents and checklist sent beforehand; examination and recording of findings; consolidation meeting; verification of fixes. Results go into item tracking.
