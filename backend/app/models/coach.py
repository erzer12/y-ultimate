from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base


class Coach(Base):
    """
    Coach model for tracking coach information and workload.
    Links to User model for authentication.
    """
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    name = Column(String, nullable=False, index=True)
    phone = Column(String)
    email = Column(String)
    
    # Workload tracking
    total_session_hours = Column(Float, default=0.0)
    total_travel_hours = Column(Float, default=0.0)
    total_home_visits = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User")
    sessions = relationship("Session", back_populates="coach")
    home_visits = relationship("HomeVisit", back_populates="coach")
    attendance_records = relationship("Attendance", back_populates="coach")
