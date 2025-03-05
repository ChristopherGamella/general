import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.mysql_host = os.getenv('MYSQL_HOST')
        self.mysql_port = os.getenv('MYSQL_PORT')
        self.mysql_user = os.getenv('MYSQL_USER')
        self.mysql_password = os.getenv('MYSQL_PASSWORD')
        self.mysql_database = os.getenv('MYSQL_DATABASE')