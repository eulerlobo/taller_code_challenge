from typing import List, Optional, Dict, Any
from databases import Database
from sqlalchemy import select, insert, update, delete

from app.models.task import task


class TaskRepository:
    def __init__(self, db: Database):
        self.db = db

    async def get_by_project_id(self, project_id: int) -> List[Dict[str, Any]]:
        query = (
            "SELECT id, project_id, title, priority, completed, due_date "
            "FROM task "
            "WHERE project_id = :project_id "
            "ORDER BY priority DESC"
        )
        results = await self.db.fetch_all(query, {"project_id": project_id})
        return [dict(row) for row in results]

    async def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        query = select(task).where(task.c.id == id)
        result = await self.db.fetch_one(query)
        return dict(result) if result else None

    async def create(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        query = insert(task).values(**task_data).returning(task)
        result = await self.db.fetch_one(query)
        return dict(result)

    async def update(self, id: int, task_data: Dict[str, Any]) -> Dict[str, Any]:
        query = (
            update(task)
            .where(task.c.id == id)
            .values(**task_data)
            .returning(task)
        )
        result = await self.db.fetch_one(query)
        return dict(result)

    async def delete(self, id: int) -> Dict[str, Any]:
        query = delete(task).where(task.c.id == id).returning(task)
        result = await self.db.fetch_one(query)
        return dict(result)
