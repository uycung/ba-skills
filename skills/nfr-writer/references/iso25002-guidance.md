# Guidance on using the quality model per ISO/IEC 25002:2024

A paraphrased summary of 25002:2024 (first edition, current). Cite section numbers when quoting; do not copy verbatim.

1. **Tailoring**: you may add, remove or rename at the **sub-characteristic** level, not at the characteristic level; changes and their reasons must be recorded. In the skill: every "not applicable" sub-characteristic needs a short reason.
2. **Trade-offs (§7.1)**: characteristics can pull against each other (security vs convenience, performance vs cost and maintainability). State the conflicting pair and let the PO decide.
3. **Prioritization by context (§7.4)**: not every characteristic matters equally; rank by product type, users, risk. Use `product-profiles.md` as a starting point.
4. **The BA's role (§8.1)**: anticipate NFRs early, from the requirements phase, instead of finding them in the testing phase.
5. **Measurement**: measures are in ISO/IEC 25023 (a draft DIS 25023:2026 exists). When writing NFRs, each requirement needs a measure, a threshold and a measurement method, even if the exact codes of 25023 are not used.
6. **Related standards family**: 25019 (quality in use), 25030 (quality requirements), 25040 (evaluation process).
