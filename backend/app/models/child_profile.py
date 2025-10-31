"""
Child Profile Database Model

This file will contain the SQLAlchemy model for a Child Profile.

A Child Profile stores information about a child player in the system.
It would typically have:
  - name: Child's name
  - date_of_birth: Date of birth
  - parent_id: Foreign key to the User (parent)
  - LSAS assessments: One-to-many relationship with LSASAssessment
"""

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class ChildProfile(Base):
    """
    ChildProfile Model - Placeholder
    
    This is a placeholder model showing the basic structure.
    Expand this as needed for your application.
    """
    __tablename__ = "child_profile"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # Example: Foreign key to the parent (a User)
    # parent_id = Column(Integer, ForeignKey("user.id"))
    # parent = relationship("User", back_populates="child_profiles")
    
    # Example: One-to-many relationship with LSAS assessments
    # lsas_assessments = relationship("LSASAssessment", back_populates="child_profile")
