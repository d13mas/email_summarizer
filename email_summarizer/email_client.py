import email
from imapclient import IMAPClient
from datetime import datetime
from .email_summarizer.config import settings

def connect_imap():
    client = IMAPClient('imap.gmail.com', ssl=True)
    client.login(settings.gmail_user, settings.gmail_app_password)
    client.select_folder('INBOX', readonly=True)
    return client

def fetch_emails(client):
    search_criteria = [
        'SUBJECT', settings.search_subject,
        'SINCE', settings.since_date,
        'BEFORE', settings.before_date
    ]
    message_ids = client.search(search_criteria)
    return client.fetch(message_ids, ['RFC822'])

def parse_email(msg_data):
    email_msg = email.message_from_bytes(msg_data[b'RFC822'])
    text_content = ""
    for part in email_msg.walk():
        if part.get_content_type() == 'text/plain':
            text_content += part.get_payload(decode=True).decode(errors='ignore')
    return text_content.strip()
