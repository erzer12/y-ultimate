from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ....db.session import get_db
from ....models import home_visit as home_visit_model
from ....schemas import home_visit as home_visit_schema

router = APIRouter()


@router.post("/", response_model=home_visit_schema.HomeVisit, status_code=status.HTTP_201_CREATED)
def create_home_visit(
    home_visit: home_visit_schema.HomeVisitCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new home visit record.
    """
    db_visit = home_visit_model.HomeVisit(**home_visit.model_dump())
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit


@router.get("/", response_model=List[home_visit_schema.HomeVisit])
def list_home_visits(
    skip: int = 0,
    limit: int = 100,
    child_id: int = None,
    coach_id: int = None,
    visit_type: str = None,
    db: Session = Depends(get_db)
):
    """
    Get all home visits with optional filtering.
    """
    query = db.query(home_visit_model.HomeVisit)
    
    if child_id:
        query = query.filter(home_visit_model.HomeVisit.child_id == child_id)
    if coach_id:
        query = query.filter(home_visit_model.HomeVisit.coach_id == coach_id)
    if visit_type:
        query = query.filter(home_visit_model.HomeVisit.visit_type == visit_type)
    
    visits = query.offset(skip).limit(limit).all()
    return visits


@router.get("/{visit_id}", response_model=home_visit_schema.HomeVisit)
def get_home_visit(
    visit_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific home visit by ID.
    """
    visit = db.query(home_visit_model.HomeVisit).filter(
        home_visit_model.HomeVisit.id == visit_id
    ).first()
    if not visit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Home visit not found"
        )
    return visit


@router.put("/{visit_id}", response_model=home_visit_schema.HomeVisit)
def update_home_visit(
    visit_id: int,
    visit_update: home_visit_schema.HomeVisitUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a home visit record.
    """
    visit = db.query(home_visit_model.HomeVisit).filter(
        home_visit_model.HomeVisit.id == visit_id
    ).first()
    if not visit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Home visit not found"
        )
    
    update_data = visit_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(visit, field, value)
    
    db.commit()
    db.refresh(visit)
    return visit


@router.delete("/{visit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_home_visit(
    visit_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a home visit record.
    """
    visit = db.query(home_visit_model.HomeVisit).filter(
        home_visit_model.HomeVisit.id == visit_id
    ).first()
    if not visit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Home visit not found"
        )
    
    db.delete(visit)
    db.commit()
    return None
