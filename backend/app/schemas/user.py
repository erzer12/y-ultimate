"""
User Pydantic Schemas

CRITICAL CONCEPT: Models vs. Schemas
====================================
This file defines SCHEMAS, not MODELS. Understanding the difference is crucial:

MODELS (in app/models/user.py):
  - Represent the DATABASE TABLE STRUCTURE
  - Define columns, data types, and relationships in the database
  - Used by SQLAlchemy to create/read/update/delete database rows
  - Example: User model with hashed_password column

SCHEMAS (this file):
  - Represent the API DATA STRUCTURE (JSON)
  - Define what data the API accepts (requests) and returns (responses)
  - Used by FastAPI to validate incoming data and serialize outgoing data
  - Example: UserCreate schema with plain text password (for input)
           User schema without hashed_password (for output - security)

Why separate Models and Schemas?
  1. Security: API responses shouldn't include hashed_password
  2. Validation: API inputs need different validation than database fields
  3. Flexibility: API structure can differ from database structure
  4. Documentation: FastAPI auto-generates API docs from schemas

The flow:
  Request (JSON) -> Pydantic Schema (validates) -> SQLAlchemy Model (saves to DB)
  Database Row -> SQLAlchemy Model (loads) -> Pydantic Schema (serializes) -> Response (JSON)
"""

from pydantic import BaseModel, EmailStr, ConfigDict


# === Base Schema ===
# Contains common fields shared by all User schemas
class UserBase(BaseModel):
    """
    Base User Schema
    
    Contains fields that are common to all user-related schemas.
    Other schemas will inherit from this to avoid duplication.
    """
    email: EmailStr  # EmailStr validates that the string is a valid email format
    full_name: str | None = None  # Optional field (can be None)
    is_active: bool = True
    is_admin: bool = False


# === Create Schema ===
# Used when creating a new user (includes password)
class UserCreate(UserBase):
    """
    Schema for Creating a User
    
    Used in POST /users/ endpoint.
    Includes the plain text password, which will be hashed before saving to the database.
    
    Example JSON:
    {
        "email": "user@example.com",
        "password": "securepassword123",
        "full_name": "John Doe"
    }
    """
    password: str  # Plain text password (will be hashed by the backend)


# === Response Schema ===
# Used when returning user data (excludes hashed_password)
class User(UserBase):
    """
    Schema for Reading a User
    
    Used in API responses (GET /users/, GET /users/{id}).
    Does NOT include hashed_password for security reasons.
    
    ConfigDict(from_attributes=True) allows Pydantic to read data from SQLAlchemy models.
    Without this, Pydantic can only read from dictionaries.
    
    Example: 
        user_model = db.query(User).first()  # SQLAlchemy model object
        user_schema = User.model_validate(user_model)  # Converts to Pydantic schema
    
    Example JSON response:
    {
        "id": 1,
        "email": "user@example.com",
        "full_name": "John Doe",
        "is_active": true,
        "is_admin": false
    }
    """
    id: int
    
    # Configure Pydantic to work with SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)
