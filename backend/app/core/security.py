"""
Security Utilities

This file will contain all security-related utility functions:
  - Password hashing (using passlib with bcrypt)
  - Password verification
  - JWT token creation
  - JWT token verification
  - Current user dependency (for protected routes)

These functions are used by the authentication endpoints and any
protected routes that require an authenticated user.
"""

from datetime import datetime, timedelta
from typing import Any

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

# Password hashing context
# This uses bcrypt algorithm for secure password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain text password against a hashed password.
    
    Args:
        plain_password: The password entered by the user
        hashed_password: The hashed password from the database
    
    Returns:
        True if the password matches, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash a plain text password.
    
    Args:
        password: The plain text password to hash
    
    Returns:
        The hashed password (safe to store in database)
    """
    return pwd_context.hash(password)


def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    """
    Create a JWT access token.
    
    Args:
        data: The data to encode in the token (usually {"sub": user_id})
        expires_delta: How long until the token expires (optional)
    
    Returns:
        The encoded JWT token as a string
    
    Example:
        token = create_access_token(data={"sub": str(user.id)})
    """
    to_encode = data.copy()
    
    # Set expiration time
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    # Encode the JWT token
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
    
    return encoded_jwt


# TODO: Add get_current_user dependency
# This function would:
#   1. Extract the JWT token from the Authorization header
#   2. Decode and verify the token
#   3. Get the user from the database
#   4. Return the user (or raise 401 if invalid)
#
# Usage in routes:
#   @router.get("/protected")
#   def protected_route(current_user: User = Depends(get_current_user)):
#       return {"message": f"Hello {current_user.email}"}
