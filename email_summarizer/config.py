from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    gmail_user: str
    gmail_app_password: str
    localai_model: str = "llama-3-8b-instruct-q4_K_M"
    localai_base_url: str = "http://localhost:8080/v1"
    search_subject: str = ""
    since_date: str = "2025-05-01"
    before_date: str = "2025-05-11"

    class Config:
        env_file = ".env"

settings = Settings()
