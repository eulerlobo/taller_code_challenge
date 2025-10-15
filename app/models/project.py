from sqlalchemy import Column, Integer, String, DateTime, func

from app.database import Base

class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100))
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())