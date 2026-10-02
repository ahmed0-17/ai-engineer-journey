import json
from pathlib import Path
from dataclasses import asdict

from .models import Task


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DATA_FILE = DATA_DIR / "tasks.json"


class Storage:

    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file

    def save_tasks(self, tasks):
        data = [asdict(task) for task in tasks]

        with open(self.data_file, "w") as info:
            json.dump(data, info, indent=4)

    def load_tasks(self):
        if not self.data_file.exists():
            return []

        with open(self.data_file, "r") as info:
            data = json.load(info)

        return [Task(**item) for item in data]