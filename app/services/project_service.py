from typing import Dict, Any

from app.exceptions.project import ProjectNotFoundException
from app.repository.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectUpdate

class ProjectService:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    async def get_project_by_id(self, project_id: int) -> Dict[str, Any]:
        project = await self.project_repository.get_by_id(project_id)
        if not project:
            raise ProjectNotFoundException(project_id)
        return project

    async def create_project(self, project_data: ProjectCreate) -> Dict[str, Any]:
        project_dict = {
            "name": project_data.name,
            "description": project_data.description,
        }
        return await self.project_repository.create(project_dict)

    async def update_project(self, project_id: int, project_data: ProjectUpdate) -> Dict[str, Any]:
        await self.get_project_by_id(project_id)

        update_dict = {}
        if project_data.name is not None:
            update_dict["name"] = project_data.name
        if project_data.description is not None:
            update_dict["description"] = project_data.description

        return await self.project_repository.update(project_id, update_dict)

    async def delete_project(self, project_id: int) -> Dict[str, Any]:
        await self.get_project_by_id(project_id)
        return await self.project_repository.delete(project_id)