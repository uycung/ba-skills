# Types of traceability relationships

Per BABOK v3 section 5.1.4.2 (pp. 81–82), paraphrased; read from the copy supplied by the user.
| Relationship | Meaning | Example |
|---|---|---|
| Derive | This requirement arises from the other one, usually at a different level of abstraction | FR-05 derives from GOAL-02 |
| Depends | This requirement needs the other one. Two kinds: necessity (only meaningful if the other is also done) and effort (easier to do if the other is also done) | US-14 depends on US-09 (necessity) |
| Satisfy | An implementation component satisfies a requirement | A module/API satisfies FR-05 |
| Validate | A test case or other element determines whether the solution meets the requirement | TC-31 validates AC-12.2 |

Typical chain: GOAL → (derive) FR/US → (derive) AC; NFR → (derive) from a GOAL or from a law/standard; BR → (support) FR/US; TC → (validate) AC/NFR; component → (satisfy) FR/US/NFR.
The "support" relationship between a business rule and a requirement is an extension based on BABOK 5.1.6 (the Business Rules Analysis technique is used to trace rules to requirements); it is not an official relationship type in the list above.
