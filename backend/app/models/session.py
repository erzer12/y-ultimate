from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.base import Base


class Session(Base):
    """
    Session model for tracking coaching sessions.
    """
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    session_type = Column(String, nullable=False)  # school, community, tournament_prep
    location = Column(String, nullable=False)
    school = Column(String)
    community = Column(String)
    
    # Timing
    scheduled_start = Column(DateTime, nullable=False)
    scheduled_end = Column(DateTime, nullable=False)
    actual_start = Column(DateTime)
    actual_end = Column(DateTime)
    
    # Coach assignment
    coach_id = Column(Integer, ForeignKey("coaches.id"), nullable=False)
    
    # Session details
    duration_hours = Column(Float)
    travel_hours = Column(Float, default=0.0)
    is_active = Column(Boolean, default=False)
    is_completed = Column(Boolean, default=False)
    notes = Column(Text)
    
    # Relationships
    coach = relationship("Coach", back_populates="sessions")
    attendance_records = relationship("Attendance", back_populates="session")
