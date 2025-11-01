from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from ..db.base import Base


class Match(Base):
    """
    Match model for tournament games.
    """
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    
    # Tournament reference
    tournament_id = Column(Integer, ForeignKey("tournaments.id"), nullable=False)
    
    # Match details
    match_number = Column(Integer, nullable=False)
    round = Column(String)  # pool_play, quarterfinal, semifinal, final
    pool = Column(String)  # Pool A, Pool B, etc.
    
    # Teams
    team1_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team2_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    
    # Scheduling
    scheduled_time = Column(DateTime)
    field = Column(String)
    
    # Scoring
    team1_score = Column(Integer, default=0)
    team2_score = Column(Integer, default=0)
    winner_id = Column(Integer, ForeignKey("teams.id"))
    
    # Spirit scores
    team1_spirit_score = Column(Float)
    team2_spirit_score = Column(Float)
    
    # Status
    is_completed = Column(Boolean, default=False)
    is_forfeit = Column(Boolean, default=False)
    
    # Relationships
    tournament = relationship("Tournament", back_populates="matches")
    team1 = relationship("Team", foreign_keys=[team1_id], back_populates="matches_as_team1")
    team2 = relationship("Team", foreign_keys=[team2_id], back_populates="matches_as_team2")
    winner = relationship("Team", foreign_keys=[winner_id])
