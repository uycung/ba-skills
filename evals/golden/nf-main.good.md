## NFRs for online booking (web, Vietnam, health data)

| Code | Characteristic | Description | Measure | Threshold | Verification method | Evidence type | Owner |
|---|---|---|---|---|---|---|---|
| NFR-PERF-01 | Performance efficiency | Booking confirmation shown quickly | Time from confirm click to confirmation | 95% within 3 s at the expected peak load | Load test | (c) common practice, PO to fix | Tech lead |
| NFR-SEC-01 | Security | Patient data protected | Encryption at rest and in transit | Current TLS version, AES for storage | Inspection | (b) recommended by the issuing organization | Security |
| NFR-REL-01 | Reliability | Booking service available | Availability per month | 99.5% | Monitoring | (c) common practice, PO to fix | Operations |
| NFR-PRIV-01 | Security | Personal health data handled lawfully | Compliance items | Per the legal reference | Legal review | (a) mandatory by law, needs legal confirmation | Legal |

## Trade-offs to settle
- Security checks against booking convenience: the PO decides.

## To confirm
- Every threshold marked (c) needs the PO.
- The privacy law items need legal confirmation.
