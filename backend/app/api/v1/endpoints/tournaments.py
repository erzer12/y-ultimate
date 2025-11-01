from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from ....db.session import get_db
from ....models import tournament as tournament_model
from ....models import team as team_model
from ....models import match as match_model
from ....models import player_registration as registration_model
from ....schemas import tournament as tournament_schema

router = APIRouter()


@router.post("/", response_model=tournament_schema.Tournament, status_code=status.HTTP_201_CREATED)
def create_tournament(
    tournament: tournament_schema.TournamentCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new tournament.
    """
    db_tournament = tournament_model.Tournament(**tournament.model_dump())
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament


@router.get("/", response_model=List[tournament_schema.Tournament])
def list_tournaments(
    skip: int = 0,
    limit: int = 100,
    status: str = None,
    is_published: bool = None,
    db: Session = Depends(get_db)
):
    """
    Get all tournaments with optional filtering.
    """
    query = db.query(tournament_model.Tournament)
    
    if status:
        query = query.filter(tournament_model.Tournament.status == status)
    if is_published is not None:
        query = query.filter(tournament_model.Tournament.is_published == is_published)
    
    tournaments = query.offset(skip).limit(limit).all()
    return tournaments


@router.get("/{tournament_id}", response_model=tournament_schema.Tournament)
def get_tournament(
    tournament_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific tournament by ID.
    """
    tournament = db.query(tournament_model.Tournament).filter(
        tournament_model.Tournament.id == tournament_id
    ).first()
    if not tournament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found"
        )
    return tournament


@router.get("/{tournament_id}/stats", response_model=tournament_schema.TournamentWithStats)
def get_tournament_with_stats(
    tournament_id: int,
    db: Session = Depends(get_db)
):
    """
    Get tournament with statistics.
    """
    tournament = db.query(tournament_model.Tournament).filter(
        tournament_model.Tournament.id == tournament_id
    ).first()
    if not tournament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found"
        )
    
    # Get statistics
    total_teams = db.query(func.count(team_model.Team.id)).filter(
        team_model.Team.tournament_id == tournament_id
    ).scalar() or 0
    
    total_matches = db.query(func.count(match_model.Match.id)).filter(
        match_model.Match.tournament_id == tournament_id
    ).scalar() or 0
    
    completed_matches = db.query(func.count(match_model.Match.id)).filter(
        match_model.Match.tournament_id == tournament_id,
        match_model.Match.is_completed == True
    ).scalar() or 0
    
    total_registrations = db.query(func.count(registration_model.PlayerRegistration.id)).filter(
        registration_model.PlayerRegistration.tournament_id == tournament_id
    ).scalar() or 0
    
    approved_registrations = db.query(func.count(registration_model.PlayerRegistration.id)).filter(
        registration_model.PlayerRegistration.tournament_id == tournament_id,
        registration_model.PlayerRegistration.is_approved == True
    ).scalar() or 0
    
    tournament_dict = {
        **tournament.__dict__,
        "total_teams": total_teams,
        "total_matches": total_matches,
        "completed_matches": completed_matches,
        "total_registrations": total_registrations,
        "approved_registrations": approved_registrations
    }
    
    return tournament_dict


@router.put("/{tournament_id}", response_model=tournament_schema.Tournament)
def update_tournament(
    tournament_id: int,
    tournament_update: tournament_schema.TournamentUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a tournament.
    """
    tournament = db.query(tournament_model.Tournament).filter(
        tournament_model.Tournament.id == tournament_id
    ).first()
    if not tournament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found"
        )
    
    update_data = tournament_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(tournament, field, value)
    
    db.commit()
    db.refresh(tournament)
    return tournament


@router.delete("/{tournament_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tournament(
    tournament_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a tournament.
    """
    tournament = db.query(tournament_model.Tournament).filter(
        tournament_model.Tournament.id == tournament_id
    ).first()
    if not tournament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found"
        )
    
    db.delete(tournament)
    db.commit()
    return None
