from fastapi import FastAPI
from app.routes.project_router import router as project_router

app = FastAPI(
    title="Taller challenge",
    description="Taller challenge API",
)

# Routers
app.include_router(project_router)

@app.get("/")
def root():
    return {
        "online": True,
        "documentation": "/docs"
    }

