**AUTH-01 Log in**
As a customer, I want to log in with my email and password, so that I can reach my account.
**Acceptance criteria**
1. Given a registered customer, when the correct email and password are entered, then the customer reaches the account page.
2. When a wrong password is entered, the system shows "Email or password is incorrect" and does not say which of the two is wrong.

**AUTH-02 Reset the password**
As a customer, I want to reset my password from the login page, so that I can get back in when I forget it.
**Acceptance criteria**
1. When the customer asks for a reset with a registered email, the system sends a reset link to that email.
2. When the email is not registered, the system shows the same confirmation message and sends nothing.

**AUTH-03 See my order history**
As a customer, I want to see my past orders, so that I can check what I bought.
**Acceptance criteria**
1. Given a logged-in customer, when the customer opens "Order history", then only that customer's orders are listed, newest first, each with order code, date and status.

**Assumptions**: The request was split into three stories because each delivers one value on its own; the lock rule is kept out of AUTH-01 until it is known.
**To clarify**: How many wrong passwords lock the account, for how long, and who can unlock it? Is a reset link valid for a limited time?
**NFRs found**: "fast and easy to use" has no measure; recorded as NFR-PERF-TMP and NFR-USA-TMP and handed to nfr-writer.
