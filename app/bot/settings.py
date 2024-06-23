import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_PATH = Path(os.getcwd()) / ".env"


class TgSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="TG_", env_file=ENV_PATH, extra="ignore"
    )

    TOKEN: str = ""


class BackendSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="BACKEND_", env_file=ENV_PATH, extra="ignore"
    )

    HOST: str = ""
    PORT: int = 8000


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_", env_file=ENV_PATH, extra="ignore"
    )

    DEBUG: bool = False

    TG: TgSettings = TgSettings()
    BACKEND: BackendSettings = BackendSettings()


settings: AppSettings = AppSettings()
