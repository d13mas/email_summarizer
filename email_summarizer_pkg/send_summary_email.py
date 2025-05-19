import os
import smtplib
import ssl
from email.message import EmailMessage
from email_summarizer_pkg.config import settings

def send_summary_email(summary_text, subject="Your Summarized Emails"):
    sender_email = settings.gmail_user
    sender_password = settings.gmail_app_password
    recipient_email = settings.email_recipient

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Nicely format the summary as plain text
    msg.set_content(
        f"""Hello,

Here is your summarized email content:

{'-'*40}
{summary_text}
{'-'*40}

Sent automatically.
"""
    )

    # If you want HTML formatting, uncomment below:
    # msg.add_alternative(
    #     f"""\
    #     <html>
    #       <body>
    #         <h2>Your Summarized Emails</h2>
    #         <pre style="font-size:1.1em">{summary_text}</pre>
    #         <hr>
    #         <p>Sent automatically.</p>
    #       </body>
    #     </html>
    #     """, subtype='html'
    # )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)
