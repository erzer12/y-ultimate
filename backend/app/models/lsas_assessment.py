from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class LSASAssessment(Base):
    __tablename__ = "lsas_assessments"

    id = Column(Integer, primary_key=True, index=True)
    assessment_type = Column(String)  # e.g., baseline, endline
    date = Column(Date)
    score = Column(Integer)
    child_id = Column(Integer, ForeignKey("child_profiles.id"))

    child = relationship("ChildProfile", back_populates="assessments")
