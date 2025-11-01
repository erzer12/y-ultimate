from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base
from ..models.user import User # We need to import User for the relationship

class Tournament(Base):
    """
    This is the SQLAlchemy model for a Tournament.
    It defines the 'tournaments' table in our database.
    """
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    
    # This creates a many-to-one relationship with the User model
    # It links a tournament to the user who created it.
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User") 
    
    # We can add relationships for teams, matches, etc. later
    # teams = relationship("Team", back_populates="tournament")
