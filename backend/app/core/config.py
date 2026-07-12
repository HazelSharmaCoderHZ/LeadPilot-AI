from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    ENVIRONMENT: str
    API_V1_PREFIX: str
    DEBUG: bool
    HOST: str
    PORT: int
    FIRECRAWL_API_KEY: str
    GEMINI_API_KEY: str
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str
    GEMINI_MODEL: str = "gemini-3.1-flash-lite"
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()