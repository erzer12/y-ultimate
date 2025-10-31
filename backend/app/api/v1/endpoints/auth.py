"""
Authentication Endpoints

This file contains all authentication-related endpoints:
  - POST /login: User login (returns JWT token)
  - POST /register: User registration
  - GET /me: Get current user info

These endpoints handle user authentication using JWT tokens.
The OAuth2PasswordRequestForm is a FastAPI dependency that extracts
username and password from a form post (standard OAuth2 format).
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.token import Token
from app.schemas.user import User, UserCreate

# Create a router for authentication endpoints
router = APIRouter()


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    User Login Endpoint
    
    Accepts a username (email) and password, validates credentials,
    and returns a JWT token if successful.
    
    OAuth2PasswordRequestForm is a FastAPI dependency that:
      - Expects form data (not JSON) with fields 'username' and 'password'
      - Is the standard OAuth2 format for password-based authentication
    
    Steps to implement (placeholder):
      1. Query the database for a user with the given email (form_data.username)
      2. Verify the password using passlib (compare hashed_password)
      3. Create a JWT token using python-jose
      4. Return the token
    
    Example request (form data):
      username: user@example.com
      password: securepassword123
    
    Example response:
      {
          "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
          "token_type": "bearer"
      }
    """
    # TODO: Implement login logic
    # 1. Find user by email: user = db.query(User).filter(User.email == form_data.username).first()
    # 2. Verify password: if not verify_password(form_data.password, user.hashed_password): raise HTTPException
    # 3. Create JWT token: token = create_access_token(data={"sub": str(user.id)})
    # 4. Return token: return {"access_token": token, "token_type": "bearer"}
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Login endpoint not yet implemented"
    )


@router.post("/register", response_model=User)
def register(
    user_in: UserCreate,
    db: Session = Depends(get_db)
):
    """
    User Registration Endpoint
    
    Creates a new user account.
    
    Steps to implement (placeholder):
      1. Check if email already exists
      2. Hash the password using passlib
      3. Create the user in the database
      4. Return the created user (without password)
    
    Example request (JSON):
      {
          "email": "newuser@example.com",
          "password": "securepassword123",
          "full_name": "Jane Doe"
      }
    
    Example response:
      {
          "id": 1,
          "email": "newuser@example.com",
          "full_name": "Jane Doe",
          "is_active": true,
          "is_admin": false
      }
    """
    # TODO: Implement registration logic
    # 1. Check if user exists: existing = db.query(User).filter(User.email == user_in.email).first()
    # 2. Hash password: hashed_pwd = get_password_hash(user_in.password)
    # 3. Create user: user = User(email=user_in.email, hashed_password=hashed_pwd, ...)
    # 4. Save to DB: db.add(user); db.commit(); db.refresh(user)
    # 5. Return user: return user
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Register endpoint not yet implemented"
    )
