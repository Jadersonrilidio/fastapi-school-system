from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DB_ENGINE: str = Field(...)
    DB_USER: str = Field(...)
    DB_PASSWORD: str = Field(...)
    DB_HOST: str = Field(...)
    DB_NAME: str = Field(...)

    @property
    def DATABASE_URL(self) -> str:
        return (f"{self.DB_ENGINE}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }
