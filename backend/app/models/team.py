# Placeholder for Team model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, nullable=False)
    
    # Example relationship to a tournament
    # tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    # tournament = relationship("Tournament", back_populates="teams")
