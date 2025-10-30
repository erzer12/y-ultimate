"""
Team Database Model

This file will contain the SQLAlchemy model for a Team.

A Team represents a group of players competing in tournaments.
It would typically have:
  - name: Team name
  - coach_id: Foreign key to the User (coach)
  - Players: Many-to-many relationship with User (players)
  - Tournaments: Many-to-many relationship with Tournament
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Team(Base):
    """
    Team Model - Placeholder
    
    This is a placeholder model showing the basic structure.
    Expand this as needed for your application.
    """
    __tablename__ = "team"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    
    # Example: Foreign key to the coach (a User)
    # coach_id = Column(Integer, ForeignKey("user.id"))
    # coach = relationship("User", back_populates="teams")
