from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ....db.session import get_db
from ....models import match as match_model
from ....models import team as team_model
from ....schemas import match as match_schema

router = APIRouter()


@router.post("/", response_model=match_schema.Match, status_code=status.HTTP_201_CREATED)
def create_match(
    match: match_schema.MatchCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new match.
    """
    db_match = match_model.Match(**match.model_dump())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match


@router.get("/", response_model=List[match_schema.Match])
def list_matches(
    skip: int = 0,
    limit: int = 100,
    tournament_id: int = None,
    is_completed: bool = None,
    round: str = None,
    db: Session = Depends(get_db)
):
    """
    Get all matches with optional filtering.
    """
    query = db.query(match_model.Match)
    
    if tournament_id:
        query = query.filter(match_model.Match.tournament_id == tournament_id)
    if is_completed is not None:
        query = query.filter(match_model.Match.is_completed == is_completed)
    if round:
        query = query.filter(match_model.Match.round == round)
    
    matches = query.offset(skip).limit(limit).all()
    return matches


@router.get("/{match_id}", response_model=match_schema.MatchWithTeams)
def get_match(
    match_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific match by ID with team names.
    """
    match = db.query(match_model.Match).filter(
        match_model.Match.id == match_id
    ).first()
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found"
        )
    
    # Get team names
    team1 = db.query(team_model.Team).filter(team_model.Team.id == match.team1_id).first()
    team2 = db.query(team_model.Team).filter(team_model.Team.id == match.team2_id).first()
    winner = db.query(team_model.Team).filter(team_model.Team.id == match.winner_id).first() if match.winner_id else None
    
    match_dict = {
        **match.__dict__,
        "team1_name": team1.name if team1 else "Unknown",
        "team2_name": team2.name if team2 else "Unknown",
        "winner_name": winner.name if winner else None
    }
    
    return match_dict


@router.put("/{match_id}/score", response_model=match_schema.Match)
def update_match_score(
    match_id: int,
    match_update: match_schema.MatchUpdate,
    db: Session = Depends(get_db)
):
    """
    Update match score and status.
    """
    match = db.query(match_model.Match).filter(
        match_model.Match.id == match_id
    ).first()
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found"
        )
    
    update_data = match_update.model_dump(exclude_unset=True)
    
    # Update match fields
    for field, value in update_data.items():
        setattr(match, field, value)
    
    # Determine winner if scores are provided
    if "team1_score" in update_data and "team2_score" in update_data:
        if match.team1_score > match.team2_score:
            match.winner_id = match.team1_id
        elif match.team2_score > match.team1_score:
            match.winner_id = match.team2_id
        # If scores are equal, no winner (draw)
    
    # Update team statistics if match is completed
    if match.is_completed:
        team1 = db.query(team_model.Team).filter(team_model.Team.id == match.team1_id).first()
        team2 = db.query(team_model.Team).filter(team_model.Team.id == match.team2_id).first()
        
        if team1:
            team1.points_for += match.team1_score
            team1.points_against += match.team2_score
            if match.winner_id == team1.id:
                team1.wins += 1
            elif match.winner_id == team2.id:
                team1.losses += 1
            else:
                team1.draws += 1
            
            if match.team1_spirit_score:
                team1.spirit_score_total += int(match.team1_spirit_score)
        
        if team2:
            team2.points_for += match.team2_score
            team2.points_against += match.team1_score
            if match.winner_id == team2.id:
                team2.wins += 1
            elif match.winner_id == team1.id:
                team2.losses += 1
            else:
                team2.draws += 1
            
            if match.team2_spirit_score:
                team2.spirit_score_total += int(match.team2_spirit_score)
    
    db.commit()
    db.refresh(match)
    return match


@router.put("/{match_id}", response_model=match_schema.Match)
def update_match(
    match_id: int,
    match_update: match_schema.MatchUpdate,
    db: Session = Depends(get_db)
):
    """
    Update match details.
    """
    match = db.query(match_model.Match).filter(
        match_model.Match.id == match_id
    ).first()
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found"
        )
    
    update_data = match_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(match, field, value)
    
    db.commit()
    db.refresh(match)
    return match


@router.delete("/{match_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_match(
    match_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a match.
    """
    match = db.query(match_model.Match).filter(
        match_model.Match.id == match_id
    ).first()
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found"
        )
    
    db.delete(match)
    db.commit()
    return None
