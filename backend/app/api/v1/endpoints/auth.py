from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....core import security
from ....models.user import User
from ....schemas.token import Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    This is the main login endpoint.
    It takes a username (which is our email) and password.
    
    FastAPI's 'OAuth2PasswordRequestForm' makes it work
    just like a standard OAuth2 login form.
    """
    
    # 1. Find the user in the database by their email
    user = db.query(User).filter(User.email == form_data.username).first()

    # 2. Check if user exists and the password is correct
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Create the JWT access token
    # We store the user's email in the 'sub' (subject) field
    access_token = security.create_access_token(
        data={"sub": user.email}
    )
    
    # 4. Return the token
    return {"access_token": access_token, "token_type": "bearer"}
