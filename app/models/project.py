from sqlachemy import Column, Integer, String, Datetime

class Project(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100))
    create_at = Column(Datetime(timezone=True), nullable=False)