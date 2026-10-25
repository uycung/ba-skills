# Clinic appointment booking - requirements package (draft v0.3)

## Goals
- GOAL-01 Patients can book an appointment online without phoning the clinic.
- GOAL-02 Fewer missed appointments through reminders.
- GOAL-03 Clinic managers get a weekly report of free slots.

## Stories
### US-01 Book an appointment (GOAL-01)
As a registered patient, I want to book a free slot with a chosen doctor, so that I do not have to phone the clinic.
- AC-01.1 Given a registered patient and a free slot, when the patient confirms the booking, then the slot is marked taken and a confirmation is shown.
- AC-01.2 When two patients confirm the same slot, only the first confirmation succeeds and the second patient sees "This slot has just been taken".
Rules: BR-01

### US-02 Cancel an appointment (GOAL-01)
As a registered patient, I want to cancel my appointment up to 2 hours before it starts, so that the slot can be given to someone else.
- AC-02.1 Given an appointment that starts in more than 2 hours, when the patient cancels, then the slot becomes free.
- AC-02.2 Given an appointment that starts in less than 2 hours, the Cancel button is not shown.
Rules: BR-02, BR-09

### US-03 Remind the patient (GOAL-02)
As a registered patient, I want a reminder before my appointment, so that I do not forget it.
- AC-03.1 A reminder is sent to the phone number on file on the day before the appointment.
Rules: BR-04

### US-04 Reschedule an appointment (GOAL-01)
As a registered patient, I want to move my appointment to another free slot, so that I do not have to cancel and book again.

### US-05 Export the audit log
As a clinic administrator, I want to export the audit log as a CSV file, so that I can send it to an auditor.
- AC-05.1 The export contains one row per booking, change and cancellation.

## Business rules
- BR-01 A patient may hold at most one appointment per doctor per day.
- BR-02 An appointment can be cancelled up to 24 hours before it starts.
- BR-03 Doctor working hours are set by the clinic manager.
- BR-04 Reminders are sent only to patients who gave consent to messages.

## Non-functional requirements
- NFR-SEC-01 Patient data is encrypted at rest and in transit.
- NFR-PERF-01 The system should be fast.
