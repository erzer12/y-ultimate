# Placeholder for ChildProfile schemas
from pydantic import BaseModel

class ChildProfileBase(BaseModel):
    first_name: str
    last_name: str | None = None

class ChildProfileCreate(ChildProfileBase):
    pass

class ChildProfile(ChildProfileBase):
    id: int
    
    class Config:
        from_attributes = True
