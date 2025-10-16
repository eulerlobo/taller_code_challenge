from sqlalchemy import Table, Column, Integer, Boolean, ForeignKey, String, DateTime

from app.database import metadata

task = Table(
    "task",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("project_id", Integer, ForeignKey("project.id"), nullable=False),
    Column("title", String(100), nullable=False),
    Column("priority", Integer, nullable=False, default=0),
    Column("completed", Boolean, nullable=False, default=False),
    Column("due_date", DateTime(timezone=True), nullable=True),
)