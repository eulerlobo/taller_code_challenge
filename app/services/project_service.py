from datetime import timezone, datetime

from app.exceptions.project import ProjectNotFoundException
from app.models import Project
from app.repository.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectUpdate

class ProjectService:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def get_project_by_id(self, project_id: int) -> Project:
        project = self.project_repository.get_by_id(project_id)
        if not project:
            raise ProjectNotFoundException(project_id)
        return project

    def create_project(self, project_data: ProjectCreate) -> Project:
        now = datetime.now(timezone.utc)
        project = Project(
            name=project_data.name,
            description=project_data.description,
            created_at=now
        )
        return self.project_repository.create(project)

    def update_project(self, project_id: int, project_data: ProjectUpdate) -> Project:
        project = self.get_project_by_id(project_id)

        if project_data.name is not None:
            project.name = project_data.name
        if project_data.description is not None:
            project.description = project_data.description

        return self.project_repository.update(project)

    def delete_project(self, project_id: int) -> Project:
        project = self.get_project_by_id(project_id)
        return self.project_repository.delete(project)