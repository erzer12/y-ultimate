# Y-Ultimate Management Platform

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-nodejs](https://img.shields.io/badge/Made%20with-Node.js-339933.svg?logo=node.js)](https://nodejs.org/)
[![made-with-react](https://img.shields.io/badge/Made%20with-React-20232a?logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![made-with-fastapi](https://img.shields.io/badge/Made%20with-FastAPI-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![made-with-express](https://img.shields.io/badge/Made%20with-Express-000000.svg?logo=express)](https://expressjs.com/)

A single, centralized web platform to manage all of Y-Ultimate's operations, replacing scattered Google Sheets with a single source of truth.

This platform manages tournaments, team/player registrations, live scoring, and coaching modules (like Child Profiles and LSAS assessments).

## 🚀 The Core Problem & Solution

* **Problem:** Y-Ultimate's data is fragmented across many manual Google Sheets, leading to slow workflows, data integrity issues, and delayed reporting.
* **Solution:** A modern, monorepo web application with a **React (Vite) frontend** and multiple backend options. This provides a single, responsive, and reliable system for all users (Admins, Coaches, and Parents).

## 🗂️ Project Structure

This is a monorepo, meaning both frontend and backend code live in the same repository.

* **`/backend`**: The FastAPI Python application (legacy/full platform). Contains the API, database models, and business logic for the complete platform.
* **`/backend-node`**: The Node.js + TypeScript + Express MVP (hackathon prototype). A minimal, demo-ready backend with JWT auth, children management, sessions, and attendance tracking using SQLite + Prisma.
* **`/frontend`**: The React (Vite) application. Contains all UI components, pages, and frontend logic. Works with both backends.
* **`/docker-compose.yml`**: Helper file to run the PostgreSQL database for the Python backend.

## 🎯 Quick Start: MVP Hackathon Demo

For the **minimal MVP demo** (ready for Nov 4 hackathon), see **[DEV-SETUP.md](DEV-SETUP.md)** for complete instructions.

**TL;DR:**
```bash
# Start the Node.js backend
cd backend-node
npm install
npm run prisma:migrate
npm run seed
npm run dev  # Runs on http://localhost:3001

# In a new terminal, start the frontend
cd frontend
npm install
npm run dev  # Runs on http://localhost:5173
```

**Test Credentials:**
- Admin: `admin@yultimate.com` / `password123`
- Manager: `manager@yultimate.com` / `password123`
- Coach: `coach@yultimate.com` / `password123`

## ⚙️ Full Platform Setup (Python/FastAPI Backend)

For the complete platform with all features, follow these steps:

### Prerequisites

* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js v18+](https://nodejs.org/)
* [Docker](https://www.docker.com/products/docker-desktop/) (for PostgreSQL database)

---

### 1. Run the Database

The FastAPI backend uses PostgreSQL. The easiest way to run it is with Docker.

1.  **Start Docker:** Open Docker Desktop on your machine.
2.  **Run Postgres:** In your project's root directory, run:
    ```sh
    docker-compose up -d
    ```

### 2. Configure Environment

You must provide your secret keys for the application to work.

1.  **Copy the example:**
    ```sh
    cp .env.example .env
    ```
2.  **Edit the `.env` file:**
    Open the `.env` file and fill in the values. The `DATABASE_URL` should match the one in your `docker-compose.yml`.

    ```ini
    # Example .env file
    DATABASE_URL="postgresql://user:password@localhost:5432/yultimate_db"
    JWT_SECRET_KEY="YOUR_SUPER_SECRET_RANDOM_KEY"
    JWT_ALGORITHM="HS256"
    ```

### 3. Run the Backend (FastAPI)

1.  **Navigate to the backend:**
    ```sh
    cd backend
    ```
2.  **Create a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
    ```
3.  **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run database migrations:**
    ```sh
    alembic upgrade head
    ```
5.  **Start the backend server:**
    ```sh
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```
    Your backend is now running on `http://localhost:8000`.

### 4. Run the Frontend (React)

1.  **Open a new terminal window.**
2.  **Navigate to the frontend:**
    ```sh
    cd frontend
    ```
3.  **Install Node.js dependencies:**
    ```sh
    npm install
    ```
4.  **Update the API endpoint** (if needed):
    Edit `frontend/src/services/api.js` to point to:
    ```javascript
    baseURL: 'http://localhost:8000/api/v1',
    ```
5.  **Start the frontend server:**
    ```sh
    npm run dev
    ```
    Your frontend is now running on `http://localhost:5173`.

---

## 📚 API Documentation

### MVP Backend (Node.js)
- **Port:** 3001
- **Endpoints:** See [DEV-SETUP.md](DEV-SETUP.md) for full API documentation
- **Database:** SQLite (file-based, no Docker required)

### Full Platform Backend (FastAPI)
- **Port:** 8000
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Database:** PostgreSQL

## 🏗️ Architecture

### MVP Hackathon Stack (backend-node)
- **Backend:** Node.js + TypeScript + Express
- **Database:** SQLite via Prisma ORM
- **Authentication:** JWT tokens (24-hour expiry)
- **Frontend:** React + Vite + Tailwind CSS

### Full Platform Stack (backend)
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL via SQLAlchemy
- **Authentication:** JWT tokens
- **Frontend:** React + Vite + Tailwind CSS

## 📖 Documentation

- **[DEV-SETUP.md](DEV-SETUP.md)** - Complete setup guide for the MVP hackathon demo
- **API Docs** - Auto-generated Swagger/ReDoc documentation for both backends

## 🤝 Contributing

This is an active development project for Y-Ultimate. The MVP scaffold provides a working prototype for the hackathon, while the full platform is being developed in parallel.
