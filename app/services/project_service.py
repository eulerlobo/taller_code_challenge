from datetime import timezone, datetime

from app.models import Project
from app.repository.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate


class ProjectService:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def get_project_by_id(self, project_id: int) -> Project:
        project = self.project_repository.get_by_id(project_id)
        if not project:
            raise Exception("Project not found")
        return project

    def create_project(self, project_data: ProjectCreate) -> Project:
        now = datetime.now(timezone.utc)
        project = Project(
            name=project_data.name,
            description=project_data.description,
            created_at=now
        )
        return self.project_repository.create(project)