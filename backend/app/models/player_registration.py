from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.base import Base


class PlayerRegistration(Base):
    """
    Player registration model for tournament participation.
    """
    __tablename__ = "player_registrations"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign keys
    tournament_id = Column(Integer, ForeignKey("tournaments.id"), nullable=False)
    child_id = Column(Integer, ForeignKey("child_profiles.id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"))
    
    # Registration details
    registration_date = Column(DateTime, default=datetime.utcnow)
    jersey_number = Column(Integer)
    jersey_size = Column(String)
    
    # Status
    is_approved = Column(Boolean, default=False)
    approval_date = Column(DateTime)
    approved_by = Column(Integer, ForeignKey("users.id"))
    
    # Emergency contact
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String)
    
    # Notes
    dietary_restrictions = Column(Text)
    medical_conditions = Column(Text)
    notes = Column(Text)
    
    # Relationships
    tournament = relationship("Tournament")
    child = relationship("ChildProfile")
    team = relationship("Team", back_populates="player_registrations")
    approver = relationship("User")
