import logging
from pathlib import Path


def get_logger():
 BASE_DIR = Path(__file__).resolve().parents[2]

 LOG_DIR = BASE_DIR / "logs"
 LOG_DIR.mkdir(exist_ok=True)

 LOG_FILE = LOG_DIR / "app.log"

 logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
 return logging.getLogger("task_app")




logger=get_logger()

