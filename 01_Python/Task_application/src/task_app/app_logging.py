import logging
from pathlib import Path


def get_logger():
 log_dir=Path("logs")
 log_dir.mkdir(exist_ok=True,parents=True)
 log_file= log_dir / "app.log"
 log_file.touch()


 logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
 return logging.getLogger("task_app")




logger=get_logger()

