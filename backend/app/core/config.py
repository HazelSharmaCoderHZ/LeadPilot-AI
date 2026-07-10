from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    ENVIRONMENT: str
    API_V1_PREFIX: str
    DEBUG: bool
    HOST: str
    PORT: int

    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()