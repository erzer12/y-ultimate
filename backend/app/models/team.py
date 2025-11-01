# Placeholder for Team model
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from ..db.base import Base


class Team(Base):
    """
    Team model for tournament participation.
    """
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    
    # Team details
    school = Column(String)
    community = Column(String)
    coach_name = Column(String)
    coach_contact = Column(String)
    
    # Tournament linkage
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    
    # Team statistics
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    draws = Column(Integer, default=0)
    points_for = Column(Integer, default=0)
    points_against = Column(Integer, default=0)
    spirit_score_total = Column(Integer, default=0)
    
    # Status
    is_active = Column(Boolean, default=True)
    
    # Notes
    notes = Column(Text)
    
    # Relationships
    tournament = relationship("Tournament", back_populates="teams")
    player_registrations = relationship("PlayerRegistration", back_populates="team")
    matches_as_team1 = relationship("Match", foreign_keys="Match.team1_id", back_populates="team1")
    matches_as_team2 = relationship("Match", foreign_keys="Match.team2_id", back_populates="team2")
