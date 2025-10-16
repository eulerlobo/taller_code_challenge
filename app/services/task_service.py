from typing import List, Dict, Any

from app.exceptions.task import TaskNotFoundException
from app.repository.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def get_tasks_by_project_id(self, project_id: int) -> List[Dict[str, Any]]:
        return await self.task_repository.get_by_project_id(project_id)

    async def get_task_by_id(self, task_id: int) -> Dict[str, Any]:
        task = await self.task_repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundException(task_id)
        return task

    async def create_task(self, task_data: TaskCreate) -> Dict[str, Any]:
        task_dict = {
            "project_id": task_data.project_id,
            "title": task_data.title,
            "priority": task_data.priority,
            "completed": task_data.completed,
            "due_date": task_data.due_date,
        }
        return await self.task_repository.create(task_dict)

    async def update_task(self, task_id: int, task_data: TaskUpdate) -> Dict[str, Any]:
        await self.get_task_by_id(task_id)

        update_dict = {}
        if task_data.project_id is not None:
            update_dict["project_id"] = task_data.project_id
        if task_data.title is not None:
            update_dict["title"] = task_data.title
        if task_data.priority is not None:
            update_dict["priority"] = task_data.priority
        if task_data.completed is not None:
            update_dict["completed"] = task_data.completed
        if task_data.due_date is not None:
            update_dict["due_date"] = task_data.due_date

        return await self.task_repository.update(task_id, update_dict)

    async def delete_task(self, task_id: int) -> Dict[str, Any]:
        await self.get_task_by_id(task_id)
        return await self.task_repository.delete(task_id)