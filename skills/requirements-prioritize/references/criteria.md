# Prioritization criteria and methods

## Criteria (BABOK 5.3.4.1, pp. 88–89; paraphrased, read from the copy supplied by the user)
| Criterion | Question |
|---|---|
| Benefit | What advantage does it give stakeholders, measured against the objective of the change? Which group benefits? |
| Penalty (consequence of not doing it) | What is lost if it is not done (both regulatory penalties and customer experience)? |
| Cost | Effort and resources needed? (figures from the delivery team/vendor) |
| Risk | Likelihood of not producing value or not being achievable (difficulty, stakeholders not accepting)? High technical-risk items may be done early to learn early |
| Dependencies | Does it depend on other requirements, or on decisions/resources outside the project? |
| Time sensitivity | Is there a "best before" date (market launch, seasonality)? |
| Stability | How likely the requirement is to change; if unstable it may get low priority to avoid rework |
| Regulatory/Policy compliance | Mandatory by regulation/policy? May outrank other benefits |

## Ways of arranging (BABOK 10.33.3, p. 313)
- **Grouping**: place in high/medium/low groups, as an attribute of the requirement.
- **Ranking**: order from most important; use when a clear order is needed (backlog).
- **Time boxing/Budgeting**: prioritize against fixed resources (time or budget), used when there is a fixed deadline.
- **Negotiation**: reach consensus among stakeholders.

## Common additional frameworks (not in the BABOK sections that were read; use as discussion tools, not as a standard)
MoSCoW (Must/Should/Could/Won't), RICE, value–effort matrix. When using them, say plainly that they are additional frameworks and explain how scoring works.

## Challenges and biases (BABOK 5.3.4.2 and 10.33.4)
Stakeholders find it hard to accept that their item ranks low, so trade-offs are hard; they may adjust what they declare to influence the result; the solution team may exaggerate complexity; without KPIs/data the assessment is subjective. Ways to reduce this: criteria agreed beforehand, a written reason for each score, several viewpoints, and cost estimates checked with a second person.

## Additions from the BABOK sections read later
- **Multi-phase backlog (10.2.3, p. 221)**: when an item first enters the backlog only a broad high/medium/low group is needed; high items are reviewed more often; only to tell high items apart do you move to a numeric ranking against a value measure. Items at the top are described and estimated in more detail. The backlog is reviewed periodically and the trend in its size is watched (growth may come from rising demand or falling productivity). There can be several backlogs (global and near-term).
- **The four ways in 10.33 (pp. 311–313) mapped onto the process**: Grouping (high/medium/low, an attribute of the requirement); Ranking (an ordered list, for example a product backlog); Time boxing/Budgeting (fixed resources, used when there is a fixed deadline or steady improvement); Negotiation (consensus among stakeholders). Choose by audience and need; the approach can change when the context changes.
- **Factors when assessing a change (5.4.4, p. 93)**: benefit, cost (including rework and opportunity cost), impact (number of customers/processes), schedule, urgency (including regulation, safety). Use when re-prioritizing because a requirement changed.
- **MoSCoW**: BABOK v3 section 11.1.2 lists it (must, should, could, won't have), but Agile Extension v2 has **dropped** this technique, so there is no detailed source in the documents we have; use it as a common framework and define each group explicitly. RICE is not in BABOK.
- **Kano (AE 7.5, pp. 66–69)**: classifies features as threshold (absence causes strong dissatisfaction, presence does not raise satisfaction much), performance (the more, the more satisfied, close to linear), excitement (exceeds expectations, customers do not yet know they want it), indifferent (no value). Ask two forms of question: "how do you feel if the feature is present" and "if it is absent", each with five levels (like, expect, neutral, tolerate, dislike), and read the pair against the table to get E/P/T/I/Q/R. Limits stated by AE: it measures only satisfaction, so combine it with other factors when ordering the backlog; classification changes over time (excitement becomes threshold).
- **MVP (AE 7.6, pp. 69–71)**: the smallest set of requirements that can validate a hypothesis and give early feedback. Steps: identify the problem and hypothesis, choose the minimum feature set to test, analyze what was learned. You need: the target group and early adopters, a hypothesis/goal, a way to measure what is learned, and the minimum requirements. Limits: there is no formula, the number of features is a judgment; it does not suit cases where the solution is already clear and simple (then the MVP is simply the full product).
- **Persona (AE 7.7)**: rank personas to see which group benefits most, then prioritize features by how well they meet that persona's needs.
- **Approval**: a priority order is only valid when someone with authority approves it (5.5); unresolved conflicts must be recorded as risks.
