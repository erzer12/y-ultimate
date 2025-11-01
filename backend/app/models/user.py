from sqlalchemy import Column, Integer, String, Boolean
from ..db.base import Base # Import the Base we just made

class User(Base):
    """
    This is the SQLAlchemy model for the User.
    It defines the 'user' table in our database.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    
    # We can add relationships later, e.g.:
    # tournaments = relationship("Tournament", back_populates="owner")
