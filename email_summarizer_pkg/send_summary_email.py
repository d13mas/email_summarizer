import os
import smtplib
import ssl
from email.message import EmailMessage

def send_summary_email(summary_text, subject="Your Summarized Emails"):
    sender_email = os.environ["EMAIL_USERNAME"]
    sender_password = os.environ["EMAIL_APP_PASSWORD"]
    recipient_email = os.environ.get("EMAIL_RECIPIENT", sender_email)  # Default to sender if not set

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
