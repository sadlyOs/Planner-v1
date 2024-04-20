import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, BaseModel

ENV_FILE_DIR = os.path.abspath(".")


class Config(BaseSettings):
    BOT_TOKEN: SecretStr
    host: str
    port: int
    user: SecretStr
    password: SecretStr
    db: SecretStr


    @property
    def url(self):
        return f"sqlite+aiosqlite:///db.sqlite3"


    @property
    async def bot_token(self):
        return self.BOT_TOKEN.get_secret_value()

    model_config = SettingsConfigDict(
        env_file=f"{ENV_FILE_DIR}/.env",
        env_file_encoding='utf-8'
        
    )

config = Config()