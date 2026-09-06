import logging
from calculator import division

logging.basicConfig(
    level=logging.INFO,
    filename="01_Python/Week_3/Day_3/logging_project/app.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

division(2,"a")