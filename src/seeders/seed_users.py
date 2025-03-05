import os
from faker import Faker
from sqlalchemy.orm import sessionmaker
from services.database_service import DatabaseService
from models.user_model import User

# Initialize Faker
fake = Faker()

# Initialize DatabaseService
db_service = DatabaseService()
Session = sessionmaker(bind=db_service.engine)
session = Session()

def seed_users(num_users):
    for _ in range(num_users):
        fake_user = User(
            username=fake.user_name(),
            email=fake.email(),
            created_at=fake.date_time_this_decade()
        )
        session.add(fake_user)
    session.commit()

if __name__ == "__main__":
    num_users = 10  # Number of fake users to generate
    seed_users(num_users)
    print(f"Seeded {num_users} fake users.")
    session.close()