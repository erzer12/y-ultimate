from pydantic import BaseModel
from typing import Optional


class CoachBase(BaseModel):
    """Base coach schema"""
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None


class CoachCreate(CoachBase):
    """Schema for creating a coach"""
    user_id: int


class CoachUpdate(BaseModel):
    """Schema for updating a coach"""
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    total_session_hours: Optional[float] = None
    total_travel_hours: Optional[float] = None
    total_home_visits: Optional[int] = None


class Coach(CoachBase):
    """Schema for reading a coach"""
    id: int
    user_id: int
    total_session_hours: float
    total_travel_hours: float
    total_home_visits: int

    class Config:
        from_attributes = True
