from .email_client import connect_imap, fetch_emails, parse_email
from .summarizer import summarize_text
from email_summarizer_pkg.send_summary_email import send_summary_email

def process_emails():
    client = connect_imap()
    raw_emails = fetch_emails(client)
    for msg_id, data in raw_emails.items():
        email_text = parse_email(data)
        if not email_text:
            continue
        summary = summarize_text(email_text)
        print(f"Summary for email {msg_id}:\n{summary}\n{'='*50}")
        # ... after summary is created
        send_summary_email(summary)
        print("Summary email sent!")

if __name__ == "__main__":
    process_emails()
