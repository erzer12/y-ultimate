from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db.session import get_db, engine # Import from our new 'db' folder
from .api.v1.api import api_router # Import our new V1 router
from fastapi.middleware.cors import CORSMiddleware

# Create the main FastAPI application instance
app = FastAPI()

# --- CORS Middleware ---
# This is CRITICAL for your frontend to talk to your backend
# It allows requests from your React app (running on localhost:5173)
app.add_middleware(
    CORSMiddleware,
    # This list should contain the URL of your React app
    allow_origins=[
        "http://localhost:5173", 
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)

# --- Include API Routers ---
# This line adds all the routes from 'api/v1/api.py'
# All routes from api_router will be prefixed with '/api/v1'
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root(db: Session = Depends(get_db)):
    """
    This is the main root endpoint.
    It's a good place to check if the server is running
    and if the database connection is healthy.
    """
    try:
        # Try to execute a simple query
        db.execute("SELECT 1")
        return {"message": "Y-Ultimate API is running!", "database_status": "Connected"}
    except Exception as e:
        # If the DB connection fails, return an error
        return {"message": "Y-Ultimate API is running!", "database_status": "Connection FAILED", "error": str(e)}

