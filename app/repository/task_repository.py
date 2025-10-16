from typing import List

from app.models.task import Task

class TaskRepository:
    def __init__(self, db):
        self.db = db

    def get_by_project_id(self, project_id: int) -> List[Task]:
        return self.db.query(Task).filter(Task.project_id == project_id).all()

    def get_by_id(self, id):
        return self.db.query(Task).filter(Task.id == id).first()

    def create(self, task: Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update(self, task: Task) -> Task:
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task: Task) -> Task:
        self.db.delete(task)
        self.db.commit()
        return task