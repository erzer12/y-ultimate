# Placeholder for ChildProfile endpoints
from fastapi import APIRuter

router = APIRouter()

@router.get("/")
def read_profiles():
    return [{"profile_name": "Profile 1"}, {"profile_name": "Profile 2"}]
