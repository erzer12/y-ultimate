"""
Database Session Management

This file sets up SQLAlchemy to connect to PostgreSQL and provides a
FastAPI dependency for getting database sessions.

Key concepts:
  1. Engine: The starting point for any SQLAlchemy application. It represents
     the connection to the database.
  
  2. SessionLocal: A factory for creating new database sessions. Each request
     will get its own session.
  
  3. get_db(): A FastAPI dependency that provides a database session to route
     functions. It ensures the session is always closed, even if an error occurs.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create the database engine
# This connects to the database using the URL from your settings (which reads from .env)
# 
# connect_args={"check_same_thread": False} is only needed for SQLite.
# For PostgreSQL, we don't need it, but it's harmless to leave out.
engine = create_engine(
    settings.DATABASE_URL,
    # pool_pre_ping=True ensures that database connections are valid before using them
    pool_pre_ping=True,
)

# SessionLocal is a factory for creating database sessions
# Each session represents a "conversation" with the database.
# autocommit=False: Changes aren't saved until you call session.commit()
# autoflush=False: Changes aren't sent to the database until you commit
# bind=engine: This session factory will use the engine we created above
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    FastAPI Dependency for Database Sessions
    
    This function is a "dependency" that FastAPI can inject into route functions.
    It creates a new database session for each request and ensures it's closed
    when the request is complete.
    
    Usage in a route:
        @app.get("/users/")
        def read_users(db: Session = Depends(get_db)):
            users = db.query(User).all()
            return users
    
    The "yield" keyword makes this a generator, which allows FastAPI to run
    code after the request is complete (the "finally" block).
    
    Why this pattern is important:
      - Each request gets its own session (thread-safe)
      - Sessions are always closed, preventing memory leaks
      - Even if an exception occurs, the "finally" block runs
    """
    db = SessionLocal()
    try:
        # The session is yielded to the route function
        yield db
    finally:
        # After the route function completes (or errors), close the session
        db.close()
