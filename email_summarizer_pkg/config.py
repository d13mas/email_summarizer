from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file early
load_dotenv()

class Settings(BaseSettings):
    # the list must match env vars (case sensitive)
    openai_api_key: str
    gmail_user: str
    gmail_app_password: str
    email_recipient: str

    allowed_senders: list[str] = []
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

# Hardcoded list of allowed senders to summarize
settings.allowed_senders = [
        settings.email_recipient
        # "pragmaticengineer+deepdives@substack.com",
        # "will@lethain.com",
        # "scarletink@substack.com",
        # "pragmaticengineer+the-pulse@substack.com",
        # "bytebytego@substack.com",
    ]
