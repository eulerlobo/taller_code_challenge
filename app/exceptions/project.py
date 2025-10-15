class ProjectNotFoundException(Exception):
    def __init__(self, project_id: int):
        self.project_id = project_id
        self.message = f"Project with id {project_id} not found"
        super().__init__(self.message)