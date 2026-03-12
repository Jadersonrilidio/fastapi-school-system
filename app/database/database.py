from app.database import Base
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker


class DataBase():

    def __init__(self, database_url: str) -> None:
        self.Engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(bind=self.Engine, autoflush=False, autocommit=False)

    def get_session_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def create_tables(self):
        Base.metadata.create_all(bind=self.Engine)

    def drop_tables(self):
        Base.metadata.drop_all(bind=self.Engine)
