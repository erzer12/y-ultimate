"""
FastAPI Main Application Entry Point

This is the main file that creates and configures the FastAPI application.
When you run `uvicorn app.main:app`, Python looks for the 'app' object in this file.

Key components:
  1. FastAPI() instance: The core application object
  2. CORSMiddleware: CRITICAL for allowing the frontend to make requests to this backend
  3. Router inclusion: Connects all API endpoints from app/api/v1/api.py
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings

# Create the FastAPI application instance
# This is the main object that handles all HTTP requests
app = FastAPI(
    title="Y-Ultimate Management Platform API",
    description="Backend API for managing tournaments, teams, and player profiles",
    version="1.0.0",
    # Customize the auto-generated API documentation
    docs_url="/docs",  # Swagger UI at http://localhost:8000/docs
    redoc_url="/redoc",  # ReDoc at http://localhost:8000/redoc
)

# === CORS Configuration ===
# CORS (Cross-Origin Resource Sharing) is CRITICAL for web applications.
# 
# The Problem:
#   By default, browsers block JavaScript requests from one origin (domain/port)
#   to another origin. Your React frontend runs on http://localhost:5173, and
#   your FastAPI backend runs on http://localhost:8000. These are different
#   origins, so the browser will block requests from the frontend to the backend.
#
# The Solution:
#   Add CORSMiddleware to tell the browser which origins are allowed to make requests.
#   The backend sends special CORS headers in its responses, which tell the browser
#   "it's okay, I trust requests from http://localhost:5173".
#
# Configuration:
#   - allow_origins: List of allowed origins (the React frontend URL)
#   - allow_credentials: Allow cookies/authentication headers
#   - allow_methods: Which HTTP methods are allowed (GET, POST, etc.)
#   - allow_headers: Which headers are allowed (Authorization, Content-Type, etc.)
#
# IMPORTANT: In production, replace ["http://localhost:5173"] with your actual
# frontend domain (e.g., ["https://yourdomain.com"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # React dev server
        "http://localhost:3000",  # Alternative React port
        # Add your production frontend URL here when deploying
    ],
    allow_credentials=True,  # Allow cookies and Authorization headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# === Include API Router ===
# This connects all the endpoints from app/api/v1/api.py to the main app.
# The api_router includes all endpoint files (auth.py, tournaments.py, etc.)
# The prefix="/api" means all routes will start with /api
#
# Example routes:
#   - POST /api/v1/auth/login
#   - GET /api/v1/tournaments/
#   - POST /api/v1/teams/
app.include_router(api_router, prefix="/api/v1")


# === Root Endpoint ===
# A simple endpoint to verify the API is running
@app.get("/")
def root():
    """
    Root endpoint
    
    Returns a welcome message.
    Visit http://localhost:8000 to see this response.
    """
    return {
        "message": "Welcome to Y-Ultimate Management Platform API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


# === Health Check Endpoint ===
# Useful for monitoring and deployment systems
@app.get("/health")
def health_check():
    """
    Health check endpoint
    
    Returns the API status.
    Useful for monitoring tools and container orchestration systems.
    """
    return {"status": "healthy"}
