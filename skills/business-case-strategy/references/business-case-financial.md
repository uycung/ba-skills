# Business case and financial analysis

## Business case (BABOK 10.7)
Justifies a course of action based on benefits relative to cost, effort and other considerations; records the reason for making the change; can be formal or informal. **The effort put into the business case is proportional to the size and importance of the potential value.** Detailed enough to inform and to ask for approval, with no need for implementation detail. Used to: define desired outcomes, assess constraints/assumptions/risks, recommend a solution.
| Part | Content |
|---|---|
| Need | Related objectives/targets, tied to strategy; the problem or opportunity |
| Desired outcomes | Measurable, **independent of the solution**, reviewed at milestones and at the end |
| Options | Technology, process, business model; how to obtain; timing; **includes a do-nothing option** |
| For each option | Scope (in/out); organizational feasibility (knowledge, skills, capability) and technical feasibility (technology maturity, experience); assumptions, risks, constraints; financial analysis and value |
| Recommended solution | Detailed enough for the decision-maker to understand; cost and time estimates if available; measurable benefits/outcomes to evaluate after deployment |
Strengths: gathers the facts, problem and analysis for a decision; detailed financial analysis; guides decisions throughout the initiative. Limits: can suffer from the author's bias; often not updated after funding is granted; assumptions about cost and benefit may be wrong.
**Skill rule**: record the date and owner of each assumption; suggest a schedule for reviewing the business case at milestones.

## Financial analysis (BABOK 10.20)
Purpose: understand the financial aspects of an investment/solution; compare options by upfront cost and when it is incurred, expected financial benefits and when, ongoing operating/support costs, the risk of the change, and ongoing risks to value. **Several techniques** are usually used because each is a different viewpoint. It should keep being applied throughout the initiative; it may recommend adjusting or stopping when new information means the results no longer support it.
- **Cost of change**: building or buying the solution, and moving the organization from the current to the future state (equipment, software, facilities, staff, contract buy-outs, subsidies, penalties, data conversion, training, communication, deployment).
- **TCO** (total cost of ownership): acquisition cost + usage cost + support cost over the expected period. Equipment has a standard lifetime; processes and software are usually unclear, so many organizations assume a standard period (for example 3 to 5 years is BABOK's example).
- **Cost-benefit**: total expected benefits minus total expected costs = net benefit (planned value). State the assumptions and estimation method so others can review, challenge and approve. The period must be long enough for the solution to be fully used and the value to be achieved.
  Sample table by year (BABOK Table 10.20.1): benefits (revenue, lower operating cost, time saved, lower error cost, more customers, etc.), costs (project, ongoing support, facilities, licences, infrastructure renewal), total net benefit, cumulative net benefit. Cumulative net benefit can be negative for a while; some organizations require costs to be allocated over several years.
- **ROI** = (Total benefits − Investment cost) / Investment cost, expressed as a percentage; a higher ROI is better; compare investments **over the same period**.
- **Present value (PV)** = the sum of net benefit of each period / (1 + that period's discount rate), added over all periods; it does not count the original investment cost. The **discount rate** is usually set as a standard by finance; sometimes a higher rate is used for distant periods because uncertainty is larger.
- **NPV** = PV − investment cost; a higher NPV is better.
- **IRR**: the interest rate at which NPV equals zero; compared with the organization's minimum required threshold (hurdle rate); if IRR < hurdle, do not invest; compare IRR between options over the same period. IRR is internal to one organization and does not account for inflation, interest-rate movements or a changing context.
- **Payback period**: the time needed to recover the cost of the change, independent of the discount rate; **there is no standard formula** (BABOK says so explicitly); `fin.py` interpolates linearly within the year. Say so when returning results.
- Limits: not every cost/benefit can be converted to money; the analysis looks to the future so it is always uncertain; a positive figure can create a false sense of safety; a positive figure does not tell you enough about the initiative.

## How to use `scripts/fin.py`
1. Ask the user for: the list of years (0..n), benefits and costs for each year (each line with a source or an assumption label), the discount rate set by finance.
2. Build an `input.json` file matching the format in the script; run `python3 scripts/fin.py input.json`.
3. Present: the table by year, ROI, NPV, IRR, payback, sensitivity (NPV at ±5 percentage points of the discount rate).
4. Recommend extra sensitivity on the largest assumption (benefits −20%, costs +20% are examples of the skill's sensitivity, **not a standard level**; ask the user which scale suits).
5. Always include: the assumptions, the period, the types of cost/benefit left out of the calculation, and the sentence "this analysis supports decision-making and is not investment advice".
6. Script conventions: Year 0 is usually the upfront cost. The NPV in the script adds up all periods including year 0 (equivalent to the PV of later periods minus the original investment cost when that cost sits in year 0). ROI uses the total cost over the whole period as the denominator.
