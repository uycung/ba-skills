# Stakeholder register template and example

Labels: [Stated] (source is explicit), [Inferred], [Assumption]. The example below is assumed, for illustration.

## Register
| ID | Person/group | BABOK role | Role in the initiative | Attitude | Decision authority | Influence | Interest/Impact | Source | To clarify |
|---|---|---|---|---|---|---|---|---|---|
| SH-01 | Operations Director (sponsor) | Sponsor | Accountable for the initiative, approves the budget | Supportive [Inferred] | Approves scope and budget [Stated] | High [Inferred] | High [Inferred] | Meeting notes 12/10 | Who stands in when absent? |
| SH-02 | Receptionists (group of 5) | End user | Use it daily to book and change appointments | ? | None [Inferred] | Low [Inferred] | High [Inferred] | Process diagram | Who represents the group? |
| SH-03 | SMS provider | Supplier | Sends appointment reminders | ? | None | Low [Inferred] | Low [Inferred] | Contract | Sending limits? |
| SH-04 | (unknown) | Regulator | Rules on customer data | ? | ? | ? | ? | Legal documents | Who is in charge of legal? |

BABOK roles that do not exist in the project: write "not applicable" + the reason.

## Matrix (influence × interest)
| | Low interest | High interest |
|---|---|---|
| High influence | | SH-01 |
| Low influence | SH-03 | SH-02 |

## RACI (example for "Approve a change request")
Definitions: R does the work; A is ultimately accountable and decides (only one); C is consulted (two-way); I is informed (one-way).
| Activity | SH-01 Sponsor | BA | PM | Dev lead | Tester | Receptionist |
|---|---|---|---|---|---|---|
| Assess change impact | I | R | C | C | C | I |
| Approve the change | A | R | C | C | I | I |
| Announce the change | I | R | A? | I | I | I |
(Row 3: needs confirmation of who is A.)

## Engagement plan
| Group | Purpose | Activity | Frequency | Means | Owner |
|---|---|---|---|---|---|

## Communication plan
| Information | Audience | Means | Frequency | Level of detail | Sender |
|---|---|---|---|---|---|

## Stakeholder risks
| ID | Condition | Consequence | Likelihood | Impact | Proposed response | Owner who watches |
|---|---|---|---|---|---|---|

## Open questions and change history
