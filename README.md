# Email Summarizer

Summarizes emails received in a Gmail inbox. Created to reduce the time to read extensive newsletters, but can be used for any text received in an email.

It narrows down the list of emails by filtering by subject and date range.

## TO DO

1. Improve search criteria to filter by UNSEEN messages AND specific senders (from a list).
2. Add a GPT cost tracker, indicating the GPT cost for each summarized email.
3. Manage big emails beyond 16385 tokens (apparently the limit for GPT 3.5 turbo).
4. Prompt it differently:

    - Create titles
    - Bullet points

5. Create a Flask and React app to publish on a website for general use. This will need:
    1. Account management
    2. Authentication
    3. Encrypted Settings: email and app password
