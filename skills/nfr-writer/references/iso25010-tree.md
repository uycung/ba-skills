# ISO/IEC 25010:2023 tree: 9 characteristics, 40 sub-characteristics

The names of the characteristics and sub-characteristics match the 2023 edition. The "Meaning" column is the skill's paraphrase, **not checked against the official definitions** (the full text is behind a paywall). Quality in use has moved to ISO/IEC 25019:2023 and is not part of this tree. The compilation file of the 40 sub-characteristics supplied by the user describes itself as "official definitions" but gives no clause citations; its names were compared with this table (the structure matches), but the definition sentences in that file remain an unverified secondary source, so the "Meaning" column was not replaced.
Changes from the 2011 edition: Safety added, Interaction capability split out (replacing Usability), Flexibility (replacing Portability), "faultlessness" instead of "maturity", "resistance" instead of "integrity" under Security, scalability and other new sub-characteristics added.

## 1. Functional suitability (3)
| Sub-characteristic | Meaning (paraphrased) | Suggested NFR question |
|---|---|---|
| Functional completeness | Whether the functions cover all the tasks that need to be done | What share of use cases/tasks is covered? |
| Functional correctness | Results are correct and sufficiently accurate | Permitted error? Which calculation rules must be 100% correct? |
| Functional appropriateness | The functions help complete the task the right way, with no superfluous steps | Maximum number of steps for the main task? |

## 2. Performance efficiency (3)
| Sub-characteristic | Meaning | Suggested question |
|---|---|---|
| Time behaviour | Response time, processing time, throughput | Which percentile, at what load, on which device/network? |
| Resource utilization | Amount of CPU, memory, battery, bandwidth | Resource ceiling? Battery consumption on mobile? |
| Capacity | The maximum limit the system can bear | Concurrent users, transactions per second, data volume? |

## 3. Compatibility (2)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Co-existence | Runs in the same environment as other products without affecting each other | Which systems share the infrastructure? |
| Interoperability | Can exchange data with other systems | Which standards, API versions, formats? |

## 4. Interaction capability (8)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Appropriateness recognizability | Users can recognize whether the product fits their needs | Share of new users who understand the purpose within N seconds? |
| Learnability | Quick to learn to use | Time / completion rate of a first-time task? |
| Operability | Easy to operate and control | Number of actions, keyboard/touch support? |
| User error protection | Prevents, detects, and helps correct user errors | Confirmation of dangerous actions, undo? |
| User engagement | An attractive interface that keeps users engaged | Which engagement indicators must be reached? |
| Inclusivity | Usable by many different groups of users | WCAG level? Languages? Users with disabilities? |
| User assistance | Help is available when users need it | Contextual help, support channels? |
| Self-descriptiveness | The interface explains itself | Are messages, labels and system status clear? |

## 5. Reliability (4)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Faultlessness | Works correctly, with few faults under normal conditions | Defect density, target MTBF? |
| Availability | Available when needed | SLO %, measurement window, are maintenance windows excluded? |
| Fault tolerance | Keeps running when a component fails | Which single points of failure are acceptable? |
| Recoverability | Recovers after an incident | RTO, RPO, frequency of recovery tests? |

## 6. Security (6)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Confidentiality | Only authorized people can access | Data classification, encryption at rest/in transit? |
| Integrity | Prevents unauthorized modification | Integrity controls, signatures, audit? |
| Non-repudiation | Actions cannot be denied | Which actions need evidence? |
| Accountability | Actions trace back to the actor | What logs, retained for how long? |
| Authenticity | Identity/origin is authenticated | Authentication method, MFA? |
| Resistance | Withstands attack | ASVS level? OWASP list? Time to patch vulnerabilities? |

## 7. Maintainability (5)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Modularity | Changing one part has little effect on others | Module boundaries, dependencies? |
| Reusability | Components can be reused | Which components are shared? |
| Analysability | Easy to diagnose faults and assess the impact of changes | Which logs, traces, monitoring are mandatory? |
| Modifiability | Can be changed without introducing defects | Change lead time, complexity? |
| Testability | Easy to test | Test coverage level by risk? |

## 8. Flexibility (4)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Adaptability | Adapts to a changing environment/requirements | Configuration instead of code changes? |
| Scalability | Scales when load grows | Scale over the next 12–24 months, how to scale? |
| Installability | Easy to install/uninstall | Deployment time, automation? |
| Replaceability | Can replace another product with the same purpose | Data export/import, avoiding vendor lock-in? |

## 9. Safety (5)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Operational constraint | Stays within safe operating limits | Which limits must not be exceeded? |
| Risk identification | Identifies risks that cause harm | Which hazard analysis has been done? |
| Fail safe | On failure, falls back to a safe state | What is the safe state? |
| Hazard warning | Warns of hazards | When and how to warn? |
| Safe integration | Stays safe when integrated with other systems | Integration conditions, testing? |
