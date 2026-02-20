import logging
from app.config import settings

def setup_logging():
    level = logging.DEBUG if settings.ENV == "dev" else logging.INFO

    logging.basicConfig(
        level = level,
        format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )