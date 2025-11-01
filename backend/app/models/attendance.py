from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.base import Base


class Attendance(Base):
    """
    Attendance model for tracking child attendance at sessions.
    """
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign keys
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    child_id = Column(Integer, ForeignKey("child_profiles.id"), nullable=False)
    coach_id = Column(Integer, ForeignKey("coaches.id"), nullable=False)
    
    # Attendance details
    present = Column(Boolean, default=False, nullable=False)
    marked_at = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)
    
    # Relationships
    session = relationship("Session", back_populates="attendance_records")
    child = relationship("ChildProfile", back_populates="attendance_records")
    coach = relationship("Coach", back_populates="attendance_records")
