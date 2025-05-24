# Email Summarizer

Summarizes emails received in a Gmail inbox. Created to shorten the time to read extensive newsletters, but can be used for any text received in an email.

## Details and flow

1. Connects to the email inbox via IMAP.
    a. if you want to avoid using your real email address where you get the long emails to summarize, you can create a new Gmail account and forward the emails there using a rule.
2. IMAP connection will require an APP Password. Check here how to get one: https://support.google.com/accounts/answer/185833?hl=en
3. The app will fetch only unread emails that belong to a list of from addresses you set in the config file. This list is initialized with the email recipient you defined in your .env file. you can add as many email addresses as needed (newsletters you are subscribed to, or senders of other content you want to summarize).
4. The app uses the GPT 3.5 Turbo module, so there's a limit of token that can be sent. Longer emails are processed in chunks and then concatenated to send as a single email. 
    a. TO DO: Re summarize all token to get a single harmonized summary.
5. Only if the email was summarized and sent to the indicated recipient, is marked as read, so it does not get reprocessed.

## Config

1. Create a `.env` file in your root folder.
2. Populate the file with the following variables:

    - gmail_user
    - gmail_app_password
    - email_recipient
    - openai_api_key

## TO DO

1. Create a Flask and React app to publish on a website for general use. This will need:
    1. Account management
    2. Authentication
    3. Encrypted Settings: email and app password
    4. A FE to settings, and output.
