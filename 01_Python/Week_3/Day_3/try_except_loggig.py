import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

try:
    result = 10 / 0
    logger.info("Calculation successful")

except ZeroDivisionError:
    # logger.error("Cannot divide by zero")
    logger.exception("Cannot divide by zero")