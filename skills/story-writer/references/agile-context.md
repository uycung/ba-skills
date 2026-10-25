# Agile context, backlog, decomposition (BABOK 10.2, 11.1; Agile Extension v2 sections 7.1, 7.2, 7.4, 7.18–7.21; paraphrased)

## Story decomposition: breadth-before-depth (AE 7.18, pp. 95–98)
Product goal → MMF/component (the minimum set of features worth releasing, usually the theme of a release) → story → story with acceptance criteria. Do it progressively: at first identify the goal, the MMFs and most of the large stories; **decomposing to the finest level early is waste**. Only a story that is too large or not understood well enough to elaborate/estimate/deliver needs decomposing. Once the MMF exists, use cases can replace stories.
**Do not decompose by process (step 1, 2, 3), architecture (do the DB, server, front end) or procedure (design, build, test)**; decompose by features that have value to the customer. Warning: do not turn decomposition into "detailed requirements from the start"; know when to stop.

## Elaborating a story: just-in-time, just-enough (AE 7.19, pp. 98–99)
The lowest level of decomposition, done within the Delivery Horizon, for stories already identified as belonging to an upcoming iteration, usually through a workshop with SMEs, the person who needs the story, the person who will test it and a BA facilitating. Done to prepare for the Planning Workshop. Outputs: clearer acceptance criteria (added/removed/clarified), possibly examples and scenarios, low-level models (data, data flow), screen/report mock-ups, input/output data tables, tasks. The result is a shared understanding of the story's "Done" state. Risk: too early means eliciting again; too late blocks development.

## Backlog (BABOK 10.2, pp. 220–223; AE 7.1, pp. 57–58)
Items at the top: small enough and detailed enough to do in the next iteration; items at the bottom can be large and vague. Continuous refinement includes: elaborating, decomposing, prioritizing, ordering, splitting large items by INVEST, adding AC or needed documents; it is done when the team has enough information to carry the item out. There is a refinement meeting (usually led by the PO) and a **Definition of Ready**. Limits: out of step with the team makes it ineffective; with only a few attendees other viewpoints are missed; ineffective when the vision/roadmap keeps changing. A backlog item is usually a user story, but can be a job story or a wireframe.
=> In this skill: a story whose turn has not come is written only as a preliminary version, saying plainly that it is not elaborated.

## Job story (AE 7.4, pp. 64–65)
Template: "When <situation> I want to <motivation> so I can <expected outcome>" (or third person). The situation provides context; **do not name a persona** in the situation so the team looks at the real customer; **do not name a feature/solution** in the motivation. Suits cases where context and motivation matter (UX) and several roles complete the same job. Limits: longer than a user story; mixing the two kinds in a backlog easily causes confusion. They can be used together: the job story states motivation and outcome, the user story states the feature that solves it.

## BDD and examples (AE 7.2, pp. 59–61)
Concrete examples are the root for agreeing requirements. Gherkin: GIVEN <situation> (may use AND), **only one WHEN** <event>, THEN <result> (may use several ANDs). Scenarios can serve as acceptance criteria and automated tests. Ask "what if/what about" to expose other scenarios; hold a **Three Amigos** meeting (PO, tester, developer). The terms BDD, ATDD and Specification by Example are used interchangeably. Limits: scenarios are easily missed if nobody asks; with complex rules the number of scenarios explodes, so a tool or a decision table is needed; it must be kept up to date.

## Story map (AE 7.20, pp. 100–102)
A two-dimensional grid: horizontally the sequence of customer themes/activities over time; vertically the stories in priority order, allowing release slicing. Suits processes with a flow; it does not analyze dependencies between requirements (it only helps surface them); it does not suit contexts that are not process-based; it gets unwieldy when the solution is very large.

## Note on sources
INVEST is in AE v2 7.21 (see quality-checks.md). **Lightweight Documentation and MoSCoW** appear in the technique table of BABOK v3 section 11.1.2 but were **dropped from Agile Extension v2** (appendix D), so there is no detailed description in any source we have.
