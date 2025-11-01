from pydantic import BaseModel
from datetime import date

class ChildProfileBase(BaseModel):
    name: str
    date_of_birth: date
    school: str | None = None
    community: str | None = None

class ChildProfileCreate(ChildProfileBase):
    pass

class ChildProfile(ChildProfileBase):
    id: int

    class Config:
        from_attributes = True
