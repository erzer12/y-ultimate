"""
Child Profile Pydantic Schemas

This file will contain the Pydantic schemas for Child Profile API operations.

Similar to User and Tournament schemas, these define the structure of data
that flows through the API (not the database structure).
"""

from datetime import date
from pydantic import BaseModel, ConfigDict


class ChildProfileBase(BaseModel):
    """
    Base Child Profile Schema
    
    Contains common fields shared by all ChildProfile schemas.
    """
    name: str
    date_of_birth: date | None = None


class ChildProfileCreate(ChildProfileBase):
    """
    Schema for Creating a Child Profile
    
    Used in POST /profiles/ endpoint.
    """
    pass  # Inherits all fields from ChildProfileBase


class ChildProfile(ChildProfileBase):
    """
    Schema for Reading a Child Profile
    
    Used in API responses.
    """
    id: int
    # parent_id: int  # Uncomment when parent relationship is implemented
    
    model_config = ConfigDict(from_attributes=True)
