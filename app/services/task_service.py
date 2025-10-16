from typing import List

from app.exceptions.task import TaskNotFoundException
from app.models.task import Task
from app.repository.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get_tasks_by_project_id(self, project_id: int) -> List[Task]:
        return self.task_repository.get_by_project_id(project_id)

    def get_task_by_id(self, task_id: int) -> Task:
        task = self.task_repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundException(task_id)
        return task

    def create_task(self, task_data: TaskCreate) -> Task:
        task = Task(
            project_id=task_data.project_id,
            title=task_data.title,
            priority=task_data.priority,
            completed=task_data.completed,
            due_date=task_data.due_date,
        )
        return self.task_repository.create(task)

    def update_task(self, task_id, task_data: TaskUpdate) -> Task:
        task = self.get_task_by_id(task_id)

        if task_data.project_id is not None:
            task.project_id = task_data.project_id
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.priority is not None:
            task.priority = task_data.priority
        if task_data.completed is not None:
            task.completed = task_data.completed
        if task_data.due_date is not None:
            task.due_date = task_data.due_date

        return self.task_repository.update(task)