# Clinic booking - stories submitted for review (draft v0.2)

## Stories
### US-01 Book an appointment
As a registered patient, I want to book a free slot with a chosen doctor, so that I do not have to phone the clinic.
- AC-01.1 Given a registered patient and a free slot on 2026-11-02 at 09:00, when the patient confirms, then the slot is marked taken and a confirmation with the doctor's name and time is shown.
- AC-01.2 When two patients confirm the same slot, only the first confirmation succeeds and the second patient sees "This slot has just been taken".

### US-02 Search doctors
As a customer, I want to search for doctors so that I can find one quickly.
- AC-02.1 The system should respond quickly when the customer searches for a doctor.
- AC-02.2 Results show the doctor's name, specialty and next free slot.

### US-03 Manage appointments
As a client, I want to manage my appointments.
- AC-03.1 The client can do what they need with their appointments.

### US-04 Cancel an appointment
As a patient, I want to cancel my appointment at any time, so that I do not pay for nothing.
- AC-04.1 Given an appointment, when the patient cancels, then it is cancelled at any time before the start.
Rules: BR-02

### US-05 Reminders
As a patient, I want a reminder, so that I do not forget my appointment.
(No acceptance criteria yet.)

## Business rules
- BR-02 An appointment can be cancelled up to 24 hours before it starts.

## Non-functional requirements
- NFR-USA-01 The system shall be user-friendly.
