import re

# Common phishing keywords
PHISHING_KEYWORDS = [
    'urgent', 'account suspended', 'verify your account', 'click here', 
    'security alert', 'password expired', 'action required'
]

# Suspicious sender patterns
SUSPICIOUS_SENDER_DOMAINS = [
    'amaz0n', 'paypa1', 'micr0soft', 'secure-mail', 'update-info'
]

def scan_subject(subject):
    """Scan subject for phishing keywords."""
    subject_lower = subject.lower()
    for keyword in PHISHING_KEYWORDS:
        if keyword in subject_lower:
            return True, f"Suspicious keyword found in subject: '{keyword}'"
    return False, "No suspicious keywords in subject."

def check_sender(sender_email):
    """Check sender email address for suspicious patterns."""
    sender_lower = sender_email.lower()
    for bad_domain in SUSPICIOUS_SENDER_DOMAINS:
        if bad_domain in sender_lower:
            return True, f"Suspicious sender domain found: '{bad_domain}'"
    return False, "Sender email appears safe."

def find_urls(email_body):
    """Extract URLs and check for suspicious domains."""
    urls = re.findall(r'(https?://[^\s]+)', email_body)
    flagged_urls = []
    for url in urls:
        if any(bad_domain in url.lower() for bad_domain in SUSPICIOUS_SENDER_DOMAINS):
            flagged_urls.append(url)
    return urls, flagged_urls

def scan_email(subject, sender, body):
    """Perform a full scan on email components."""
    report = []

    subject_flag, subject_message = scan_subject(subject)
    report.append(subject_message)

    sender_flag, sender_message = check_sender(sender)
    report.append(sender_message)

    urls, flagged_urls = find_urls(body)
    if flagged_urls:
        report.append(f"Suspicious URLs found: {', '.join(flagged_urls)}")
    else:
        report.append("No suspicious URLs found.")

    return report
