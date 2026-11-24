from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url : str = "sqlite+aiosqlite:///./clinic.db"


settings = Settings()