from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100))
    create_at = Column(DateTime(timezone=True), nullable=False)