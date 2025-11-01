from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from ....db.session import get_db
from ....models import attendance as attendance_model
from ....schemas import attendance as attendance_schema

router = APIRouter()


@router.post("/", response_model=attendance_schema.Attendance, status_code=status.HTTP_201_CREATED)
def create_attendance(
    attendance: attendance_schema.AttendanceCreate,
    db: Session = Depends(get_db)
):
    """
    Create a single attendance record.
    """
    db_attendance = attendance_model.Attendance(**attendance.model_dump())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


@router.post("/bulk", status_code=status.HTTP_201_CREATED)
def create_bulk_attendance(
    bulk_data: attendance_schema.AttendanceBulkCreate,
    db: Session = Depends(get_db)
):
    """
    Create multiple attendance records at once (for marking a whole session).
    """
    created_records = []
    
    for record in bulk_data.attendance_records:
        db_attendance = attendance_model.Attendance(
            session_id=bulk_data.session_id,
            coach_id=bulk_data.coach_id,
            child_id=record["child_id"],
            present=record["present"],
            notes=record.get("notes", "")
        )
        db.add(db_attendance)
        created_records.append(db_attendance)
    
    db.commit()
    
    return {
        "message": f"Created {len(created_records)} attendance records",
        "count": len(created_records)
    }


@router.get("/", response_model=List[attendance_schema.Attendance])
def list_attendance(
    skip: int = 0,
    limit: int = 100,
    session_id: int = None,
    child_id: int = None,
    coach_id: int = None,
    db: Session = Depends(get_db)
):
    """
    Get attendance records with optional filtering.
    """
    query = db.query(attendance_model.Attendance)
    
    if session_id:
        query = query.filter(attendance_model.Attendance.session_id == session_id)
    if child_id:
        query = query.filter(attendance_model.Attendance.child_id == child_id)
    if coach_id:
        query = query.filter(attendance_model.Attendance.coach_id == coach_id)
    
    records = query.offset(skip).limit(limit).all()
    return records


@router.get("/{attendance_id}", response_model=attendance_schema.Attendance)
def get_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific attendance record by ID.
    """
    attendance = db.query(attendance_model.Attendance).filter(
        attendance_model.Attendance.id == attendance_id
    ).first()
    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found"
        )
    return attendance


@router.put("/{attendance_id}", response_model=attendance_schema.Attendance)
def update_attendance(
    attendance_id: int,
    attendance_update: attendance_schema.AttendanceUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an attendance record.
    """
    attendance = db.query(attendance_model.Attendance).filter(
        attendance_model.Attendance.id == attendance_id
    ).first()
    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found"
        )
    
    update_data = attendance_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(attendance, field, value)
    
    db.commit()
    db.refresh(attendance)
    return attendance


@router.delete("/{attendance_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an attendance record.
    """
    attendance = db.query(attendance_model.Attendance).filter(
        attendance_model.Attendance.id == attendance_id
    ).first()
    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found"
        )
    
    db.delete(attendance)
    db.commit()
    return None
