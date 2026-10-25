# Mapping BABOK v3 to ISO/IEC 25010:2023

BABOK sources: section 2.3 (p. 16), 10.30 (pp. 302–304), read from the copy supplied by the user. Use this table when the stakeholder/BA is familiar with BABOK terms.

## What BABOK says about NFRs
- NFRs (also called quality attributes, quality of service requirements) are a subtype of **solution requirements**, alongside functional requirements. NFRs are not about functional behaviour but about the conditions the solution must meet to remain effective.
- NFRs can apply to process and people aspects too, not only software.
- Quantify when possible so they can be verified (for example "90% of responses within 2 seconds" instead of "fast response"). The examples in BABOK are only illustrations, not standard thresholds.
- Certification, compliance, localization: the measurement detail is given by the party that sets the standard/regulation; an SLA states the measures of success; enterprise architecture determines environment requirements.
- Context decides the optimal set of NFRs; context always changes, so NFRs may have to be adjusted or dropped.
- Limits: user expectations differ, NFRs can conflict and need negotiation (for example security versus performance), over-tight constraints increase time/cost, many NFRs are qualitative.
- **Transition requirements** (data conversion, training, keeping operations running) are a separate type, not NFRs (BABOK 2.3).

## Catalogue mapping
| BABOK 10.30.3.1 | ISO/IEC 25010:2023 | Note |
|---|---|---|
| Availability | Reliability / Availability | BABOK: % of time available |
| Compatibility | Compatibility | Matches |
| Functionality (suitability, accuracy, interoperability) | Functional suitability; "interoperability" belongs to Compatibility in ISO | Interoperability is placed differently |
| Maintainability | Maintainability | Matches |
| Performance Efficiency | Performance efficiency | Matches |
| Portability | Flexibility (installability, adaptability, replaceability) | Renamed in ISO 2023 |
| Reliability | Reliability (faultlessness, fault tolerance, recoverability) | Matches |
| Scalability | Flexibility / Scalability; partly Performance efficiency / Capacity | ISO 2023 made scalability a sub-characteristic |
| Security | Security | ISO 2023 has 6 sub-characteristics |
| Usability | Interaction capability | Renamed and extended in ISO 2023 (inclusivity, user assistance...) |
| Extensibility | Flexibility / Modifiability (Maintainability) | Close |
| Certification | Not a quality characteristic; it is a **source** of requirements | Label (a) and name the standard |
| Compliance | As above | See `legal-vn.md` |
| Localization | Partly Inclusivity (language), Adaptability | Ask separately: language, currency, formats |
| Service Level Agreements | Not a characteristic; it is a **form of commitment** that contains NFRs (availability, performance...) | Record the source as the SLA |
| (none) | **Safety** (5 sub-characteristics) | Added by ISO; BABOK does not name it |

## Is there a conflict?
No conflict in principle: both require NFRs that are measurable, contextual and subject to trade-off negotiation. Differences to note:
1. **Level of detail**: BABOK is a flat catalogue of about 14 items with short definitions; ISO has 9 characteristics, 40 sub-characteristics and a tailoring framework (25002). Use ISO as the main frame and BABOK as a terminology bridge.
2. **Different placement**: interoperability; Compliance/Certification/Localization/SLA in BABOK are sources or constraints, not quality characteristics in ISO.
3. **Renamed**: Portability → Flexibility, Usability → Interaction capability. When talking to people used to the old names, give both.
4. **Scope**: BABOK allows NFRs about processes and people; ISO 25010 speaks only of product/system quality.
5. **Gap in ISO**: transition requirements are not in ISO 25010. When they come up (data conversion, training, parallel running), record them in a separate section, not inside a quality characteristic.
