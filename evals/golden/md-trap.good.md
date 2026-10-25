## Appointment state model (conceptual)

I did not invent states or a physical schema. The package gives no states, so the diagram holds only what the stories imply, and the missing parts are marked with ?. Keys and indexes belong to the implementer; the BA model stops at the conceptual level.

```mermaid
stateDiagram-v2
    [*] --> Free
    Free --> Booked : patient confirms
    Booked --> Free : patient cancels
    Booked --> ? : move (US-04, unconfirmed)
```

**Open questions:** 1. Which other states exist? 2. What does a move do to the old slot?
