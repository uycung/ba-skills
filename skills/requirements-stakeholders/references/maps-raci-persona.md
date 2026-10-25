# Maps, RACI, persona

## Stakeholder matrix (BABOK 10.43.3.2)
Two axes: the stakeholder's **influence**; **interest** (as the text describes it) or **impact on the stakeholder** (the label in the figure of the guide). The text of section 10.43 says the matrix maps influence against interest, while the legend of the four corners uses "impact". When using it, choose one axis and tell the user which one you chose.
The four corners (paraphrased):
| Influence | Interest/impact | How to work with them per BABOK |
|---|---|---|
| High | High | Key players: concentrate effort, engage frequently, work closely so they agree to and support the change. |
| High | Low | Have needs to be met: consult, keep them satisfied, find ways to raise their interest. |
| Low | High | Supporters and potential goodwill ambassadors: gather their views, show concern for their needs; they may be anxious about lack of control so they need to be informed. |
| Low | Low | General information; monitor to make sure interest or influence has not changed; extra engagement can move them to the supporter group. |
How to do it: place each stakeholder/group in a cell with a source label. A position is a judgment: tag it [Inferred] unless confirmed. A single "?" is also acceptable.

## Onion diagram (10.43.3.2)
The rings from inside out (paraphrased): **Solution** (the delivery team and the people who directly create the solution) → **Affected units** (end users, support, people whose work changes) → **Organization/enterprise** (sponsor, leadership, business experts, people who interact with the affected units) → **External** (customers, suppliers, regulators). Use when you want to see closeness to the solution and organizational boundaries.
It can be sketched quickly in Mermaid (a drawing tool, not BABOK notation) or as a 4-row table.

## RACI (10.43.3.3)
- **R** (Responsible): the person who does the work.
- **A** (Accountable): the person ultimately answerable who decides; **only one person**.
- **C** (Consulted): asked for input, two-way, usually SMEs.
- **I** (Informed): kept updated, one-way (BA to stakeholder).
Process: (1) make sure all stakeholders are present; (2) list the activities/deliverables; (3) assign R/A/C/I; (4) **define the letters** in the document so that everyone understands them the same way; (5) confirm with the parties.
Check: each row has exactly one A and at least one R; no row is all C/I; a stakeholder with no cell at all should be reviewed to see whether they belong in the list; one person is not both R and A for every row (a sign of overload).
This RACI is at the initiative level. The system-level CRUD permission matrix belongs to `requirements-modelling` (10.39).
The BABOK example is a RACI for the change-request process (sponsor, BA, project manager, developers, testers...).

## Persona (BABOK 10.43.3.4; Agile Extension 7.7)
- A persona is a fictional character that represents how a typical user uses the solution, but it is built from research on real user groups (interviews, surveys), so it rests on understanding rather than opinion. Write it as a narrative focused on the group's goals.
- Short form (one page): name, background/details, tasks and responsibilities, technology used, characteristics (age, job, residence), goals. The long form adds buying motives, demographics, characteristics, needs, drivers, differentiators (Agile Extension 7.7.3).
- Personas are ranked to see who benefits most from the design (7.7.2).
- Needs are finite while wants are infinite: record specific needs, not generic wants (7.7.3.5).
**Rules of this skill**:
- Write a persona only when there is data. Every field carries a source (number of interviews, surveys). Without data: the label "Hypothesis" + a validation plan.
- Do not use sensitive information (health, religion, etc.) unless it relates directly to the need and consent exists.
- Different personas must differ in their **differentiators**; otherwise merge them.
- Do not equate a persona with a system role (authorization); a persona is about people and needs.
