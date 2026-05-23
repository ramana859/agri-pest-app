from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AgriPest - Vegetable Pest Advisor"
    VERSION: str = "0.1.0"
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/agri_db"  # We'll set up DB later
    MODEL_PATH: str = "app/models/"

settings = Settings()
