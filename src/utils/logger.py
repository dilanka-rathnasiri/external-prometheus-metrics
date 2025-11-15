import logging
from logging import Logger


def get_logger() -> Logger:
    logger = logging.getLogger()

    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger


logger = get_logger()
