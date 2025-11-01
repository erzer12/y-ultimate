from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from ..db.base import Base
import enum


class UserRole(str, enum.Enum):
    """User roles for role-based access control"""
    ADMIN = "admin"  # Programme Director / Admin
    MANAGER = "manager"  # Programme Manager
    COACH = "coach"  # Coach / Facilitator
    REPORTING = "reporting"  # Reporting / Data Team
    COORDINATOR = "coordinator"  # Community / School Coordinator


class User(Base):
    """
    This is the SQLAlchemy model for the User.
    It defines the 'user' table in our database.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    
    # Role-based access control
    role = Column(Enum(UserRole), default=UserRole.COACH, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Legacy field for backward compatibility
    is_admin = Column(Boolean, default=False)
    
    # Relationships
    tournaments = relationship("Tournament", back_populates="owner")
