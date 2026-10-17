# Phishing Triage Automator - scores suspicious emails for red flags
email = {
    "sender": "security@am-azon.com",
    "subject": "Urgent: Your Account Will Be Locked",
    "body": "Dear User, We noticed suspicious activity on your account. To avoid account suspension, please verify your details immediately. Verify Now: http://secure-account-verify[.]com Failure to verify within 24 hours will result in permanent account lock"
}
email_two = {
    "sender": "newsletter@mycollege.edu",
    "subject": "Weekly campus events",
    "body": "Here are the clubs and talks happening this week on campus."
}
emails = [email,email_two]
def triage(email):
    score = 0
    if "Urgent" in email["subject"]:
        score = score + 1
    if "verify" in email["body"]:
        score = score + 1
    return score
for email in emails:
    score = triage(email)
    if score == 0:
        verdict = "SAFE"
    elif score == 1:
        verdict = "SUSPICIOUS"
    else:
        verdict = "LIKELY PHISHING"
    print(f"Sender: {email['sender']}")
    print(f"Subject: {email['subject']}")
    print(f"Risk Score: {score}")
    print(f"Verdict: {verdict}")
