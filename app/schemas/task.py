from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

class TaskResponse(BaseModel):
    """Schema for task response"""
    id: int
    project_id: int
    title: str
    priority: int
    complete: bool
    due_data: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
