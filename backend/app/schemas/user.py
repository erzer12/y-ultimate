from pydantic import BaseModel, EmailStr
from typing import Optional


# --- UserBase ---
# This contains the common fields that are
# shared by other schemas.
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


# --- UserCreate ---
# This is the schema used when *creating* a new user.
# It requires a password.
class UserCreate(UserBase):
    password: str
    role: str = "coach"  # admin, manager, coach, reporting, coordinator
    is_admin: bool = False


# --- UserUpdate ---
# Schema for updating a user
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None


# --- User ---
# This is the schema used when *reading* a user from the API.
# Notice it does NOT include the password.
# 'from_attributes' tells Pydantic to read from the SQLAlchemy model.
class User(UserBase):
    id: int
    role: str
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True

