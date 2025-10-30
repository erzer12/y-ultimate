"""
API Version 1 Router Hub

This file acts as a "collector" or "hub" for all v1 API endpoints.
It imports routers from individual endpoint files and includes them under
a single APIRouter with the /v1 prefix.

Why this pattern?
  1. Organization: Keeps endpoint logic separated by resource (auth, tournaments, etc.)
  2. Versioning: Makes it easy to create v2, v3, etc. without breaking v1
  3. Prefixing: All routes automatically get the /api/v1 prefix
  4. Clean main.py: The main app file just includes this one router

Structure:
  app/main.py includes this router with prefix="/api"
  This router includes auth.py, tournaments.py, etc. with prefix="/v1"
  
  Result: Routes like POST /api/v1/login, GET /api/v1/tournaments
"""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, tournaments, teams, profiles

# Create the main v1 router
api_router = APIRouter()

# Include all endpoint routers
# Each router's routes will be prefixed with its 'prefix' argument and tagged for docs

# Authentication endpoints (login, register, etc.)
api_router.include_router(
    auth.router,
    prefix="/auth",  # Routes will be at /api/v1/auth/...
    tags=["authentication"]  # Groups these routes in the API docs
)

# Tournament endpoints
api_router.include_router(
    tournaments.router,
    prefix="/tournaments",  # Routes will be at /api/v1/tournaments/...
    tags=["tournaments"]
)

# Team endpoints
api_router.include_router(
    teams.router,
    prefix="/teams",  # Routes will be at /api/v1/teams/...
    tags=["teams"]
)

# Child Profile endpoints
api_router.include_router(
    profiles.router,
    prefix="/profiles",  # Routes will be at /api/v1/profiles/...
    tags=["profiles"]
)
