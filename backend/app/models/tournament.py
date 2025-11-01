from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Boolean, Enum
from sqlalchemy.orm import relationship
from ..db.base import Base
from ..models.user import User
import enum


class TournamentStatus(str, enum.Enum):
    """Tournament status options"""
    DRAFT = "draft"
    OPEN_REGISTRATION = "open_registration"
    REGISTRATION_CLOSED = "registration_closed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Tournament(Base):
    """
    Tournament model for managing ultimate frisbee events.
    """
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    
    # Basic information
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    location = Column(String, nullable=False)
    venue = Column(String)
    
    # Dates
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    registration_open_date = Column(Date)
    registration_close_date = Column(Date)
    
    # Tournament details
    max_teams = Column(Integer)
    tournament_format = Column(String)  # round_robin, bracket, pool_play
    age_division = Column(String)  # U12, U15, U18, Open
    
    # Status
    status = Column(Enum(TournamentStatus), default=TournamentStatus.DRAFT)
    is_published = Column(Boolean, default=False)
    
    # Media
    logo_url = Column(String)
    banner_url = Column(String)
    
    # Contact and organization
    organizer_name = Column(String)
    organizer_email = Column(String)
    organizer_phone = Column(String)
    
    # Owner relationship
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="tournaments")
    
    # Additional info
    rules = Column(Text)
    notes = Column(Text)
    
    # Relationships
    teams = relationship("Team", back_populates="tournament")
    matches = relationship("Match", back_populates="tournament")
