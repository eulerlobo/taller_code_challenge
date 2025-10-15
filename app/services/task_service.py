from typing import List

from app.models.task import Task
from app.repository.task_repository import TaskRepository

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get_tasks_by_project_id(self, project_id: int) -> List[Task]:
        return self.task_repository.get_by_project_id(project_id)
