# Y-Ultimate Management Platform

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-react](https://img.shields.io/badge/Made%20with-React-20232a?logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![made-with-fastapi](https://img.shields.io/badge/Made%20with-FastAPI-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![made-with-postgresql](https://img.shields.io/badge/Made%20with-PostgreSQL-336791.svg?logo=postgresql)](https://www.postgresql.org/)

A single, centralized web platform to manage all of Y-Ultimate's operations, replacing scattered Google Sheets with a single source of truth.

This platform manages tournaments, team/player registrations, live scoring, and coaching modules (like Child Profiles and LSAS assessments).

## 🚀 The Core Problem & Solution

* **Problem:** Y-Ultimate's data is fragmented across many manual Google Sheets, leading to slow workflows, data integrity issues, and delayed reporting.
* **Solution:** A modern, monorepo web application with a **React (Vite) frontend** and a **FastAPI (Python) backend** powered by a **PostgreSQL** database. This provides a single, responsive, and reliable system for all users (Admins, Coaches, and Parents).

## 🗂️ Project Structure

This is a monorepo, meaning both the frontend and backend code live in the same repository.

* `/backend`: The FastAPI Python application. This folder contains the API, database models, and all business logic.
* `/frontend`: The React (Vite) application. This folder contains all UI components, pages, and frontend logic.
* `/docker-compose.yml`: A helper file to easily run the PostgreSQL database in a Docker container.

---

## ⚙️ Getting Started: Local Development

Follow these steps to run the complete application on your local machine.

### Prerequisites

* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js v18+](https://nodejs.org/)
* [Docker](https://www.docker.com/products/docker-desktop/) (for running the database)

---

### 1. Run the Database

The easiest way to run a PostgreSQL database is with Docker.

1.  **Start Docker:** Open Docker Desktop on your machine.
2.  **Run Postgres:** In your project's root directory, run:
    ```sh
    docker-compose up
    ```
    (You can add `-d` to run it in the background)

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
    This command creates all the tables in your database based on your SQLAlchemy models.
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
4.  **Start the frontend server:**
    ```sh
    npm run dev
    ```
    Your frontend is now running on `http://localhost:5173` (or the next available port).

---

## 📚 API Documentation

Once the backend server is running, you can view and interact with the complete, auto-generated API documentation:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)