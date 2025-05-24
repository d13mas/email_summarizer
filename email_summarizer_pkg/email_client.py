import email
from imapclient import IMAPClient
from datetime import datetime
from email_summarizer_pkg.config import settings

def connect_imap():
    client = IMAPClient('imap.gmail.com', ssl=True)
    client.login(settings.gmail_user, settings.gmail_app_password)
    client.select_folder('INBOX', readonly=False)
    return client

def fetch_emails(client):
    client.select_folder('INBOX', readonly=False)

    senders = settings.allowed_senders
    search_criteria = ['UNSEEN']

    if senders:
        if len(senders) == 1:
            search_criteria += ['FROM', senders[0]]
        elif len(senders) > 1:
            # Build an OR group for multiple senders
            or_criteria = ['OR', 'FROM', senders[0], 'FROM', senders[1]]
            for sender in senders[2:]:
                or_criteria = ['OR', or_criteria, ['FROM', sender]]

            # Flatten to single list
            def flatten(c): return sum([flatten(i) if isinstance(i, list) else [i] for i in c], [])
            search_criteria += flatten(or_criteria)

    print("IMAP search criteria:", search_criteria)
    message_ids = client.search(search_criteria)
    return client.fetch(message_ids, ['RFC822'])

def parse_email(msg_data):
    email_msg = email.message_from_bytes(msg_data[b'RFC822'])
    text_content = ""
    for part in email_msg.walk():
        if part.get_content_type() == 'text/plain':
            text_content += part.get_payload(decode=True).decode(errors='ignore')
    return text_content.strip()

def mark_as_read(client, msg_id: str):
    # Mark a single email as read (adds the \Seen flag).
    client.set_flags(msg_id, ['\\Seen'])
