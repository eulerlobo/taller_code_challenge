from app.models.project import Project

class ProjectRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id(self, id):
        return self.db.query(Project).filter(Project.id == id).first()