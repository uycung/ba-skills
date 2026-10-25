**MOVE-01 Move an appointment to another free slot**
As a registered patient, I want to move my appointment to another free slot with the same doctor, so that I do not have to cancel and book again.

**Scope**: In: moving one appointment to another free slot of the same doctor. Out: changing the doctor, moving after the cut-off.
**Related business rules**: BR-01 (one appointment per doctor per day), BR-02 (a change is allowed up to 24 hours before the start).
**Acceptance criteria**
1. Given an appointment that starts in more than 24 hours, when the patient picks another free slot of the same doctor and confirms, then the appointment is booked in the new slot and the old slot becomes free.
2. Given an appointment that starts in less than 24 hours, the "Move" action is not offered; if it is called directly, the system rejects it and states the reason.
3. When the chosen slot has been taken in the meantime, the system keeps the old appointment and tells the patient the slot is no longer free.
4. When the patient already holds an appointment with that doctor on the new day, the system rejects the move and states BR-01 as the reason.
**Assumptions**: "Same doctor" is a hard rule; the old slot is released only when the new booking succeeds.
**To clarify**: Is a move exactly 24 hours before the start still allowed? Should a waiting list be told when the old slot is freed?
**NFRs found**: "The move should complete within 3 seconds" (response time) is recorded as NFR-PERF-TMP and handed to nfr-writer.
