from src.task_app.manager import TaskManager
from src.task_app.storage import Storage


def test_create_task(tmp_path):
    manager = TaskManager()

    manager.storage = Storage(tmp_path / "tasks.json")
    manager.tasks = []
    manager.next_id = 1

    task = manager.create_task(
        "Learn Python",
        "Practice pytest",
        "High"
    )

    assert task.id == 1
    assert task.title == "Learn Python"
    assert task.description == "Practice pytest"
    assert task.priority == "High"
    assert task.completed is False


def test_get_task(tmp_path):
    manager = TaskManager()

    manager.storage = Storage(tmp_path / "tasks.json")
    manager.tasks = []
    manager.next_id = 1

    created_task = manager.create_task(
        "Learn Python",
        "Practice pytest",
        "High"
    )

    task = manager.get_task(created_task.id)

    assert task is not None
    assert task.id == created_task.id


def test_complete_task(tmp_path):
    manager = TaskManager()

    manager.storage = Storage(tmp_path / "tasks.json")
    manager.tasks = []
    manager.next_id = 1

    task = manager.create_task(
        "Learn Python",
        "Practice pytest",
        "High"
    )

    result = manager.complete_task(task.id)

    assert result is True
    assert task.completed is True


def test_update_task(tmp_path):
    manager = TaskManager()

    manager.storage = Storage(tmp_path / "tasks.json")
    manager.tasks = []
    manager.next_id = 1

    task = manager.create_task(
        "Learn Python",
        "Practice pytest",
        "High"
    )

    updated_task = manager.update_task(
        task.id,
        "Learn Pytest",
        "Write unit tests",
        "Medium"
    )

    assert updated_task is not None
    assert updated_task.title == "Learn Pytest"
    assert updated_task.description == "Write unit tests"
    assert updated_task.priority == "Medium"


def test_delete_task(tmp_path):
    manager = TaskManager()

    manager.storage = Storage(tmp_path / "tasks.json")
    manager.tasks = []
    manager.next_id = 1

    task = manager.create_task(
        "Learn Python",
        "Practice pytest",
        "High"
    )

    result = manager.delete_task(task.id)

    assert result is True
    assert manager.get_task(task.id) is None