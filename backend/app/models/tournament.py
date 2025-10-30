"""
Tournament Database Model

This file defines the database table schema for tournaments.
It demonstrates how to create relationships between models using ForeignKey.
"""

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.db.base import Base


class Tournament(Base):
    """
    Tournament Model
    
    Represents a tournament event in the system.
    Each tournament has an owner (the user who created it).
    """
    
    # The table name in the database
    __tablename__ = "tournament"

    # === Column Definitions ===
    id = Column(Integer, primary_key=True, index=True)
    
    # Tournament name
    name = Column(String, nullable=False, index=True)
    
    # Tournament description
    description = Column(String)
    
    # Tournament location
    location = Column(String)
    
    # Start date of the tournament
    start_date = Column(DateTime)
    
    # End date of the tournament
    end_date = Column(DateTime)
    
    # Whether the tournament is currently active
    is_active = Column(Boolean, default=True)
    
    # === Foreign Key ===
    # ForeignKey creates a real database column that stores the ID of another table's row
    # "user.id" refers to the "id" column in the "user" table
    # This creates a many-to-one relationship: many tournaments can have one owner
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    
    # === Relationships ===
    # relationship() creates a Python attribute to access the related User object
    # back_populates="tournaments" links this to the "tournaments" attribute in the User model
    # 
    # This allows you to write:
    #   tournament.owner -> Returns the User object who owns this tournament
    #   user.tournaments -> Returns all Tournament objects owned by this user
    owner = relationship("User", back_populates="tournaments")
    
    # Placeholder for other relationships (teams participating in this tournament)
    # teams = relationship("Team", secondary="tournament_teams", back_populates="tournaments")
