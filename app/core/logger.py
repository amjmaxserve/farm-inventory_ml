import logging
import os

os.makedirs(
    "logs",
    exist_ok=True
)

def get_logger(name):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        f"logs/{name}.log"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(
        logging.StreamHandler()
    )

    return logger