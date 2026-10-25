# Process model and state model

## Process (BABOK 10.35, pp. 318–322; paraphrased)
**Purpose**: show how work is done; the foundation of process analysis. It can describe the current state (as-is: to agree on what is happening) or the future (to-be: to agree on what should happen).
**Minimum**: a triggering event, a sequence of activities, an outcome. Add: participants (roles), manual and automated activities, paths and decision points, input/output data, annotations.
**Elements**: Activity (can be a sub-process), Event (triggering, interrupting or ending; can be a message, time, condition), Directional flow, Decision point (exclusive or parallel branching, or where flows merge), Link (connects to another process), Role (matching the organization model).
**Levels**: context/enterprise (overview, relation to other processes), operational (activity detail, **all outcomes including exceptions and alternative paths**), system (a platform for simulation/execution).
**Common notations**: flowchart (suits non-technical people; add swimlanes to separate work by role, an informal extension), BPMN (industry standard, pools and swimlanes, handing over responsibility when the flow crosses a lane boundary), DFD and UML (the IT domain), IDEF/IGOE (setting scope), SIPOC and value stream.

**How to do it with the skill**
1. Ask the triggering event and the outcome first, then the activities in order, then the exceptions.
2. Assign each activity to exactly one role (lane). An activity whose performer is unclear: a "?" mark.
3. Every branching point has all its exits; branch conditions refer to a BR or a decision table.
4. as-is: label sources [Stated]/[Inferred]; to-be: show clearly what is new and what is kept.
**Check**: there is a trigger and an outcome; no orphan activity (no entry or no exit); every branch has an exit; no infinite loop without an exit condition; roles match the role list; terms match the glossary; common exceptions (mid-way cancellation, missing data, no capacity, overdue) have been asked about.
BABOK limits: useful for analysis, but must be kept up to date and does not replace rule analysis.

## State (BABOK 10.44, pp. 348–350; paraphrased)
**Purpose**: describe the possible states of an entity, how it moves between them, and what can happen to it in each state. Use when the entity has complex behaviour and rules and needs to be understood precisely and consistently. Complements the process: a process shows all the entities in one process; a state model shows one entity across all the processes that act on it.
**Elements**: State (name, activities performed there, rules, events it responds to; can be divided into sub-states); Transition (the event causing the move, a condition deciding whether it responds, an accompanying action; can be conditional or automatic; can skip states, return to a previous state, or return to itself); initial and final states; the state diagram; the **state table** (each row: initial state, transition, final state; one row per transition).
**How to do it with the skill**
1. Start with the **state table** to elicit state names and events with experts (BABOK says this is an easy way to start), and only then draw the diagram.
2. Ask: how the entity starts, how it ends; from each state, which events occur; who does them; under which conditions.
3. Ask separately about exceptions: cancel, undo, expiry, duplicate, override.
**Check**: there are initial and final states; every state is reachable and (except final states) can move on; each transition has an event; no two transitions with the same event and the same condition but different destinations; state names match the AC and the data; each state states the permitted actions.
From the model generate: AC for each state transition, BR for the transition conditions, and tests that probe every transition.
BABOK limits: only worth doing for complex entities; detailed consensus with experts is hard to reach; some people dislike the precise level of detail.
