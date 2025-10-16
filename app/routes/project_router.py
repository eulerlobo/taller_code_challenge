from typing import Annotated, List

from databases import Database
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from app.database import get_db
from app.exceptions.project import ProjectNotFoundException
from app.repository.project_repository import ProjectRepository
from app.repository.task_repository import TaskRepository
from app.schemas.project import ProjectResponse, ProjectCreate, ProjectUpdate
from app.schemas.task import TaskResponse, TaskCreate
from app.services.project_service import ProjectService
from app.services.task_service import TaskService

router = APIRouter(prefix="/projects", tags=["projects"])

async def get_project_service(
    db: Annotated[Database, Depends(get_db)],
) -> ProjectService:
    repository = ProjectRepository(db)
    return ProjectService(repository)

async def get_task_service(
    db: Annotated[Database, Depends(get_db)],
) -> TaskService:
    repository = TaskRepository(db)
    return TaskService(repository)

@router.post("/")
async def insert_project(
    project_data: ProjectCreate,
    project_service: Annotated[ProjectService, Depends(get_project_service)]
) -> ProjectResponse:
    project = await project_service.create_project(project_data)
    return ProjectResponse.model_validate(project)


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: Annotated[int, Path(description="ID of the project to retrieve")],
    project_service: Annotated[ProjectService, Depends(get_project_service)],
) -> ProjectResponse:
    try:
        project = await project_service.get_project_by_id(project_id)
        return ProjectResponse.model_validate(project)
    except ProjectNotFoundException as e:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=e.message
        ) from e


@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: Annotated[int, Path(description="ID of the project to update")],
    project_data: ProjectUpdate,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
) -> ProjectResponse:
    if project_data.name is None and project_data.description is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="No fields to update")

    try:
        project = await project_service.update_project(project_id, project_data)
        return ProjectResponse.model_validate(project)
    except ProjectNotFoundException as e:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=e.message
        ) from e

@router.delete("/{project_id}")
async def delete_project(
    project_id: Annotated[int, Path(description="ID of the project to delete")],
    project_service: Annotated[ProjectService, Depends(get_project_service)],
) -> ProjectResponse:
    try:
        project = await project_service.delete_project(project_id)
        return ProjectResponse.model_validate(project)
    except ProjectNotFoundException as e:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=e.message
        ) from e


@router.get("/{project_id}/tasks", response_model=List[TaskResponse])
async def get_project_tasks(
    project_id: Annotated[int, Path(description="ID of the project")],
    project_service: Annotated[ProjectService, Depends(get_project_service)],
    task_service: Annotated[TaskService, Depends(get_task_service)],
) -> List[TaskResponse]:
    # TODO: Implement pagination and sorted by priority
    try:
        await project_service.get_project_by_id(project_id)
        tasks = await task_service.get_tasks_by_project_id(project_id)
        return [TaskResponse.model_validate(task) for task in tasks]
    except ProjectNotFoundException as e:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=e.message
        ) from e

@router.post("/{project_id}/tasks")
async def insert_task(
    task_data: TaskCreate,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
    task_service: Annotated[TaskService, Depends(get_task_service)],
) -> TaskResponse:
    try:
        await project_service.get_project_by_id(task_data.project_id)
        task = await task_service.create_task(task_data)
        return TaskResponse.model_validate(task)
    except ProjectNotFoundException as e:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=e.message
        ) from e
