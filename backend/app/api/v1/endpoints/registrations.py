from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from ....db.session import get_db
from ....models import player_registration as registration_model
from ....schemas import player_registration as registration_schema

router = APIRouter()


@router.post("/", response_model=registration_schema.PlayerRegistration, status_code=status.HTTP_201_CREATED)
def create_registration(
    registration: registration_schema.PlayerRegistrationCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new player registration.
    """
    db_registration = registration_model.PlayerRegistration(**registration.model_dump())
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration


@router.get("/", response_model=List[registration_schema.PlayerRegistration])
def list_registrations(
    skip: int = 0,
    limit: int = 100,
    tournament_id: int = None,
    team_id: int = None,
    is_approved: bool = None,
    db: Session = Depends(get_db)
):
    """
    Get all player registrations with optional filtering.
    """
    query = db.query(registration_model.PlayerRegistration)
    
    if tournament_id:
        query = query.filter(registration_model.PlayerRegistration.tournament_id == tournament_id)
    if team_id:
        query = query.filter(registration_model.PlayerRegistration.team_id == team_id)
    if is_approved is not None:
        query = query.filter(registration_model.PlayerRegistration.is_approved == is_approved)
    
    registrations = query.offset(skip).limit(limit).all()
    return registrations


@router.get("/{registration_id}", response_model=registration_schema.PlayerRegistration)
def get_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific registration by ID.
    """
    registration = db.query(registration_model.PlayerRegistration).filter(
        registration_model.PlayerRegistration.id == registration_id
    ).first()
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return registration


@router.post("/{registration_id}/approve", response_model=registration_schema.PlayerRegistration)
def approve_registration(
    registration_id: int,
    approval: registration_schema.PlayerRegistrationApproval,
    db: Session = Depends(get_db)
):
    """
    Approve or reject a player registration.
    """
    registration = db.query(registration_model.PlayerRegistration).filter(
        registration_model.PlayerRegistration.id == registration_id
    ).first()
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    
    registration.is_approved = approval.is_approved
    registration.approved_by = approval.approved_by
    registration.approval_date = datetime.utcnow()
    
    db.commit()
    db.refresh(registration)
    return registration


@router.put("/{registration_id}", response_model=registration_schema.PlayerRegistration)
def update_registration(
    registration_id: int,
    registration_update: registration_schema.PlayerRegistrationUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a player registration.
    """
    registration = db.query(registration_model.PlayerRegistration).filter(
        registration_model.PlayerRegistration.id == registration_id
    ).first()
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    
    update_data = registration_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(registration, field, value)
    
    db.commit()
    db.refresh(registration)
    return registration


@router.delete("/{registration_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a player registration.
    """
    registration = db.query(registration_model.PlayerRegistration).filter(
        registration_model.PlayerRegistration.id == registration_id
    ).first()
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    
    db.delete(registration)
    db.commit()
    return None
