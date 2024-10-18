import logging
import os
from fastapi import FastAPI
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
logger = logging.getLogger(__name__)

@app.get("/generate-log")
async def generate_log():
    logger.info("This is an info log")
    logger.debug("This is a debug log")
    logger.warning("This is a warning log")
    logger.info("This is another info log")
    logger.debug("This is another debug log")
    return {"message": "Logs generated successfully"}

@app.get("/generate-error")
async def generate_error():
    try:
        # Intentionally cause an IndexError
        my_list = [1, 2, 3]
        print(my_list[10])
    except Exception as e:
        logger.exception("An error occurred")
        raise e
    return {"message": "Error message generated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.dev_mode)
