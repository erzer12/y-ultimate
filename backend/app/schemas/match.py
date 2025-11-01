from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MatchBase(BaseModel):
    """Base match schema"""
    tournament_id: int
    match_number: int
    round: Optional[str] = None  # pool_play, quarterfinal, semifinal, final
    pool: Optional[str] = None
    team1_id: int
    team2_id: int
    scheduled_time: Optional[datetime] = None
    field: Optional[str] = None


class MatchCreate(MatchBase):
    """Schema for creating a match"""
    pass


class MatchUpdate(BaseModel):
    """Schema for updating a match"""
    scheduled_time: Optional[datetime] = None
    field: Optional[str] = None
    team1_score: Optional[int] = None
    team2_score: Optional[int] = None
    winner_id: Optional[int] = None
    team1_spirit_score: Optional[float] = None
    team2_spirit_score: Optional[float] = None
    is_completed: Optional[bool] = None
    is_forfeit: Optional[bool] = None


class Match(MatchBase):
    """Schema for reading a match"""
    id: int
    team1_score: int
    team2_score: int
    winner_id: Optional[int] = None
    team1_spirit_score: Optional[float] = None
    team2_spirit_score: Optional[float] = None
    is_completed: bool
    is_forfeit: bool

    class Config:
        from_attributes = True


class MatchWithTeams(Match):
    """Match schema with team names"""
    team1_name: str
    team2_name: str
    winner_name: Optional[str] = None
