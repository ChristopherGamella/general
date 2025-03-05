from sqlalchemy.orm import Session
from ..models import MyTable  # Import your SQLAlchemy models
from services.database_service import engine, SessionLocal # Your database connection/session

def seed_data(db: Session):
    # Example seed data
    records = [
        MyTable(name="Seed Record 1"),
        MyTable(name="Seed Record 2"),
        # Add more records
    ]

    for record in records:
        db.add(record)
    db.commit()

def run_seed():
    db = SessionLocal()
    try:
        seed_data(db)
        print("Seed data added successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error seeding data: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    run_seed()