from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from datetime import date
from ....db.session import get_db
from ....models import coach as coach_model
from ....schemas import coach as coach_schema

router = APIRouter()


@router.post("/", response_model=coach_schema.Coach, status_code=status.HTTP_201_CREATED)
def create_coach(
    coach: coach_schema.CoachCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new coach profile.
    """
    # Check if coach already exists for this user
    existing_coach = db.query(coach_model.Coach).filter(
        coach_model.Coach.user_id == coach.user_id
    ).first()
    if existing_coach:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Coach profile already exists for this user"
        )
    
    db_coach = coach_model.Coach(**coach.model_dump())
    db.add(db_coach)
    db.commit()
    db.refresh(db_coach)
    return db_coach


@router.get("/", response_model=List[coach_schema.Coach])
def list_coaches(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get all coaches.
    """
    coaches = db.query(coach_model.Coach).offset(skip).limit(limit).all()
    return coaches


@router.get("/{coach_id}", response_model=coach_schema.Coach)
def get_coach(
    coach_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific coach by ID.
    """
    coach = db.query(coach_model.Coach).filter(coach_model.Coach.id == coach_id).first()
    if not coach:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coach not found"
        )
    return coach


@router.put("/{coach_id}", response_model=coach_schema.Coach)
def update_coach(
    coach_id: int,
    coach_update: coach_schema.CoachUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a coach profile.
    """
    coach = db.query(coach_model.Coach).filter(coach_model.Coach.id == coach_id).first()
    if not coach:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coach not found"
        )
    
    update_data = coach_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(coach, field, value)
    
    db.commit()
    db.refresh(coach)
    return coach


@router.delete("/{coach_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_coach(
    coach_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a coach profile.
    """
    coach = db.query(coach_model.Coach).filter(coach_model.Coach.id == coach_id).first()
    if not coach:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coach not found"
        )
    
    db.delete(coach)
    db.commit()
    return None
