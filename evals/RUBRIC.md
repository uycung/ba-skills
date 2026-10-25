# Manual rubric

Scored by a person, **after** `grade.py` has run. These are the judgements a script cannot make. Each criterion is scored 0 or 1; write the scores in `<outdir>/manual.json` (the grader creates the empty sheet). Automatic results live in `<outdir>/automatic.json` and are never mixed with these scores.

How to score: read the output next to the fixture, answer the question in "Score 1 when", and score 0 if you hesitate. Note the reason in a `notes` field if you want to keep it.

| ID | Skill | Score 1 when |
|---|---|---|
| SW-1 | story-writer | The role and the value fit the input; neither is filler that merely passes the check for "not generic". |
| SW-2 | story-writer | A tester could write one test per acceptance criterion without asking anybody (the script only rules out vague words and invented numbers). |
| SW-3 | story-writer | The questions in To clarify are the ones that block building, not trivia, and are no more than needed. |
| SW-4 | story-writer | Business rules are kept apart from operation steps and named by code, and no rule is hidden inside an AC. |
| SW-5 | story-writer | The reply reads naturally in the user's language, with no filler sentences. |
| RR-1 | requirements-review | Each finding names the right characteristic and the "why" is true for that exact sentence. |
| RR-2 | requirements-review | Proposed rewordings keep the business meaning and fill no missing information. |
| RR-3 | requirements-review | Each severity level follows the stated criteria and the verdict conditions are specific enough to act on. |
| RR-4 | requirements-review | The defect/suspicion split is justified: suspicions are the ones that need a business answer. |
| RR-5 | requirements-review | Each question names a sensible person to ask. |
| RT-1 | requirements-trace | Every link in the matrix has a basis in the text; proposed links are marked as proposed. |
| RT-2 | requirements-trace | Gaps are ordered by severity and each proposal says what to do, not only what is wrong. |
| RT-3 | requirements-trace | The contradiction or the refused link is explained so that the owner can decide (who, what). |
| RD-1 | requirements-document | Connecting sentences add no requirement, number or fact that is not in the package. |
| RD-2 | requirements-document | Requirements are classified correctly (business, stakeholder, solution functional or non-functional, transition). |
| RD-3 | requirements-document | Each missing item names who or which skill can supply it. |
| RD-4 | requirements-document | The consistency findings are correct and a reader could act on them. |
