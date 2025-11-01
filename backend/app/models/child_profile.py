from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Text, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum


class Gender(str, enum.Enum):
    """Gender options for reporting"""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"


class ChildProfile(Base):
    """
    Child profile model with support for dual-program participation
    and transfer history tracking.
    """
    __tablename__ = "child_profiles"

    id = Column(Integer, primary_key=True, index=True)
    
    # Basic information
    name = Column(String, index=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(Enum(Gender))
    
    # Contact information
    parent_name = Column(String)
    parent_phone = Column(String)
    parent_email = Column(String)
    address = Column(Text)
    
    # Programme participation
    school = Column(String, index=True)
    community = Column(String, index=True)
    enrolled_in_school_program = Column(Boolean, default=False)
    enrolled_in_community_program = Column(Boolean, default=False)
    
    # Status
    is_active = Column(Boolean, default=True)
    enrollment_date = Column(Date)
    exit_date = Column(Date)
    exit_reason = Column(Text)
    
    # Transfer history stored as JSON text
    transfer_history = Column(Text)  # JSON string of transfer records
    
    # Notes
    medical_notes = Column(Text)
    general_notes = Column(Text)
    
    # Relationships
    assessments = relationship("LSASAssessment", back_populates="child")
    attendance_records = relationship("Attendance", back_populates="child")
    home_visits = relationship("HomeVisit", back_populates="child")
