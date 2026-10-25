# NFR template

| Code | Characteristic / sub-characteristic (ISO 25010:2023) | Requirement | Measure | Threshold | Measurement condition | Verification method | Evidence | Priority | Owner | Source |
|---|---|---|---|---|---|---|---|---|---|---|

Syntax of one NFR sentence: "The system SHALL/SHOULD [behaviour] reaching [measure] [threshold], measured [where, condition, percentile/time window], verified by [method]."

## Examples (illustration, figures taken from thresholds.md)
| NFR-PERF-01 | Performance efficiency / Time behaviour | The product detail page loads quickly | LCP | ≤ 2.5 s at the 75th percentile | Real user data (field) on mobile, 4G network | Weekly RUM monitoring | (b) | Must | Frontend lead | web.dev Core Web Vitals |
| NFR-REL-01 | Reliability / Availability | The payment service is available | Share of successful requests | [FIX WITH THE PO, for example 99.9% = at most ≈ 43 minutes of downtime per month] | 30-day window, measured at the API gateway, excluding announced maintenance | SLO dashboard | (c) | Must | SRE | calculated from the SLO |
| NFR-INC-01 | Interaction capability / Inclusivity | The web interface meets WCAG 2.2 Level AA | Number of AA criteria not met | 0 criteria on the main flows | Automated tools and manual checks | Check before release | (b) | Should | UX lead | WCAG 2.2 |

## At the end of every NFR document
**Trade-offs to settle**: ...
**To confirm**: numbers without a source, ⚠️ legal items (need legal), questions for the PO/engineering.
