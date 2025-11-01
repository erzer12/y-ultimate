from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SessionBase(BaseModel):
    """Base session schema"""
    title: str
    session_type: str  # school, community, tournament_prep
    location: str
    school: Optional[str] = None
    community: Optional[str] = None
    scheduled_start: datetime
    scheduled_end: datetime
    travel_hours: Optional[float] = 0.0
    notes: Optional[str] = None


class SessionCreate(SessionBase):
    """Schema for creating a session"""
    coach_id: int


class SessionUpdate(BaseModel):
    """Schema for updating a session"""
    title: Optional[str] = None
    session_type: Optional[str] = None
    location: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    duration_hours: Optional[float] = None
    travel_hours: Optional[float] = None
    is_active: Optional[bool] = None
    is_completed: Optional[bool] = None
    notes: Optional[str] = None


class Session(SessionBase):
    """Schema for reading a session"""
    id: int
    coach_id: int
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    duration_hours: Optional[float] = None
    is_active: bool
    is_completed: bool

    class Config:
        from_attributes = True


class SessionWithAttendance(Session):
    """Session with attendance count"""
    attendance_count: int
    children_present: int
