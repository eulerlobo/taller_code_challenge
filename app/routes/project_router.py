from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app.database import get_db
from app.repository.project_repository import ProjectRepository
from app.schemas.project import ProjectResponse
from app.services.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])

def get_project_service(
    db: Annotated[Session, Depends(get_db)],
) -> ProjectService:
    repository = ProjectRepository(db)
    return ProjectService(repository)

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: Annotated[int, Path(description="ID of the project to retrieve")],
    project_service: Annotated[ProjectService, Depends(get_project_service)],
) -> ProjectResponse:
    try:
        project = project_service.get_project_by_id(project_id)

        return ProjectResponse.model_validate(project)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Project not found")