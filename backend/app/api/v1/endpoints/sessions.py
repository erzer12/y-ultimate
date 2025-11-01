from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from datetime import datetime
from ....db.session import get_db
from ....models import session as session_model
from ....models import attendance as attendance_model
from ....schemas import session as session_schema

router = APIRouter()


@router.post("/", response_model=session_schema.Session, status_code=status.HTTP_201_CREATED)
def create_session(
    session: session_schema.SessionCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new coaching session.
    """
    # Calculate duration if not provided
    duration_hours = (session.scheduled_end - session.scheduled_start).total_seconds() / 3600
    
    db_session = session_model.Session(
        **session.model_dump(),
        duration_hours=duration_hours
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


@router.get("/", response_model=List[session_schema.Session])
def list_sessions(
    skip: int = 0,
    limit: int = 100,
    is_active: bool = None,
    is_completed: bool = None,
    coach_id: int = None,
    session_type: str = None,
    db: Session = Depends(get_db)
):
    """
    Get all sessions with optional filtering.
    """
    query = db.query(session_model.Session)
    
    if is_active is not None:
        query = query.filter(session_model.Session.is_active == is_active)
    if is_completed is not None:
        query = query.filter(session_model.Session.is_completed == is_completed)
    if coach_id:
        query = query.filter(session_model.Session.coach_id == coach_id)
    if session_type:
        query = query.filter(session_model.Session.session_type == session_type)
    
    sessions = query.offset(skip).limit(limit).all()
    return sessions


@router.get("/{session_id}", response_model=session_schema.Session)
def get_session(
    session_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific session by ID.
    """
    session = db.query(session_model.Session).filter(
        session_model.Session.id == session_id
    ).first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    return session


@router.get("/{session_id}/attendance", response_model=session_schema.SessionWithAttendance)
def get_session_with_attendance(
    session_id: int,
    db: Session = Depends(get_db)
):
    """
    Get session with attendance statistics.
    """
    session = db.query(session_model.Session).filter(
        session_model.Session.id == session_id
    ).first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    # Get attendance counts
    attendance_count = db.query(func.count(attendance_model.Attendance.id)).filter(
        attendance_model.Attendance.session_id == session_id
    ).scalar()
    
    children_present = db.query(func.count(attendance_model.Attendance.id)).filter(
        attendance_model.Attendance.session_id == session_id,
        attendance_model.Attendance.present == True
    ).scalar()
    
    # Create response with attendance data
    session_dict = {
        **session.__dict__,
        "attendance_count": attendance_count or 0,
        "children_present": children_present or 0
    }
    
    return session_dict


@router.put("/{session_id}", response_model=session_schema.Session)
def update_session(
    session_id: int,
    session_update: session_schema.SessionUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a session.
    """
    session = db.query(session_model.Session).filter(
        session_model.Session.id == session_id
    ).first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    update_data = session_update.model_dump(exclude_unset=True)
    
    # Recalculate duration if times are updated
    if "actual_start" in update_data and "actual_end" in update_data:
        if update_data["actual_start"] and update_data["actual_end"]:
            duration = (update_data["actual_end"] - update_data["actual_start"]).total_seconds() / 3600
            update_data["duration_hours"] = duration
    
    for field, value in update_data.items():
        setattr(session, field, value)
    
    db.commit()
    db.refresh(session)
    return session


@router.post("/{session_id}/start", response_model=session_schema.Session)
def start_session(
    session_id: int,
    db: Session = Depends(get_db)
):
    """
    Mark a session as started.
    """
    session = db.query(session_model.Session).filter(
        session_model.Session.id == session_id
    ).first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    session.is_active = True
    session.actual_start = datetime.utcnow()
    db.commit()
    db.refresh(session)
    return session


@router.post("/{session_id}/end", response_model=session_schema.Session)
def end_session(
    session_id: int,
    db: Session = Depends(get_db)
):
    """
    Mark a session as completed.
    """
    session = db.query(session_model.Session).filter(
        session_model.Session.id == session_id
    ).first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    session.is_active = False
    session.is_completed = True
    session.actual_end = datetime.utcnow()
    
    # Calculate duration if actual times are available
    if session.actual_start and session.actual_end:
        duration = (session.actual_end - session.actual_start).total_seconds() / 3600
        session.duration_hours = duration
    
    db.commit()
    db.refresh(session)
    return session


@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_session(
    session_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a session.
    """
    session = db.query(session_model.Session).filter(
        session_model.Session.id == session_id
    ).first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    db.delete(session)
    db.commit()
    return None
