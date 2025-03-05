import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

class DatabaseService:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv('MYSQL_HOST')
        self.port = os.getenv('MYSQL_PORT')
        self.user = os.getenv('MYSQL_USER')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.database = os.getenv('MYSQL_DATABASE')
        self.engine = self.create_engine()
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def create_engine(self):
        connection_string = f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        return create_engine(connection_string)

    def get_session(self):
        return self.Session()

    def close_session(self):
        self.Session.remove()

    def execute_query(self, query):
        with self.get_session() as session:
            result = session.execute(query)
            session.commit()
            return result

    def fetch_all(self, query):
        with self.get_session() as session:
            result = session.execute(query)
            return result.fetchall()

# Example usage
if __name__ == "__main__":
    db_service = DatabaseService()
    session = db_service.get_session()
    # Perform database operations using session
    db_service.close_session()