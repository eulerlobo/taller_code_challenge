from pydantic import BaseModel, ConfigDict

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    create_at: str

    model_config = ConfigDict(from_attributes=True)