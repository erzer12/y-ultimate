"""
Token Pydantic Schemas

This file will contain the Pydantic schema for a JWT token response.

When a user logs in successfully, the API returns a JWT token.
The schema defines the structure of that response.

Typical fields:
  - access_token: The JWT token string
  - token_type: Usually "bearer" (refers to Bearer token authentication)
"""

from pydantic import BaseModel


class Token(BaseModel):
    """
    Token Response Schema
    
    Used in POST /login endpoint response.
    
    Example JSON response:
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "token_type": "bearer"
    }
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Token Data Schema
    
    Represents the data stored inside a JWT token (the "claims").
    Used when decoding and validating tokens.
    
    Typical claims:
      - sub (subject): The user ID or username
      - exp (expiration): When the token expires (handled automatically by python-jose)
    """
    user_id: int | None = None
