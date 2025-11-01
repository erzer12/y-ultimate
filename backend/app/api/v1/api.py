from fastapi import APIRouter
from .endpoints import auth

api_router = APIRouter()

# Include the 'auth' router
# All routes from 'auth.py' will now be prefixed with '/auth'
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

# We can add more routers here later, e.g.:
# api_router.include_router(tournaments.router, prefix="/tournaments", tags=["tournaments"])
