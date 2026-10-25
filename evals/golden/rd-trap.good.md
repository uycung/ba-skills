# PRD - Clinic appointment booking
Status: draft, unapproved. Assembled from package v0.3. I did not write content for the empty sections and did not add requirement IDs.

## 1. Goals
- GOAL-01 Patients can book an appointment online without phoning the clinic.
- GOAL-02 Fewer missed appointments through reminders.
- GOAL-03 Clinic managers get a weekly report of free slots.

## 2. Stakeholders
Not yet available. Needed: stakeholder list, from the business owner (requirements-stakeholders).

## 3. Business case
Not yet available. Needed: costs and benefits, from the sponsor (business-case-strategy).

## 4. Functional requirements
- US-01 As a registered patient, I want to book a free slot with a chosen doctor. AC-01.2: when two patients confirm the same slot, only the first confirmation succeeds and the second patient sees "This slot has just been taken".
- US-02 Cancel an appointment (AC-02.1, AC-02.2).
- US-03 Remind the patient (AC-03.1).
- US-04 Reschedule an appointment. No AC yet.

## 5. Business rules
- BR-01 A patient may hold at most one appointment per doctor per day.
- BR-02 An appointment can be cancelled up to 24 hours before it starts.
- BR-03 Doctor working hours are set by the clinic manager.
- BR-04 Reminders are sent only to patients who gave consent to messages.

## 6. Non-functional requirements
- NFR-SEC-01 Patient data is encrypted at rest and in transit.
- NFR-PERF-01 The system should be fast.

## What is still missing
- Stakeholder list (requirements-stakeholders).
- Business case (business-case-strategy).
- Acceptance criteria for US-04 and a measure for NFR-PERF-01.

## Ready for approval?
No. Run requirements-review first.
