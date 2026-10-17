# phishing-triage-automator
Python tool that scores emails for phishing red flags

A simple Python tool that scans emails for common phishing red flags and gives each one a risk score and a verdict: SAFE, SUSPICIOUS, or LIKELY PHISHING.
I built this while studying cybersecurity, to practice the kind of first-pass triage a SOC analyst does when sorting through suspicious emails.

## What it does

It checks each email for known phishing signals and adds a point for each one:
- Urgency / pressure language in the subject (e.g. "Urgent")
- Requests to "verify" account details in the body

Based on the total score, it prints a verdict:
- **0 → SAFE**
- **1 → SUSPICIOUS**
- **2 or more → LIKELY PHISHING**

It runs over a list of emails, so it can triage many at once.

## Example output

Sender: security@am-azon.com
Subject: Urgent: Your Account Will Be Locked
Risk Score: 2
Verdict: LIKELY PHISHING

Sender: newsletter@mycollege.edu
Subject: Weekly campus events
Risk Score: 0
Verdict: SAFE

## How to run

1. Install Python 3.
2. Download the .py file.
3. Run it: `python phishing_triage.py`

## How to add your own emails

Make a new email dictionary and add it to the `emails` list:

    my_email = {
        "sender": "example@test.com",
        "subject": "Some subject line",
        "body": "The email body text."
    }
    emails = [email, email_two, my_email]

The loop triages it automatically.

## Roadmap

- More detection rules (suspicious links, lookalike domains, attachments)
- Flag spoofed / mismatched sender domains
- Export results to a report file

## About

Built by Delina Teshome, cybersecurity student, learning SOC-style email triage.
