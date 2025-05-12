from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    gmail_user: str
    gmail_app_password: str
    localai_model: str = "meta-llama-3-8b-instruct" #"llama-3-8b-instruct-q4_K_M"
    localai_base_url: str = "http://localhost:8080/v1"
    search_subject: str = ""
    since_date: str = "01-May-2025"
    before_date: str = "11-May-2025"
    email_recipient: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
