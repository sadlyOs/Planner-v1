import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

ENV_FILE_DIR = os.path.abspath(".")

class Config(BaseSettings):
    BOT_TOKEN: SecretStr
    host: SecretStr
    port: SecretStr
    user: SecretStr
    password: SecretStr
    db: SecretStr

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


    @property
    async def bot_token(self):
        return self.BOT_TOKEN.get_secret_value()

    model_config = SettingsConfigDict(
        env_file=f"{ENV_FILE_DIR}/.env",
        env_file_encoding='utf-8'
    )