from .models import Task
from datetime import datetime
from .storage import Storage
from .app_logging import get_logger
class TaskManager:

    def __init__(self):
        self.storage=Storage()
        self.tasks: list[Task] = self.storage.load_tasks()
        self.logger = get_logger()

        # setting id dynamically
        if self.tasks:
            self.next_id = max(task.id for task in self.tasks) + 1
        else:
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
        self.storage.save_tasks(self.tasks)
        self.logger.info("Task Created successfully")
        return task

    def get_tasks(self) -> list[Task]:
        self.logger.info(f"{len(self.tasks)} tasks fetched successfully")
        return self.tasks

    def get_task(self, task_id: int) -> Task | None:

        for task in self.tasks:
            if task.id == task_id:
                self.logger.info(f"Task fetched successfully having ID {task_id}") 
                return task
        self.logger.warning(f"Task not found with ID {task_id}")  
        return None

    def delete_task(self, task_id: int) -> bool:

        task = self.get_task(task_id)
         
        if task is None:
            self.logger.warning(f"Task not found with ID {task_id}")
            return False

        self.tasks.remove(task)
        self.storage.save_tasks(self.tasks)
        self.logger.info(f"Task deleted successfully having ID {task_id}")
        return True

    def complete_task(self, task_id: int) -> bool:

        task = self.get_task(task_id)

        if task is None:
            self.logger.warning(f"Task not found with ID {task_id}")
            return False

        task.completed = True
        self.storage.save_tasks(self.tasks)
        self.logger.info(f"Task Completed successfully having ID {task_id}")
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
            self.logger.warning(f"Task not found with ID {task_id}") 
            return None

        task.title = title
        task.description = description
        task.priority = priority
        self.storage.save_tasks(self.tasks)
        self.logger.info(f"Task updated successfully having ID {task_id}")
        return task




