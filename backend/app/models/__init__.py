# Import all models here to make them available to Alembic and the app
from .user import User, UserRole
from .child_profile import ChildProfile, Gender
from .team import Team
from .tournament import Tournament, TournamentStatus
from .lsas_assessment import LSASAssessment, AssessmentType
from .coach import Coach
from .session import Session
from .attendance import Attendance
from .home_visit import HomeVisit
from .match import Match
from .player_registration import PlayerRegistration

__all__ = [
    "User",
    "UserRole",
    "ChildProfile",
    "Gender",
    "Team",
    "Tournament",
    "TournamentStatus",
    "LSASAssessment",
    "AssessmentType",
    "Coach",
    "Session",
    "Attendance",
    "HomeVisit",
    "Match",
    "PlayerRegistration",
]
