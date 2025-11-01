from pydantic import BaseModel, EmailStr

# --- UserBase ---
# This contains the common fields that are
# shared by other schemas.
class UserBase(BaseModel):
    email: EmailStr

# --- UserCreate ---
# This is the schema used when *creating* a new user.
# It requires a password.
class UserCreate(UserBase):
    password: str
    is_admin: bool = False

# --- User ---
# This is the schema used when *reading* a user from the API.
# Notice it does NOT include the password.
# 'from_attributes' tells Pydantic to read from the SQLAlchemy model.
class User(UserBase):
    id: int
    is_admin: bool

    class Config:
        from_attributes = True
