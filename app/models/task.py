from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, DateTime

from app.database import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    title = Column(String(100), nullable=False)
    priority = Column(Integer, nullable=False, default=0)
    complete = Column(Boolean, nullable=False, default=False)
    due_data = Column(DateTime(timezone=True), nullable=True)