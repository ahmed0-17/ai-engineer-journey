from .models import Task
from datetime import datetime


class TaskManager:

    def __init__(self):
        self.tasks: list[Task] = []
        self.next_id = 1

    def create_task(
        self,
        title: str,
        description: str,
        priority: str
    ) -> Task:

        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            completed=False,
            created_at=datetime.now().isoformat()
        )

        self.tasks.append(task)
        self.next_id += 1

        return task

    def get_tasks(self) -> list[Task]:
        return self.tasks

    def get_task(self, task_id: int) -> Task | None:

        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def delete_task(self, task_id: int) -> bool:

        task = self.get_task(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def complete_task(self, task_id: int) -> bool:

        task = self.get_task(task_id)

        if task is None:
            return False

        task.completed = True
        return True

    def update_task(
        self,
        task_id: int,
        title: str,
        description: str,
        priority: str
    ) -> Task | None:

        task = self.get_task(task_id)

        if task is None:
            return None

        task.title = title
        task.description = description
        task.priority = priority

        return task




Task1=TaskManager("LEARN PYTHON","with context manager","High")
print(Task1)