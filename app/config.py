from pydantic_settings import BaseSettings
from pydantic import Field
import logging

class Settings(BaseSettings):
    dev_mode: bool = Field(default=False, env='DEV_MODE')

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
