from pydantic import BaseModel
from datetime import date
from .user import User # Import the User schema to nest it

# --- TournamentBase ---
# The common fields shared by create and read schemas
class TournamentBase(BaseModel):
    name: str
    location: str | None = None
    start_date: date | None = None
    end_date: date | None = None

# --- TournamentCreate ---
# The schema used when *creating* a new tournament
# We don't need owner_id here, as we get it from the logged-in user
class TournamentCreate(TournamentBase):
    pass

# --- Tournament ---
# The schema used when *reading* a tournament from the API
# This will be returned to the frontend
class Tournament(TournamentBase):
    id: int
    owner_id: int
    owner: User # Nest the full User object

    class Config:
        from_attributes = True
