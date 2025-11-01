from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ....db.session import get_db
from ....models import lsas_assessment as assessment_model
from ....schemas import lsas_assessment as assessment_schema

router = APIRouter()


@router.post("/", response_model=assessment_schema.LSASAssessment, status_code=status.HTTP_201_CREATED)
def create_assessment(
    assessment: assessment_schema.LSASAssessmentCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new LSAS assessment.
    """
    db_assessment = assessment_model.LSASAssessment(**assessment.model_dump())
    db.add(db_assessment)
    db.commit()
    db.refresh(db_assessment)
    return db_assessment


@router.get("/", response_model=List[assessment_schema.LSASAssessment])
def list_assessments(
    skip: int = 0,
    limit: int = 100,
    child_id: int = None,
    assessment_type: str = None,
    db: Session = Depends(get_db)
):
    """
    Get all assessments with optional filtering.
    """
    query = db.query(assessment_model.LSASAssessment)
    
    if child_id:
        query = query.filter(assessment_model.LSASAssessment.child_id == child_id)
    if assessment_type:
        query = query.filter(assessment_model.LSASAssessment.assessment_type == assessment_type)
    
    assessments = query.offset(skip).limit(limit).all()
    return assessments


@router.get("/{assessment_id}", response_model=assessment_schema.LSASAssessment)
def get_assessment(
    assessment_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific assessment by ID.
    """
    assessment = db.query(assessment_model.LSASAssessment).filter(
        assessment_model.LSASAssessment.id == assessment_id
    ).first()
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found"
        )
    return assessment


@router.get("/child/{child_id}/progress")
def get_child_assessment_progress(
    child_id: int,
    db: Session = Depends(get_db)
):
    """
    Get assessment progress for a specific child, showing trends over time.
    """
    assessments = db.query(assessment_model.LSASAssessment).filter(
        assessment_model.LSASAssessment.child_id == child_id
    ).order_by(assessment_model.LSASAssessment.assessment_date).all()
    
    if not assessments:
        return {
            "child_id": child_id,
            "assessments": [],
            "trend": "No assessments available"
        }
    
    # Calculate progress
    baseline = next((a for a in assessments if a.assessment_type == "baseline"), None)
    latest = assessments[-1]
    
    progress = {}
    if baseline and latest and baseline.id != latest.id:
        if baseline.overall_score and latest.overall_score:
            progress["overall_improvement"] = latest.overall_score - baseline.overall_score
        if baseline.leadership_score and latest.leadership_score:
            progress["leadership_improvement"] = latest.leadership_score - baseline.leadership_score
        if baseline.teamwork_score and latest.teamwork_score:
            progress["teamwork_improvement"] = latest.teamwork_score - baseline.teamwork_score
        if baseline.communication_score and latest.communication_score:
            progress["communication_improvement"] = latest.communication_score - baseline.communication_score
        if baseline.confidence_score and latest.confidence_score:
            progress["confidence_improvement"] = latest.confidence_score - baseline.confidence_score
        if baseline.resilience_score and latest.resilience_score:
            progress["resilience_improvement"] = latest.resilience_score - baseline.resilience_score
    
    return {
        "child_id": child_id,
        "total_assessments": len(assessments),
        "assessments": assessments,
        "progress": progress,
        "baseline_date": baseline.assessment_date if baseline else None,
        "latest_date": latest.assessment_date if latest else None
    }


@router.put("/{assessment_id}", response_model=assessment_schema.LSASAssessment)
def update_assessment(
    assessment_id: int,
    assessment_update: assessment_schema.LSASAssessmentUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an assessment.
    """
    assessment = db.query(assessment_model.LSASAssessment).filter(
        assessment_model.LSASAssessment.id == assessment_id
    ).first()
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found"
        )
    
    update_data = assessment_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(assessment, field, value)
    
    db.commit()
    db.refresh(assessment)
    return assessment


@router.delete("/{assessment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assessment(
    assessment_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an assessment.
    """
    assessment = db.query(assessment_model.LSASAssessment).filter(
        assessment_model.LSASAssessment.id == assessment_id
    ).first()
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found"
        )
    
    db.delete(assessment)
    db.commit()
    return None
