from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file early
load_dotenv()

class Settings(BaseSettings):
    # the list must match env vars (case sensitive)
    openai_api_key: str
    gmail_user: str
    gmail_app_password: str
    search_subject: str = ""
    since_date: str = "01-May-2025"
    before_date: str = "11-May-2025"
    email_recipient: str

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
