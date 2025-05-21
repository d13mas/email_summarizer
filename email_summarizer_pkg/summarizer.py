# summarizer.py

from openai import OpenAI
from email_summarizer_pkg.config import settings

client = OpenAI(api_key=settings.openai_api_key)

def summarize_text(text: str) -> str:
    """Summarizes the input text using OpenAI's GPT API."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that summarizes emails."
                        "Return a clear, concise summary that is no more than a 5-minute read."
                        "Use resources as you see fit, like adding titles to paragraphs, or using bullet points, or numbered lists, etc"
                        "Whatever you find useful to make it clear, emphasize the concept and speed up readability."
                    ),
                },
                {"role": "user", "content": text},
            ],
            temperature=0.5,
            max_tokens=4096,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error during summarization: {str(e)}"
