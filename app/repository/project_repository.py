from typing import Optional, Dict, Any
from databases import Database
from sqlalchemy import select, insert, update, delete

from app.models.project import project


class ProjectRepository:
    def __init__(self, db: Database):
        self.db = db

    async def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        query = select(project).where(project.c.id == id)
        result = await self.db.fetch_one(query)
        return dict(result) if result else None

    async def create(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        query = insert(project).values(**project_data).returning(project)
        result = await self.db.fetch_one(query)
        return dict(result)

    async def update(self, id: int, project_data: Dict[str, Any]) -> Dict[str, Any]:
        query = (
            update(project)
            .where(project.c.id == id)
            .values(**project_data)
            .returning(project)
        )
        result = await self.db.fetch_one(query)
        return dict(result)

    async def delete(self, id: int) -> Dict[str, Any]:
        query = delete(project).where(project.c.id == id).returning(project)
        result = await self.db.fetch_one(query)
        return dict(result)
