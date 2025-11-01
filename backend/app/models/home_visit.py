from sqlalchemy import Column, Integer, Date, ForeignKey, Text, String
from sqlalchemy.orm import relationship
from ..db.base import Base


class HomeVisit(Base):
    """
    HomeVisit model for tracking home visits to children's families.
    """
    __tablename__ = "home_visits"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign keys
    child_id = Column(Integer, ForeignKey("child_profiles.id"), nullable=False)
    coach_id = Column(Integer, ForeignKey("coaches.id"), nullable=False)
    
    # Visit details
    visit_date = Column(Date, nullable=False)
    visit_type = Column(String)  # baseline, follow_up, emergency
    purpose = Column(Text)
    observations = Column(Text)
    action_items = Column(Text)
    
    # Relationships
    child = relationship("ChildProfile", back_populates="home_visits")
    coach = relationship("Coach", back_populates="home_visits")
