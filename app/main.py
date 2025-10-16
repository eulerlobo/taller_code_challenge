from fastapi import FastAPI
from app.routes.project_router import router as project_router
from app.routes.task_router import router as task_router

app = FastAPI(
    title="Taller challenge",
    description="Taller challenge API",
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

