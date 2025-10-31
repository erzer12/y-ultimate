"""
Tournament Endpoints

This file will contain all tournament-related endpoints:
  - GET /tournaments/: List all tournaments
  - POST /tournaments/: Create a new tournament
  - GET /tournaments/{id}: Get a specific tournament
  - PUT /tournaments/{id}: Update a tournament
  - DELETE /tournaments/{id}: Delete a tournament
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

# Create a router for tournament endpoints
router = APIRouter()


@router.get("/")
def list_tournaments(db: Session = Depends(get_db)):
    """
    List All Tournaments
    
    Returns a list of all tournaments in the system.
    
    TODO: Implement tournament listing
      - Query database for all tournaments
      - Optionally add pagination, filtering, sorting
      - Return list of Tournament schemas
    """
    return {"message": "Tournament listing not yet implemented"}


@router.post("/")
def create_tournament(db: Session = Depends(get_db)):
    """
    Create a New Tournament
    
    Creates a new tournament with the authenticated user as owner.
    
    TODO: Implement tournament creation
      - Get current user from JWT token
      - Create tournament with user as owner
      - Save to database
      - Return Tournament schema
    """
    return {"message": "Tournament creation not yet implemented"}
