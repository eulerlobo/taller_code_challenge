from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class TaskCreate(BaseModel):
    project_id: int
    title: str = Field(..., min_length=1, max_length=100)
    priority: int
    completed: bool = False
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    project_id: Optional[int] = None
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    priority: Optional[int] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    """Schema for task response"""
    id: int
    project_id: int
    title: str
    priority: int
    completed: bool
    due_date: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
