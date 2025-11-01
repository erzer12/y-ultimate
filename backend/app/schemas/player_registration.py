from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PlayerRegistrationBase(BaseModel):
    """Base player registration schema"""
    tournament_id: int
    child_id: int
    team_id: Optional[int] = None
    jersey_number: Optional[int] = None
    jersey_size: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    dietary_restrictions: Optional[str] = None
    medical_conditions: Optional[str] = None
    notes: Optional[str] = None


class PlayerRegistrationCreate(PlayerRegistrationBase):
    """Schema for creating a player registration"""
    pass


class PlayerRegistrationUpdate(BaseModel):
    """Schema for updating a player registration"""
    team_id: Optional[int] = None
    jersey_number: Optional[int] = None
    jersey_size: Optional[str] = None
    is_approved: Optional[bool] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    dietary_restrictions: Optional[str] = None
    medical_conditions: Optional[str] = None
    notes: Optional[str] = None


class PlayerRegistration(PlayerRegistrationBase):
    """Schema for reading a player registration"""
    id: int
    registration_date: datetime
    is_approved: bool
    approval_date: Optional[datetime] = None
    approved_by: Optional[int] = None

    class Config:
        from_attributes = True


class PlayerRegistrationApproval(BaseModel):
    """Schema for approving/rejecting registrations"""
    is_approved: bool
    approved_by: int
