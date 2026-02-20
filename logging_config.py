import logging
import os

def setup_logging():
    os.makedirs("log",exist_ok=True)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler("log/app.log")
    file_handler.setFormatter(formatter)

    console_hander = logging.StreamHandler()
    console_hander.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_hander)