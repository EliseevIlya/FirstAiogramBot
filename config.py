import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TOKEN: str
    ADMINS: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()


def update_env_file(key: str, value: str):
    """Обновляет переменную в .env файле"""
    with open(".env", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(".env", "w", encoding="utf-8") as file:
        found = False
        for line in lines:
            if line.strip().startswith(f"{key}="):
                file.write(f"{key}={value}\n")
                found = True
            else:
                file.write(line)
        if not found:
            file.write(f"{key}={value}\n")
