from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..core.config import settings # Import our settings
from typing import Iterator # <-- Import Iterator for type hinting

# Create the SQLAlchemy 'engine'
# This is the main connection point to our database.
# It uses the DATABASE_URL from our settings.
engine = create_engine(settings.DATABASE_URL)

# Create a 'SessionLocal' class
# This class is a "factory" for creating new database sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Iterator[Session]:
    """
    This is a FastAPI dependency function.
    It creates a new database session for a single API request,
    gives it to the endpoint, and then *always* closes it,
    even if an error occurs.
    """
    db: Session = SessionLocal()
    try:
        # 'yield' is what gives the session to the endpoint
        yield db
    finally:
        # This code runs after the endpoint has finished
        db.close()

