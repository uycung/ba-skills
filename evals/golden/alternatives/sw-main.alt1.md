## MV-1 Reschedule an appointment
As a patient with a booking, I want to switch it to another free slot of the same doctor, so that I keep my doctor without cancelling first.

**Business rules**: BR-02 (change allowed up to 24 hours before the start), BR-01 (a patient holds one appointment per doctor per day).

**Acceptance criteria**
1. Given an appointment that starts in more than 24 hours, when the patient confirms a different free slot of the same doctor, then the appointment moves to the new slot and the old slot is free again.
2. Given an appointment that starts in less than 24 hours, the system does not offer the move and explains why.
3. If the new slot is taken by someone else before confirmation, the original appointment stays unchanged and the patient is told.
4. If the patient already has an appointment with this doctor on the new day, the move is refused with a message that cites BR-01.

**Assumptions**: the old slot is only released once the new booking succeeds.

**To clarify**: Is a change exactly 24 hours before the start still allowed?

**Non-functional**: "complete within 3 seconds" is a performance requirement, kept out of the criteria and passed to nfr-writer.
