import tiktoken

def count_tokens(text: str, model: str = "gpt-3.5-turbo-0125") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def chunk_text(text: str, model: str, max_tokens: int, overlap: int = 0) -> list[str]:
    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0")
    if overlap >= max_tokens:
        raise ValueError("overlap must be smaller than max_tokens")

    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    total_tokens = len(tokens)

    chunks = []
    start = 0
    chunk_num = 0

    while start < total_tokens:
        end = min(start + max_tokens, total_tokens)
        chunk_tokens = tokens[start:end]
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)

        chunk_num += 1
        print(f" → Chunk {chunk_num}: tokens {start}-{end} ({len(chunk_tokens)} tokens)")

        if end == total_tokens:
            break  # ✅ we're done

        start = end - overlap  # ✅ move forward with overlap

    return chunks
