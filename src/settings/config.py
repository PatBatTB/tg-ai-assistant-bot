from pathlib import Path

from pydantic import BaseModel, SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

_BASE_DIR = Path(__file__).resolve().parent.parent.parent
_ENV_FILE = str(_BASE_DIR / ".env")

class TgBotSettings(BaseModel):
    token: SecretStr

class ProxySettings(BaseModel):
    type: str = Field("")
    host: str = Field("")
    port: int = Field(0)

    def get_url(self):
        if self.type and self.host and self.port:
            return f"{self.type}://{self.host}:{self.port}"
        else:
            return None

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_ENV_FILE,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore"
    )

    tg_bot: TgBotSettings
    proxy: ProxySettings


@lru_cache
def get_settings() -> Settings:
    return Settings()
