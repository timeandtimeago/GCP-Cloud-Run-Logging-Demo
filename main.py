import logging
import os
from fastapi import FastAPI
from config import settings
import logging_config

print("dev_mode: ", settings.dev_mode)

logger = logging.getLogger(__name__)

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
    uvicorn.run("main:app", log_config=None, host="0.0.0.0", port=8000, reload=settings.dev_mode)
