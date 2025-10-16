from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import database
from app.routes.project_router import router as project_router
from app.routes.task_router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(
    title="Taller challenge",
    description="Taller challenge API",
    lifespan=lifespan,
)

# Routers
app.include_router(project_router)
app.include_router(task_router)


@app.get("/")
def root():
    return {
        "online": True,
        "documentation": "/docs"
    }

