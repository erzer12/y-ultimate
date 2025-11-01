from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class TournamentBase(BaseModel):
    """Base tournament schema"""
    name: str
    description: Optional[str] = None
    location: str
    venue: Optional[str] = None
    start_date: date
    end_date: date
    registration_open_date: Optional[date] = None
    registration_close_date: Optional[date] = None
    max_teams: Optional[int] = None
    tournament_format: Optional[str] = None  # round_robin, bracket, pool_play
    age_division: Optional[str] = None  # U12, U15, U18, Open
    organizer_name: Optional[str] = None
    organizer_email: Optional[EmailStr] = None
    organizer_phone: Optional[str] = None
    rules: Optional[str] = None
    notes: Optional[str] = None


class TournamentCreate(TournamentBase):
    """Schema for creating a tournament"""
    owner_id: int


class TournamentUpdate(BaseModel):
    """Schema for updating a tournament"""
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    venue: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    registration_open_date: Optional[date] = None
    registration_close_date: Optional[date] = None
    max_teams: Optional[int] = None
    tournament_format: Optional[str] = None
    age_division: Optional[str] = None
    status: Optional[str] = None
    is_published: Optional[bool] = None
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None
    organizer_name: Optional[str] = None
    organizer_email: Optional[EmailStr] = None
    organizer_phone: Optional[str] = None
    rules: Optional[str] = None
    notes: Optional[str] = None


class Tournament(TournamentBase):
    """Schema for reading a tournament"""
    id: int
    owner_id: int
    status: str
    is_published: bool
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None

    class Config:
        from_attributes = True


class TournamentWithStats(Tournament):
    """Tournament with statistics"""
    total_teams: int = 0
    total_matches: int = 0
    completed_matches: int = 0
    total_registrations: int = 0
    approved_registrations: int = 0
