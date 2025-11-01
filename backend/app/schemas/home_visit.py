from pydantic import BaseModel
from datetime import date
from typing import Optional


class HomeVisitBase(BaseModel):
    """Base home visit schema"""
    child_id: int
    coach_id: int
    visit_date: date
    visit_type: Optional[str] = None  # baseline, follow_up, emergency
    purpose: Optional[str] = None
    observations: Optional[str] = None
    action_items: Optional[str] = None


class HomeVisitCreate(HomeVisitBase):
    """Schema for creating a home visit"""
    pass


class HomeVisitUpdate(BaseModel):
    """Schema for updating a home visit"""
    visit_date: Optional[date] = None
    visit_type: Optional[str] = None
    purpose: Optional[str] = None
    observations: Optional[str] = None
    action_items: Optional[str] = None


class HomeVisit(HomeVisitBase):
    """Schema for reading a home visit"""
    id: int

    class Config:
        from_attributes = True
