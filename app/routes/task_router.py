from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from app.database import get_db
from app.exceptions.project import ProjectNotFoundException
from app.exceptions.task import TaskNotFoundException
from app.repository.project_repository import ProjectRepository
from app.repository.task_repository import TaskRepository
from app.schemas.task import TaskUpdate, TaskResponse
from app.services.project_service import ProjectService
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_project_service(
    db: Annotated[Session, Depends(get_db)],
) -> ProjectService:
    repository = ProjectRepository(db)
    return ProjectService(repository)


def get_task_service(
    db: Annotated[Session, Depends(get_db)],
) -> TaskService:
    repository = TaskRepository(db)
    return TaskService(repository)


@router.put("/{task_id}")
async def update_task(
    task_id: Annotated[int, "The ID of the task to update"],
    task_data: TaskUpdate,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
    task_service: Annotated[TaskService, Depends(get_task_service)]
) -> TaskResponse:
    try:
        if task_data.project_id:
            project_service.get_project_by_id(task_data.project_id)

        task = task_service.update_task(task_id, task_data)
        return TaskResponse.model_validate(task)
    except ProjectNotFoundException as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=e.message)
    except TaskNotFoundException as e:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=e.message)