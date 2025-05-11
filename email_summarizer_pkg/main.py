from .email_client import connect_imap, fetch_emails, parse_email
from .summarizer import summarize_text

def process_emails():
    client = connect_imap()
    raw_emails = fetch_emails(client)
    for msg_id, data in raw_emails.items():
        email_text = parse_email(data)
        if not email_text:
            continue
        summary = summarize_text(email_text)
        print(f"Summary for email {msg_id}:\n{summary}\n{'='*50}")

if __name__ == "__main__":
    process_emails()
