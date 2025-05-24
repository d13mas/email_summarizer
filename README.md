# ✉️ Email Summarizer

**Email Summarizer** automatically summarizes emails received in a Gmail inbox using OpenAI's GPT-3.5 Turbo model. It was originally designed to condense long-form newsletters, but it can be used for any kind of content.

---

## 🚀 How It Works

1. **Connects to Gmail via IMAP**:
   - You can use your main Gmail account or create a **forwarding-only Gmail inbox** to isolate newsletters or long emails for summarization.
   - To automatically forward specific emails, create a filter in your primary Gmail account and forward them to the summarizer account.

2. **Authentication**:
   - Uses a Gmail **App Password**, not your real Gmail login.  
     📎 [How to generate an App Password](https://support.google.com/accounts/answer/185833?hl=en)

3. **Email Filtering**:
   - Only **unread emails** are processed.
   - Only emails from **approved sender addresses** (defined in `config.py`) are summarized.
     - This list is initialized with the `email_recipient` from your `.env` file.
     - You can add as many senders as needed (e.g. newsletter sources, Substack authors, etc.)

4. **Summarization via GPT-3.5 Turbo**:
   - Emails are tokenized and checked against the model’s token limit (16,385 tokens).
   - Long emails are **split into safe-size chunks** and summarized chunk-by-chunk.
   - Chunk summaries are then **combined into a single summary email**.

5. **Post-Processing**:
   - Only emails that are successfully summarized and sent are marked as **read**.
   - This prevents reprocessing on future runs.

---

## ⚙️ Configuration

1. Create a `.env` file in your root project directory:

    ```env
    gmail_user=your-gmail-address@gmail.com
    gmail_app_password=your-gmail-app-password
    email_recipient=where-you-want-to-receive-summaries@example.com
    openai_api_key=sk-xxxxxxxxxxxxxxxxxxxxx
    ```

2. Edit the `config.py` file (optional):
   - Add or modify the `allowed_senders` list to include addresses whose emails should be summarized:

     \`\`\`python
     allowed_senders = [
         "newsletter@source.com",
         "author@substack.com",
         "daily@digest.com"
     ]
     \`\`\`

---

## 🧪 Requirements

Install the dependencies with:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

This includes:
- `imapclient`
- `openai`
- `tiktoken`
- `pydantic`
- `python-dotenv`

---

## 📤 Output

Summaries are sent via email to the configured `email_recipient`. In the future, you may optionally:

- Store summaries in a Google Sheet or Markdown file
- Archive source emails
- Trigger webhook or API notifications

---

## 📝 TO DO

1. **Web Frontend (Flask + React)**:
   - Build a hosted web UI version for general users.
   - Features to include:
     - 🔐 Account registration & login
     - 🛡️ Authentication
     - 🔐 Secure storage for Gmail/app credentials
     - 🧩 UI to configure sender list, model options, and view output

2. **Enhance summarization pipeline**:
   - Summarize individual chunks → summarize combined chunk summaries (multi-pass summarization)

3. **Logging and error tracking**:
   - Add structured logs and retry logic
   - Optionally export summaries to database or file system

---
