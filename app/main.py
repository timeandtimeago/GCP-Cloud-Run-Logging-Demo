import os
from fastapi import FastAPI
from config import settings

### Logging
import logging
import logging.config
from logging_config import get_logging_config

logging_config = get_logging_config(dev_mode=settings.dev_mode, format_gcp=True)
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

logging.info(f"application dev_mode: {settings.dev_mode}")

app = FastAPI()

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
        raise e
    return {"message": "Error message generated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", log_config=None, port=8000, reload=settings.dev_mode)
