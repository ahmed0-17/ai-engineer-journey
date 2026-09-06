import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
console_handler = logging.StreamHandler()

file_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("Debug information")
logger.info("User logged in")
logger.warning("Low storage")
logger.error("Database failed")
logger.critical("System crashed")