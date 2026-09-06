import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s -%(name)s- %(levelname)s - %(message)s"
    )

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("Low storage")
logger.error("Databae failed")
logger.debug("Debug Message")
logger.critical("System crashed")