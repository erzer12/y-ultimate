from pydantic import BaseModel
from datetime import date
from typing import Optional


class LSASAssessmentBase(BaseModel):
    """Base LSAS assessment schema"""
    child_id: int
    assessment_type: str  # baseline, endline, follow_up, mid_term
    assessment_date: date
    overall_score: Optional[float] = None
    leadership_score: Optional[float] = None
    teamwork_score: Optional[float] = None
    communication_score: Optional[float] = None
    confidence_score: Optional[float] = None
    resilience_score: Optional[float] = None
    assessor_notes: Optional[str] = None
    strengths: Optional[str] = None
    areas_for_improvement: Optional[str] = None
    assessed_by: Optional[str] = None


class LSASAssessmentCreate(LSASAssessmentBase):
    """Schema for creating an assessment"""
    pass


class LSASAssessmentUpdate(BaseModel):
    """Schema for updating an assessment"""
    assessment_type: Optional[str] = None
    assessment_date: Optional[date] = None
    overall_score: Optional[float] = None
    leadership_score: Optional[float] = None
    teamwork_score: Optional[float] = None
    communication_score: Optional[float] = None
    confidence_score: Optional[float] = None
    resilience_score: Optional[float] = None
    assessor_notes: Optional[str] = None
    strengths: Optional[str] = None
    areas_for_improvement: Optional[str] = None
    assessed_by: Optional[str] = None


class LSASAssessment(LSASAssessmentBase):
    """Schema for reading an assessment"""
    id: int

    class Config:
        from_attributes = True
