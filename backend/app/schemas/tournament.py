"""
Tournament Pydantic Schemas

This file demonstrates how schemas can be nested to return rich, related data.
For example, a Tournament schema can include a nested User schema to return
information about the tournament's owner in a single API response.
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict

# Import the User schema to nest it
from app.schemas.user import User


# === Base Schema ===
class TournamentBase(BaseModel):
    """
    Base Tournament Schema
    
    Contains common fields shared by all Tournament schemas.
    """
    name: str
    description: str | None = None
    location: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    is_active: bool = True


# === Create Schema ===
class TournamentCreate(TournamentBase):
    """
    Schema for Creating a Tournament
    
    Used in POST /tournaments/ endpoint.
    The owner_id will typically come from the authenticated user's JWT token,
    not from the request body (for security).
    """
    pass  # Inherits all fields from TournamentBase


# === Update Schema ===
class TournamentUpdate(BaseModel):
    """
    Schema for Updating a Tournament
    
    Used in PUT/PATCH /tournaments/{id} endpoint.
    All fields are optional to allow partial updates.
    """
    name: str | None = None
    description: str | None = None
    location: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    is_active: bool | None = None


# === Response Schema ===
class Tournament(TournamentBase):
    """
    Schema for Reading a Tournament
    
    Used in API responses (GET /tournaments/, GET /tournaments/{id}).
    
    NESTED SCHEMAS:
    The 'owner' field is a nested User schema. This means the API can return
    rich, related data in a single response without requiring multiple requests.
    
    Example JSON response:
    {
        "id": 1,
        "name": "Summer Championship 2024",
        "description": "Annual summer tournament",
        "location": "Central Park",
        "start_date": "2024-07-01T09:00:00",
        "end_date": "2024-07-03T18:00:00",
        "is_active": true,
        "owner_id": 5,
        "owner": {
            "id": 5,
            "email": "coach@example.com",
            "full_name": "Coach Smith",
            "is_active": true,
            "is_admin": false
        }
    }
    
    Notice how the 'owner' field contains a full User object, not just an ID.
    This is the power of nested schemas.
    """
    id: int
    owner_id: int
    
    # Nested schema: includes full User object
    owner: User
    
    # Configure Pydantic to work with SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)
