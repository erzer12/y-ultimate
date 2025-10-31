"""
User Database Model

This file defines the database table schema for users.
It uses SQLAlchemy ORM to map a Python class to a database table.

Important: This is a MODEL (database structure), not a SCHEMA (API data structure).
Models live in the database. Schemas live in API requests/responses.
See app/schemas/user.py for the Pydantic schemas that define API data shapes.
"""

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    """
    User Model
    
    Represents a user in the system (Admin, Coach, or Parent).
    
    SQLAlchemy will automatically create a table named "user" in the database
    with columns matching the Column definitions below.
    """
    
    # The table name in the database
    __tablename__ = "user"

    # === Column Definitions ===
    # Column() creates a database column
    # primary_key=True means this is the unique identifier for each row
    id = Column(Integer, primary_key=True, index=True)
    
    # User's email address (must be unique across all users)
    # index=True creates a database index for faster lookups
    email = Column(String, unique=True, index=True, nullable=False)
    
    # The hashed password (NEVER store plain text passwords)
    # This will be generated using passlib's bcrypt hashing
    hashed_password = Column(String, nullable=False)
    
    # User's full name
    full_name = Column(String)
    
    # Whether this account is active (allows soft-deleting users)
    is_active = Column(Boolean, default=True)
    
    # Whether this user has admin privileges
    is_admin = Column(Boolean, default=False)
    
    # === Relationships ===
    # relationship() does NOT create a database column.
    # It creates a Python attribute that allows you to access related objects.
    # For example: user.tournaments will give you all tournaments owned by this user.
    #
    # back_populates="owner" links this to the "owner" attribute in the Tournament model.
    # This creates a two-way relationship: user.tournaments and tournament.owner
    tournaments = relationship("Tournament", back_populates="owner")
    
    # Placeholder for other relationships (teams, child_profiles, etc.)
    # These would be defined as the other models are created
    # teams = relationship("Team", back_populates="coach")
    # child_profiles = relationship("ChildProfile", back_populates="parent")
