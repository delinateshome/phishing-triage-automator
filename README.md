# phishing-triage-automator

Python tool that scores emails for phishing red flags.

A simple Python tool that scans emails for common phishing red flags, gives each one a risk score, lists the specific reasons it was flagged, and prints a verdict: SAFE, SUSPICIOUS, or LIKELY PHISHING.

I built this while studying cybersecurity, to practice the kind of first-pass triage a SOC analyst does when sorting suspicious emails.

## What it does
It checks each email for known phishing signals and records a reason for each one it finds:
- Urgency / pressure language in the subject (e.g. "Urgent")
- Requests to "verify" account details in the body
- Suspicious sender domains — lookalike addresses using hyphens (e.g. `am-azon.com`), found by splitting the sender address at the `@`
- Account-threat / fear language (e.g. "locked"), checked in both subject and body, case-insensitively

The risk score is the number of reasons found:
- 0 → SAFE
- 1 → SUSPICIOUS
- 2 or more → LIKELY PHISHING

It runs over a list of emails, so it can triage many at once, and prints *why* each one was flagged.

## Example output
Sender: security@am-azon.com
Subject: Urgent: Your Account Will Be Locked
Risk Score: 4
Verdict: LIKELY PHISHING

Urgent wording in subject
Asks you to verify something
Suspicious sender domain: am-azon.com
Threatens the account will be locked
Sender: newsletter@mycollege.edu
Subject: Weekly campus events
Risk Score: 0
Verdict: SAFE
## How to run
1. Install Python 3.
2. Download the `.py` file.
3. Run it: `python phishing_triage.py`

## How to add your own emails
Make a new email dictionary and add it to the `emails` list:
```python
my_email = {
    "sender": "example@test.com",
    "subject": "Some subject line",
    "body": "The email body text."
}
emails = [email, email_two, my_email]
```

The loop triages it automatically.

## Roadmap
-Detect suspicious links in the body (e.g. http:// and masked URLs)
-Flag risky attachments
-Case-insensitive matching across all rules
-Export results to a report file
## About
Built by Delina Teshome, cybersecurity student, learning SOC-style email triage.
