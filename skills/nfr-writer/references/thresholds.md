# NFR reference table (filtered version, updated with the agent v2 results)

Compiled: 24/10/2026. Arranged by the 9 characteristics of ISO/IEC 25010:2023.
ISO 25010 only defines characteristics and sub-characteristics and gives no numeric thresholds. Every number below comes from another source.

Status:
- ✅ Source checked in this session.
- 🔶 Consistent with current knowledge but the original source was not reopened. Must be verified before going into the skill.
- ❌ Removed from the original table (see the end of the file).

Evidence types: (a) mandatory by standard/law; (b) recommended by the issuing organization, the source states the exact number; (c) common practice, no official source, to be fixed with the PO.

Convention used in the skill: ISO definitions are paraphrased in your own words, with clause numbers cited, never copied verbatim.

## 1. Functional suitability (3 sub-characteristics)
Completeness, correctness, appropriateness. No standard numeric thresholds.
| NFR idea | Status | Note |
|---|---|---|
| Correctness of calculation results, acceptable rate of functional defects | (c) | Fixed by the PO according to business risk. |
Removed: legal obligations placed here (wrong characteristic). Legal obligations go in `legal-vn.md` and attach to the relevant characteristic (Security, Safety...).

## 2. Performance efficiency (3)
Time behaviour, resource utilization, capacity.
| Indicator | Threshold | Type | Status | Source |
|---|---|---|---|---|
| LCP (main content load) | ≤ 2.5 s at the 75th percentile | (b) | ✅ | web.dev/articles/vitals |
| INP (interaction responsiveness) | ≤ 200 ms at the 75th percentile | (b) | ✅ | web.dev/articles/vitals |
| CLS (layout stability) | ≤ 0.1 at the 75th percentile | (b) | ✅ | web.dev/articles/vitals |
| p95/p99 API latency | no official source | (c) | ✅ hard figure removed | Fix per the product's SLO |
| Load headroom, autoscaling thresholds | no official source | (c) | ✅ hard figure removed | Fix per the load test |
How to write the NFR: state the measurement condition (device, network, load, percentile); do not write "fast" or "smooth".

## 3. Compatibility (2)
Co-existence, interoperability.
| NFR idea | Status | Note |
|---|---|---|
| List of supported browsers/OS/devices | (c) | Take it from the product's actual traffic data. Suggested reference (Statcounter VN, 09/2026, secondary source, the agent summed the shares itself): Android ≥ 12 covers ≈ 82.8%, iOS ≥ 16 ≈ 92.3%. It is not certain that Android 17 is stable yet (two sources contradict). The original "iOS ≥ 17, Android ≥ 13 = N−1" is wrong and has been removed. |
| API standard / data exchange format | (c) | State the name and the specific version of the standard in the spec. |

## 4. Interaction capability (8)
Appropriateness recognizability, learnability, operability, user error protection, user engagement, inclusivity, user assistance, self-descriptiveness.
| Requirement | Status | Source |
|---|---|---|
| WCAG 2.2 Level AA conformance for web/mobile web | (b) ✅ | w3.org/TR/WCAG22 |
| Minimum touch target size 24×24 CSS px (criterion 2.5.8, level AA) | ✅ | w3.org/TR/WCAG22 |
| Focus not obscured (2.4.11, level AA) | ✅ | w3.org/TR/WCAG22 |
| Support for login that does not require remembering/puzzles (3.3.8, level AA) | ✅ | w3.org/TR/WCAG22 |
Note on mapping: WCAG mainly serves "inclusivity" (and partly "operability"). The original placed 2.4.7 under "user assistance", which is a stretch and has been removed.
WCAG 2.0 AA under Circular 26/2020 (TT 26/2020): not verified (see the removal section).

## 5. Reliability (4)
Faultlessness, availability, fault tolerance, recoverability.
| Availability level | Maximum downtime per year | Status |
|---|---|---|
| 99% | ≈ 3.65 days | ✅ (calculated) |
| 99.9% | ≈ 8.76 hours | ✅ (calculated) |
| 99.99% | ≈ 52.6 minutes | ✅ (calculated) |
| 99.999% | ≈ 5.26 minutes | ✅ (calculated) |
Always state the measurement window (month/quarter/year) and how it is measured (where, whether announced maintenance is excluded). Use error budget = 100% − SLO (sre.google, ✅).
RPO/RTO by tier: (c), fixed per business impact analysis. The AWS DR figures in the original were embellished and have been removed.
DORA (dora.dev): the latest report is 2025 (per agent v2, not reopened myself). The current metrics are 5, including deployment rework rate and failed deployment recovery time. **Do not use the 2024 figures** (5/20/10/40%) because they are outdated. When a threshold is needed, take the table from the latest report and record the report year. Status: ⚠️.
DORA is a software delivery performance metric, not a sub-characteristic of Flexibility as the original placed it. Put it in the skill's "Operational metrics" part.

## 6. Security (6)
Confidentiality, integrity, non-repudiation, accountability, authenticity, resistance.
| Standard | Content used in NFRs | Status |
|---|---|---|
| OWASP Top 10:2025 | The list of common web risks, to use as the criterion "no vulnerabilities in these categories" | ✅ |
| OWASP ASVS 5.0 | 17 chapters, about 350 requirements, 3 levels L1/L2/L3. Choose the level by risk. | ✅ |
| PCI DSS 4.0.1 | Mandatory if payment card data is processed (a). Quote the exact requirement numbers from the official document when writing the spec. | ✅ version; 🔶 individual requirements |
| ISO/IEC 27001:2022 | Information security management system (Annex A, 93 controls). | 🔶 |
| ISO/IEC 42001:2023 | AI management system. | 🔶 |
| NIST AI 100-1 (AI RMF 1.0) | Voluntary. The original wrote the code wrongly as "AI RMF". | 🔶 |
For the legal part: see `legal-vn.md`.

## 7. Maintainability (5)
Modularity, reusability, analysability, modifiability, testability.
| NFR idea | Status | Note |
|---|---|---|
| Cyclomatic complexity thresholds | (c) | The levels 10/20/50 belong to SEI, not NIST as the original said. Use as a hint. |
| Test coverage (code coverage) | (c) | No standard threshold. Fix by module risk. |

## 8. Flexibility (4)
Adaptability, scalability, installability, replaceability.
| NFR idea | Status | Note |
|---|---|---|
| Scale to be supported (users, transactions per second, data) | (c) | State the current figure, the figure for the next 12–24 months, and how it is measured. |
Removed: DORA placed here (wrong characteristic).

## 9. Safety (5)
Operational constraint, risk identification, fail safe, hazard warning, safe integration.
Applies strongly to products that affect physical wellbeing, large financial amounts, or high-risk AI. No general numeric thresholds. Vietnam's AI Law and the EU AI Act: see `legal-vn.md`.

## Removed or downgraded, with reasons
| Item in the original | Reason |
|---|---|
| Personal Data Protection Law (BVDLCN) as a "draft" | Wrong: it has been in force since 01/01/2026. Moved to `legal-vn.md`. |
| Decree 53/2022, Decree 85/2016, Circular 12/2022 | Based on repealed laws; transitional validity unclear. Marked "needs checking". |
| Decision 975/QĐ-BTTTT, Circular 26/2020 (WCAG 2.0 AA) | Not verified. |
| iOS 17 / Android 13 "N−1" | Outdated, no source. |
| API p95/p99, 5xx < 0.1%, headroom 30–50%, autoscaling thresholds | No source states these exact figures: moved to (c). |
| AWS DR figures | Embellished, not checked. |
| ASVS "14 chapters" | Wrong: v5.0 has 17 chapters. |
| URLs that are only home pages | Not used as sources. |

## Remaining work list for agent v2 to check
1. Reopen each source on the 🔶 lines.
2. Official definitions for the roughly 28 sub-characteristics still missing (only a secondary version exists).
3. DORA 2025 metrics: open dora.dev and record the reference table.
4. Current iOS/Android support milestones and market share in Vietnam.
