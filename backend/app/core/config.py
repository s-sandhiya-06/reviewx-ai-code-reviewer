from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ReviewX"
    APP_ENV: str = "development"
    DEBUG: bool = True

    DATABASE_URL: str

    # GitHub App Configuration
    GITHUB_APP_ID: int
    GITHUB_PRIVATE_KEY_PATH: str
    GITHUB_WEBHOOK_SECRET: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()