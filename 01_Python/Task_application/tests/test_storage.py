from src.task_app.storage import Storage
from src.task_app.models import Task


def test_save_and_load_tasks(tmp_path):
    data_file = tmp_path / "tasks.json"
    storage = Storage(data_file)

    tasks = [
        Task(
            id=1,
            title="Learn Python",
            description="Practice testing",
            priority="High",
            completed=False,
            created_at="2026-10-02T22:00:00"
        )
    ]

    storage.save_tasks(tasks)

    loaded_tasks = storage.load_tasks()

    assert len(loaded_tasks) == 1
    assert loaded_tasks[0].id == 1
    assert loaded_tasks[0].title == "Learn Python"
    assert loaded_tasks[0].description == "Practice testing"
    assert loaded_tasks[0].priority == "High"
    assert loaded_tasks[0].completed is False