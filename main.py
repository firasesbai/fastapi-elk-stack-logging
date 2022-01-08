import logging

import uvicorn
import uuid

from fastapi import FastAPI
from logging_setup import setup_root_logger

# setup root logger
setup_root_logger()

# Get logger for module
LOGGER = logging.getLogger(__name__)


LOGGER.info("---Starting App---")

app = FastAPI()


@app.get("/random_uuid")
async def root():
    LOGGER.info(str(uuid.uuid4()))
    return "OK"

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)
