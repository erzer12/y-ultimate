# Y-Ultimate Management Platform - Setup Guide

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Configuration](#environment-configuration)
- [Running the Application](#running-the-application)
- [Database Setup](#database-setup)
- [Development Mode](#development-mode)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker & Docker Compose** (v20.10+) - For containerized deployment
- **Node.js** (v18+) - For frontend development
- **Python** (v3.12+) - For backend development
- **PostgreSQL** (v15+) - For database (or use Docker)
- **Git** - For version control

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/erzer12/y-ultimate.git
cd y-ultimate
```

### 2. Install Dependencies

#### Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Frontend Dependencies
```bash
cd frontend
npm install
```

## Environment Configuration

### 1. Copy Environment Template

```bash
cp .env.example .env
```

### 2. Configure Environment Variables

Edit the `.env` file with your settings:

```env
# === PostgreSQL Database ===
DATABASE_URL="postgresql://user:password@localhost:5432/yultimate_db"

# === FastAPI Backend ===
# Generate a strong random key using: openssl rand -hex 32
JWT_SECRET_KEY="your_super_secret_random_key_here"
JWT_ALGORITHM="HS256"
```

#### Generating a Secure JWT Secret Key

```bash
# On Linux/Mac
openssl rand -hex 32

# On Windows (PowerShell)
python -c "import secrets; print(secrets.token_hex(32))"
```

## Running the Application

### Option 1: Docker Compose (Recommended)

Start all services with a single command:

```bash
docker compose up -d --build
```

This will start:
- **PostgreSQL Database** on port `5432`
- **Backend API** on port `8000`
- **Frontend** on port `5173`

Access the application:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Option 2: Manual Setup (Development)

#### Start PostgreSQL
```bash
docker compose up -d db
```

#### Start Backend
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Start Frontend
```bash
cd frontend
npm run dev
```

## Database Setup

### 1. Database Migrations (Using Alembic)

Initialize Alembic (first time only):
```bash
cd backend
alembic init alembic
```

Create a migration:
```bash
alembic revision --autogenerate -m "Initial migration"
```

Apply migrations:
```bash
alembic upgrade head
```

### 2. Seed Mock Data

Load sample data for development and testing:

```bash
cd backend
python scripts/seed_data.py
```

This will create:
- Sample users (coaches, managers, admins)
- Child profiles
- Sessions and attendance records
- Assessments
- Tournaments and matches

## Development Mode

### Hot Reload

Both frontend and backend support hot reload:

- **Frontend**: Vite automatically reloads on file changes
- **Backend**: Uvicorn `--reload` flag watches for Python file changes

### API Testing

Use the interactive API documentation:

1. Navigate to http://localhost:8000/docs
2. Try out endpoints directly in the browser
3. View request/response schemas

### Mock Data

The application includes mock data mode for testing without a database:

```bash
# Backend with mock data
cd backend
python app/main.py --mock-mode
```

## Troubleshooting

### Port Already in Use

If ports 5173, 8000, or 5432 are already in use:

```bash
# Check what's using the port
lsof -i :5173
lsof -i :8000
lsof -i :5432

# Kill the process
kill -9 <PID>
```

Or modify ports in `docker-compose.yaml`.

### Database Connection Issues

1. Verify PostgreSQL is running:
```bash
docker compose ps
```

2. Test connection:
```bash
psql -h localhost -U user -d yultimate_db
```

3. Check database logs:
```bash
docker compose logs db
```

### Frontend Build Issues

Clear cache and reinstall:
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Backend Import Errors

Ensure you're in the correct directory and virtual environment:
```bash
cd backend
python -c "import app; print('Success!')"
```

## Next Steps

- 📖 Read the [Feature Walkthrough](FEATURE_WALKTHROUGH.md)
- 🗺️ View the [Data Model Diagram](DATA_MODEL.md)
- 📚 Explore the [API Reference](http://localhost:8000/docs)
- 🤝 Check out the [Contribution Guide](CONTRIBUTING.md)

## Support

For issues and questions:
- GitHub Issues: https://github.com/erzer12/y-ultimate/issues
- Documentation: See docs/ folder

---

**Happy Coding! 🏐**
