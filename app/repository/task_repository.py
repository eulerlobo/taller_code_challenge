from typing import List

from app.models.task import Task

class TaskRepository:
    def __init__(self, db):
        self.db = db

    def get_by_project_id(self, project_id: int) -> List[Task]:
        return self.db.query(Task).filter(Task.project_id == project_id).all()
