import os

from dotenv import load_dotenv
from databases import Database
from sqlalchemy import MetaData

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)

metadata = MetaData()

async def get_db() -> Database:
    return database