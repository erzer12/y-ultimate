# Placeholder for ChildProfile model
from sqlalchemy import Column, Integer, String, ForeignKey
from ..db.base import Base

class ChildProfile(Base):
    __tablename__ = "child_profiles"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    
    # Example relationship to a team
    # team_id = Column(Integer, ForeignKey("teams.id"))
