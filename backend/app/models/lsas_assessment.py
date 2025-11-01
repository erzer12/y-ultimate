from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Float, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum


class AssessmentType(str, enum.Enum):
    """Assessment types for LSAS"""
    BASELINE = "baseline"
    ENDLINE = "endline"
    FOLLOW_UP = "follow_up"
    MID_TERM = "mid_term"


class LSASAssessment(Base):
    """
    LSAS (Life Skill Assessment System) model for tracking
    child development across multiple assessment periods.
    """
    __tablename__ = "lsas_assessments"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key
    child_id = Column(Integer, ForeignKey("child_profiles.id"), nullable=False)
    
    # Assessment details
    assessment_type = Column(Enum(AssessmentType), nullable=False)
    assessment_date = Column(Date, nullable=False)
    
    # Scores (can be expanded based on actual LSAS criteria)
    overall_score = Column(Float)
    
    # Individual skill scores
    leadership_score = Column(Float)
    teamwork_score = Column(Float)
    communication_score = Column(Float)
    confidence_score = Column(Float)
    resilience_score = Column(Float)
    
    # Notes and observations
    assessor_notes = Column(Text)
    strengths = Column(Text)
    areas_for_improvement = Column(Text)
    
    # Assessor information
    assessed_by = Column(String)  # Coach name
    
    # Relationships
    child = relationship("ChildProfile", back_populates="assessments")
