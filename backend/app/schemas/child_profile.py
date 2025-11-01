from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class ChildProfileBase(BaseModel):
    """Base child profile schema"""
    name: str
    date_of_birth: date
    gender: Optional[str] = None
    parent_name: Optional[str] = None
    parent_phone: Optional[str] = None
    parent_email: Optional[EmailStr] = None
    address: Optional[str] = None
    school: Optional[str] = None
    community: Optional[str] = None
    enrolled_in_school_program: bool = False
    enrolled_in_community_program: bool = False
    medical_notes: Optional[str] = None
    general_notes: Optional[str] = None


class ChildProfileCreate(ChildProfileBase):
    """Schema for creating a child profile"""
    enrollment_date: Optional[date] = None


class ChildProfileUpdate(BaseModel):
    """Schema for updating a child profile"""
    name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    parent_name: Optional[str] = None
    parent_phone: Optional[str] = None
    parent_email: Optional[EmailStr] = None
    address: Optional[str] = None
    school: Optional[str] = None
    community: Optional[str] = None
    enrolled_in_school_program: Optional[bool] = None
    enrolled_in_community_program: Optional[bool] = None
    is_active: Optional[bool] = None
    exit_date: Optional[date] = None
    exit_reason: Optional[str] = None
    medical_notes: Optional[str] = None
    general_notes: Optional[str] = None


class ChildProfile(ChildProfileBase):
    """Schema for reading a child profile"""
    id: int
    is_active: bool
    enrollment_date: Optional[date] = None
    exit_date: Optional[date] = None
    exit_reason: Optional[str] = None
    transfer_history: Optional[str] = None

    class Config:
        from_attributes = True


class ChildProfileWithStats(ChildProfile):
    """Child profile with attendance and assessment stats"""
    total_sessions: int = 0
    sessions_attended: int = 0
    attendance_rate: float = 0.0
    latest_assessment_date: Optional[date] = None
    latest_assessment_score: Optional[float] = None


class ChildTransfer(BaseModel):
    """Schema for transferring a child between schools/communities"""
    child_id: int
    from_location: str
    to_location: str
    transfer_date: date
    reason: Optional[str] = None

