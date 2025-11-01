from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from ....db.session import get_db
from ....models import team as team_model
from ....models import match as match_model
from ....schemas import team as team_schema

router = APIRouter()


@router.post("/", response_model=team_schema.Team, status_code=status.HTTP_201_CREATED)
def create_team(
    team: team_schema.TeamCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new team.
    """
    db_team = team_model.Team(**team.model_dump())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


@router.get("/", response_model=List[team_schema.Team])
def list_teams(
    skip: int = 0,
    limit: int = 100,
    tournament_id: int = None,
    is_active: bool = None,
    db: Session = Depends(get_db)
):
    """
    Get all teams with optional filtering.
    """
    query = db.query(team_model.Team)
    
    if tournament_id:
        query = query.filter(team_model.Team.tournament_id == tournament_id)
    if is_active is not None:
        query = query.filter(team_model.Team.is_active == is_active)
    
    teams = query.offset(skip).limit(limit).all()
    return teams


@router.get("/{team_id}", response_model=team_schema.Team)
def get_team(
    team_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific team by ID.
    """
    team = db.query(team_model.Team).filter(team_model.Team.id == team_id).first()
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    return team


@router.get("/{team_id}/stats", response_model=team_schema.TeamWithStats)
def get_team_with_stats(
    team_id: int,
    db: Session = Depends(get_db)
):
    """
    Get team with statistics.
    """
    team = db.query(team_model.Team).filter(team_model.Team.id == team_id).first()
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    # Get match count
    total_matches = db.query(func.count(match_model.Match.id)).filter(
        (match_model.Match.team1_id == team_id) | (match_model.Match.team2_id == team_id)
    ).scalar() or 0
    
    # Calculate stats
    win_percentage = (team.wins / total_matches * 100) if total_matches > 0 else 0.0
    average_spirit_score = (team.spirit_score_total / total_matches) if total_matches > 0 else 0.0
    point_differential = team.points_for - team.points_against
    
    team_dict = {
        **team.__dict__,
        "total_matches": total_matches,
        "win_percentage": round(win_percentage, 2),
        "average_spirit_score": round(average_spirit_score, 2),
        "point_differential": point_differential
    }
    
    return team_dict


@router.put("/{team_id}", response_model=team_schema.Team)
def update_team(
    team_id: int,
    team_update: team_schema.TeamUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a team.
    """
    team = db.query(team_model.Team).filter(team_model.Team.id == team_id).first()
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    update_data = team_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(team, field, value)
    
    db.commit()
    db.refresh(team)
    return team


@router.delete("/{team_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_team(
    team_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a team.
    """
    team = db.query(team_model.Team).filter(team_model.Team.id == team_id).first()
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    db.delete(team)
    db.commit()
    return None
