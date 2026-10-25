# Story template

**[ID] Name (verb + goal)**
As a [specific role], I want [action/need], so that [benefit/value].

**Scope**: In: ... Out: ...
**Preconditions**: ...
**Related business rules**: BR-xx
**Acceptance criteria**
1. ...
2. ...
**Assumptions**: ...
**To clarify**: ...
**NFRs found (hand off to nfr-writer)**: ...

---
## Before/after example (composed for illustration, not from a real project)

Before: "As a user, I want to manage orders easily to save time."
Problems: generic role; "manage" covers many tasks; "easily" and "save time" cannot be verified; no AC.

After (one slice):
**ORD-12 Cancel an order not yet delivered**
As a logged-in customer, I want to cancel an order that has not been delivered, so that I do not have to pay for goods I no longer need.
Scope: In: cancelling the whole order. Out: cancelling part of an order, manual refund.
Rule: BR-07 (an order can be cancelled only in the status "Pending" or "Confirmed").
AC:
1. For an order in a valid status per BR-07, when the customer chooses "Cancel order" and confirms, the order moves to "Cancelled" and the customer sees a success message.
2. For an order already in the status "Shipping" or later, the "Cancel order" button is not shown; if called directly, the system rejects it and states the reason.
3. When the order is cancelled, the corresponding stock is returned.
4. When the customer clicks "Cancel order" twice in a row, only one cancellation is carried out.
To clarify: is a prepaid order refunded automatically? Who else receives the cancellation notice besides the customer?
NFRs found: refund time (hand off to nfr-writer); logging of order cancellations.
