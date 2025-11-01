from fastapi import APIRouter
from .endpoints import (
    auth,
    profiles,
    tournaments,
    teams,
    coaches,
    sessions,
    attendance,
    home_visits,
    assessments,
    matches,
    registrations,
)

api_router = APIRouter()

# Authentication
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Coaching Programme Management
api_router.include_router(profiles.router, prefix="/profiles", tags=["Child Profiles"])
api_router.include_router(coaches.router, prefix="/coaches", tags=["Coaches"])
api_router.include_router(sessions.router, prefix="/sessions", tags=["Sessions"])
api_router.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
api_router.include_router(home_visits.router, prefix="/home-visits", tags=["Home Visits"])
api_router.include_router(assessments.router, prefix="/assessments", tags=["Assessments"])

# Tournament Management
api_router.include_router(tournaments.router, prefix="/tournaments", tags=["Tournaments"])
api_router.include_router(teams.router, prefix="/teams", tags=["Teams"])
api_router.include_router(matches.router, prefix="/matches", tags=["Matches"])
api_router.include_router(registrations.router, prefix="/registrations", tags=["Player Registrations"])
