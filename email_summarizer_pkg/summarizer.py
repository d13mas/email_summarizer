from openai import OpenAI
from email_summarizer_pkg.config import settings
from email_summarizer_pkg.utils.token_utils import count_tokens, chunk_text

client = OpenAI(api_key=settings.openai_api_key)

# Token limits
MAX_MODEL_TOKENS = 16385
RESERVED_OUTPUT_TOKENS = 1000
CHUNK_OVERHEAD_TOKENS = 100
MAX_INPUT_TOKENS = MAX_MODEL_TOKENS - RESERVED_OUTPUT_TOKENS - CHUNK_OVERHEAD_TOKENS
CHUNK_OVERLAP = 50

def summarize_text(text: str, model: str = "gpt-3.5-turbo-0125") -> str:
    token_count = count_tokens(text, model=model)

    if token_count + RESERVED_OUTPUT_TOKENS <= MAX_MODEL_TOKENS:
        return summarize_chunk(text, model)

    print(f"Splitting large input ({token_count} tokens)...")
    chunks = chunk_text(text, model=model, max_tokens=MAX_INPUT_TOKENS, overlap=CHUNK_OVERLAP)
    summaries = []

    for i, chunk in enumerate(chunks):
        tokens_in_chunk = count_tokens(chunk, model=model)

        if tokens_in_chunk + RESERVED_OUTPUT_TOKENS > MAX_MODEL_TOKENS:
            print(f"[SKIPPED] Chunk {i+1} is too large ({tokens_in_chunk} tokens). Skipping.")
            continue

        try:
            print(f"Summarizing chunk {i+1}/{len(chunks)} — {tokens_in_chunk} tokens")
            summary = summarize_chunk(chunk, model)
            summaries.append(f"Chunk {i+1} Summary:\n{summary}")
        except Exception as e:
            summaries.append(f"Chunk {i+1} failed: {e}")

    return "\n\n".join(summaries)


def summarize_chunk(text: str, model: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", 
             "content": 
             (
                "You are a helpful assistant that summarizes emails."
                "Return a clear, concise summary that is no more than a 5-minute read."
                "Use resources as you see fit, like adding titles to paragraphs, or using bullet points, or numbered lists, etc"
                "Whatever you find useful to make it clear, emphasize the concept and speed up readability."
             )
            },
            {"role": "user", "content": text},
        ],
        temperature=0.5,
        max_tokens=RESERVED_OUTPUT_TOKENS,
    )
    return response.choices[0].message.content.strip()
