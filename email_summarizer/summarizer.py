from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_text_splitters import CharacterTextSplitter
from .email_summarizer.config import settings

def initialize_llm():
    return ChatOpenAI(
        temperature=0.1,
        model=settings.localai_model,
        base_url=settings.localai_base_url,
        api_key="none"  # LocalAI does not require a real key
    )

def summarize_text(text: str) -> str:
    text_splitter = CharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=500
    )
    docs = [Document(page_content=chunk) for chunk in text_splitter.split_text(text)]
    summary_chain = load_summarize_chain(
        initialize_llm(),
        chain_type="map_reduce"
    )
    return summary_chain.invoke(docs)['output_text']
