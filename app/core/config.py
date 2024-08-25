# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    sqlalchemy_database_uri: str  # Make sure this matches the environment variable
    debug: bool = True

    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra fields if needed

settings = Settings()
