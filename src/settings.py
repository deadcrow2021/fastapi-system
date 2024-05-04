from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str
    postgres_debug: bool

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')


settings = Settings()
