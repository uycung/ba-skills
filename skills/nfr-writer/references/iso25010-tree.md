# ISO/IEC 25010:2023 tree: 9 characteristics, 40 sub-characteristics

The names of the characteristics and sub-characteristics match the 2023 edition (9 characteristics, 40 sub-characteristics). The "Meaning" column is the skill's paraphrase. It was cross-checked on 2026-10-26 against Table I of a published paper on EVSE software, which states that its definitions are reproduced exactly from ISO/IEC 25010:2023. That is a **secondary source**, not the standard itself; the 25010 preview PDF supplied by the user is an image scan without a text layer, and only its table of contents was readable (Annex A comparison with 2011, Annex B mapping to dependability, Annex C use for measurement, Annex D quality from different stakeholders' perspectives). Quality in use has moved to ISO/IEC 25019:2023 and is not part of this tree.
The "complete guide" summary PDF supplied by the user is **not** used as a definition source: it diverges from the paper's table (for example faultlessness, user assistance, functional correctness). Spelling of sub-characteristic names varies between sources (behaviour/behavior, analysability/analyzability); this file follows the paper's table for names that differ only in spelling from the 2011 edition, except "time behaviour".
Changes from the 2011 edition: Safety added, Interaction capability split out (replacing Usability), Flexibility (replacing Portability), "faultlessness" instead of "maturity", "resistance" added under Security (integrity is kept), scalability and other new sub-characteristics added.

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
| Inclusivity | Usable by people of various backgrounds (age, ability, culture, language, gender, economic situation...) | Which languages, locales and user groups must be supported? Users with disabilities? |
| User assistance | Usable by people with the widest range of characteristics and capabilities to reach their goals in the context of use (the accessibility side; this is not the same as "help text") | WCAG level? Assistive technologies supported? Contextual help and support channels (ask separately)? |
| Self-descriptiveness | The interface explains itself | Are messages, labels and system status clear? |

## 5. Reliability (4)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Faultlessness | Performs its functions without fault under normal operation | Defect density, target MTBF? |
| Availability | Available when needed | SLO %, measurement window, are maintenance windows excluded? |
| Fault tolerance | Keeps running when a component fails | Which single points of failure are acceptable? |
| Recoverability | After an interruption or failure, recovers the data directly affected and re-establishes the desired state | RTO, RPO, frequency of recovery tests? |

## 6. Security (6)
| Sub-characteristic | Meaning (paraphrased) | Suggested question |
|---|---|---|
| Confidentiality | Only authorized people can access | Data classification, encryption at rest/in transit? |
| Integrity | System state and data are protected from unauthorized modification or deletion, whether by malicious action or by computer error | Integrity controls, signatures, audit? |
| Non-repudiation | Actions cannot be denied | Which actions need evidence? |
| Accountability | Actions trace back to the actor | What logs, retained for how long? |
| Authenticity | Identity/origin is authenticated | Authentication method, MFA? |
| Resistance | Keeps operating while under attack by a malicious actor (new in 2023) | ASVS level? OWASP list? Time to patch vulnerabilities? |

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
| Scalability | Handles growing or shrinking workloads, or adapts capacity to variability | Scale over the next 12–24 months, how to scale (and scale down)? |
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
