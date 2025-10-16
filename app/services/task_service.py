from typing import List

from app.models.task import Task
from app.repository.task_repository import TaskRepository
from app.schemas.task import TaskCreate

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get_tasks_by_project_id(self, project_id: int) -> List[Task]:
        return self.task_repository.get_by_project_id(project_id)

    def create_task(self, task_data: TaskCreate) -> Task:
        task = Task(
            project_id=task_data.project_id,
            title=task_data.title,
            priority=task_data.priority,
            completed=task_data.completed,
            due_date=task_data.due_date,
        )
        return self.task_repository.create(task)