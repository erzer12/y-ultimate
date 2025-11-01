from pydantic import BaseModel
from typing import Optional


class TeamBase(BaseModel):
    """Base team schema"""
    name: str
    school: Optional[str] = None
    community: Optional[str] = None
    coach_name: Optional[str] = None
    coach_contact: Optional[str] = None
    notes: Optional[str] = None


class TeamCreate(TeamBase):
    """Schema for creating a team"""
    tournament_id: Optional[int] = None


class TeamUpdate(BaseModel):
    """Schema for updating a team"""
    name: Optional[str] = None
    school: Optional[str] = None
    community: Optional[str] = None
    coach_name: Optional[str] = None
    coach_contact: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    draws: Optional[int] = None
    points_for: Optional[int] = None
    points_against: Optional[int] = None
    spirit_score_total: Optional[int] = None
    is_active: Optional[bool] = None
    notes: Optional[str] = None


class Team(TeamBase):
    """Schema for reading a team"""
    id: int
    tournament_id: Optional[int] = None
    wins: int
    losses: int
    draws: int
    points_for: int
    points_against: int
    spirit_score_total: int
    is_active: bool

    class Config:
        from_attributes = True


class TeamWithStats(Team):
    """Team with additional statistics"""
    total_matches: int
    win_percentage: float
    average_spirit_score: float
    point_differential: int
