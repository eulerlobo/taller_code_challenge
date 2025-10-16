from sqlalchemy import Table, Column, Integer, String, DateTime, func

from app.database import metadata

project = Table(
    "project",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("description", String(100)),
    Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
)