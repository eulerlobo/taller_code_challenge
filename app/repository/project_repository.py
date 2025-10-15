from app.models.project import Project

class ProjectRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id(self, id):
        return self.db.query(Project).filter(Project.id == id).first()

    def create(self, project: Project) -> Project:
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project