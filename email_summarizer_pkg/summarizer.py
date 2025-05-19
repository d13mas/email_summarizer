# summarizer.py

from openai import OpenAI
from email_summarizer_pkg.config import settings

client = OpenAI(api_key=settings.openai_api_key)

def summarize_text(text: str) -> str:
    """Summarizes the input text using OpenAI's GPT API."""
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that summarizes emails. "
                        "Return a clear, concise summary that is no more than a 5-minute read."
                    ),
                },
                {"role": "user", "content": text},
            ],
            temperature=0.5,
            max_tokens=800,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error during summarization: {str(e)}"
