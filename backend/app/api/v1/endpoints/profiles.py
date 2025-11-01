from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from typing import List
from datetime import date, datetime
import json
from ....db.session import get_db
from ....models import child_profile as profile_model
from ....models import attendance as attendance_model
from ....models import lsas_assessment as assessment_model
from ....schemas import child_profile as profile_schema

router = APIRouter()


@router.post("/", response_model=profile_schema.ChildProfile, status_code=status.HTTP_201_CREATED)
def create_child_profile(
    profile: profile_schema.ChildProfileCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new child profile.
    """
    db_profile = profile_model.ChildProfile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


@router.get("/", response_model=List[profile_schema.ChildProfile])
def list_child_profiles(
    skip: int = 0,
    limit: int = 100,
    is_active: bool = None,
    school: str = None,
    community: str = None,
    search: str = None,
    db: Session = Depends(get_db)
):
    """
    Get all child profiles with optional filtering.
    """
    query = db.query(profile_model.ChildProfile)
    
    if is_active is not None:
        query = query.filter(profile_model.ChildProfile.is_active == is_active)
    if school:
        query = query.filter(profile_model.ChildProfile.school == school)
    if community:
        query = query.filter(profile_model.ChildProfile.community == community)
    if search:
        query = query.filter(
            or_(
                profile_model.ChildProfile.name.ilike(f"%{search}%"),
                profile_model.ChildProfile.parent_name.ilike(f"%{search}%")
            )
        )
    
    profiles = query.offset(skip).limit(limit).all()
    return profiles


@router.get("/{profile_id}", response_model=profile_schema.ChildProfile)
def get_child_profile(
    profile_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific child profile by ID.
    """
    profile = db.query(profile_model.ChildProfile).filter(
        profile_model.ChildProfile.id == profile_id
    ).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Child profile not found"
        )
    return profile


@router.get("/{profile_id}/stats", response_model=profile_schema.ChildProfileWithStats)
def get_child_profile_with_stats(
    profile_id: int,
    db: Session = Depends(get_db)
):
    """
    Get child profile with attendance and assessment statistics.
    """
    profile = db.query(profile_model.ChildProfile).filter(
        profile_model.ChildProfile.id == profile_id
    ).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Child profile not found"
        )
    
    # Get attendance stats
    total_sessions = db.query(func.count(attendance_model.Attendance.id)).filter(
        attendance_model.Attendance.child_id == profile_id
    ).scalar() or 0
    
    sessions_attended = db.query(func.count(attendance_model.Attendance.id)).filter(
        attendance_model.Attendance.child_id == profile_id,
        attendance_model.Attendance.present == True
    ).scalar() or 0
    
    attendance_rate = (sessions_attended / total_sessions * 100) if total_sessions > 0 else 0.0
    
    # Get latest assessment
    latest_assessment = db.query(assessment_model.LSASAssessment).filter(
        assessment_model.LSASAssessment.child_id == profile_id
    ).order_by(assessment_model.LSASAssessment.assessment_date.desc()).first()
    
    profile_dict = {
        **profile.__dict__,
        "total_sessions": total_sessions,
        "sessions_attended": sessions_attended,
        "attendance_rate": round(attendance_rate, 2),
        "latest_assessment_date": latest_assessment.assessment_date if latest_assessment else None,
        "latest_assessment_score": latest_assessment.overall_score if latest_assessment else None
    }
    
    return profile_dict


@router.put("/{profile_id}", response_model=profile_schema.ChildProfile)
def update_child_profile(
    profile_id: int,
    profile_update: profile_schema.ChildProfileUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a child profile.
    """
    profile = db.query(profile_model.ChildProfile).filter(
        profile_model.ChildProfile.id == profile_id
    ).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Child profile not found"
        )
    
    update_data = profile_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(profile, field, value)
    
    db.commit()
    db.refresh(profile)
    return profile


@router.post("/{profile_id}/transfer")
def transfer_child(
    profile_id: int,
    transfer_data: profile_schema.ChildTransfer,
    db: Session = Depends(get_db)
):
    """
    Transfer a child between schools or communities.
    """
    profile = db.query(profile_model.ChildProfile).filter(
        profile_model.ChildProfile.id == profile_id
    ).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Child profile not found"
        )
    
    # Update transfer history
    transfer_record = {
        "from": transfer_data.from_location,
        "to": transfer_data.to_location,
        "date": transfer_data.transfer_date.isoformat(),
        "reason": transfer_data.reason or ""
    }
    
    # Load existing history or create new
    history = []
    if profile.transfer_history:
        try:
            history = json.loads(profile.transfer_history)
        except:
            history = []
    
    history.append(transfer_record)
    profile.transfer_history = json.dumps(history)
    
    # Update location fields
    if "school" in transfer_data.to_location.lower():
        profile.school = transfer_data.to_location
    elif "community" in transfer_data.to_location.lower():
        profile.community = transfer_data.to_location
    
    db.commit()
    db.refresh(profile)
    
    return {
        "message": "Transfer completed successfully",
        "profile": profile,
        "transfer_history": history
    }


@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_child_profile(
    profile_id: int,
    db: Session = Depends(get_db)
):
    """
    Soft delete a child profile (mark as inactive).
    """
    profile = db.query(profile_model.ChildProfile).filter(
        profile_model.ChildProfile.id == profile_id
    ).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Child profile not found"
        )
    
    profile.is_active = False
    profile.exit_date = date.today()
    db.commit()
    return None
