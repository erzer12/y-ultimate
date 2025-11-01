# Placeholder for Team endpoints
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_teams():
    return [{"team_name": "Team 1"}, {"team_name": "Team 2"}]
