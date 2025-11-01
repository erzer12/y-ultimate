from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.db import session
from app.models import child_profile

router = APIRouter()

@router.post("/", response_model=schemas.child_profile.ChildProfile)
def create_child_profile(profile: schemas.child_profile.ChildProfileCreate, db: Session = Depends(session.get_db)):
    db_profile = child_profile.ChildProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


@router.get("/{profile_id}", response_model=schemas.child_profile.ChildProfile)
def read_child_profile(profile_id: int, db: Session = Depends(session.get_db)):
    db_profile = db.query(child_profile.ChildProfile).filter(child_profile.ChildProfile.id == profile_id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile
