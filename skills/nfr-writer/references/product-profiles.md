# Product profiles: priority characteristics

Levels: ●●● must be examined closely, ●● usually important, ● quick look. This is a starting point; the user adjusts it to the context (25002 §7.4).

| Characteristic | Web | Mobile | Internal | AI |
|---|---|---|---|---|
| Functional suitability | ●● | ●● | ●●● | ●●● (correctness, coverage) |
| Performance efficiency | ●●● (Core Web Vitals) | ●●● (startup, battery, memory) | ●● | ●●● (latency, cost per query) |
| Compatibility | ●● (browsers) | ●●● (OS, devices) | ●●● (integration with legacy systems) | ●● (model API) |
| Interaction capability | ●●● (WCAG) | ●●● | ●● | ●●● (transparency, user control) |
| Reliability | ●●● | ●● (offline mode, sync) | ●●● | ●● (fallback when the model fails) |
| Security | ●●● | ●●● (local storage, authentication) | ●●● (authorization) | ●●● (prompt injection, data leakage) |
| Maintainability | ●● | ●● | ●●● | ●● (model and prompt version management) |
| Flexibility | ●● | ●● (app store release) | ●● | ●● (switching model provider) |
| Safety | ● | ● | ● | ●●● (consequences of wrong results, risk to users) |

## Extra questions by type
- **Web**: supported browsers, SEO, page load on slow networks, availability SLO, CDN.
- **Mobile**: minimum OS version (take it from the product's actual traffic data, see `thresholds.md`), battery level, offline, package size, device permissions, app store rules.
- **Internal**: number of users, SSO/AD integration, audit, maintenance windows, training, system life cycle.
- **AI**: measure output quality with an evaluation set (evals) rather than by feel; latency and cost; human oversight (human-in-the-loop); labelling of AI-generated content; data used for training/sent to the provider; legal framework (see `legal-vn.md`, the AI Law and the EU AI Act). Voluntary references: NIST AI 100-1, ISO/IEC 42001:2023.
