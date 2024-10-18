from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    dev_mode: bool = Field(default=False, env='DEV_MODE')

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()

app = FastAPI()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if settings.dev_mode else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
