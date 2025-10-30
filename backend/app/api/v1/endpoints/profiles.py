"""
Child Profile Endpoints

This file will contain all child profile-related endpoints:
  - GET /profiles/: List all child profiles (for the current user)
  - POST /profiles/: Create a new child profile
  - GET /profiles/{id}: Get a specific child profile
  - PUT /profiles/{id}: Update a child profile
  - DELETE /profiles/{id}: Delete a child profile
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

# Create a router for child profile endpoints
router = APIRouter()


@router.get("/")
def list_profiles(db: Session = Depends(get_db)):
    """
    List All Child Profiles
    
    Returns a list of child profiles for the current user.
    
    TODO: Implement profile listing
    """
    return {"message": "Profile listing not yet implemented"}
