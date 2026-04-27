from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:password@db:5432/bookstore"

    class Config:
        env_file = ".env"

settings = Settings()