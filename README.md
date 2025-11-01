
# Y-Ultimate Management Platform

A unified web platform to manage Y-Ultimate's tournaments and coaching programs, built with FastAPI, React, and PostgreSQL.

## Project Overview

The Y-Ultimate Management Platform is designed to streamline the management of youth ultimate frisbee programs. It provides a central hub for a variety of users, including:

*   **Prospective members:** Can find information about the organization and its programs.
*   **Parents:** Can register their children for programs, track their progress, and view assessment results.
*   **Coaches:** Can manage their teams, track player attendance, and conduct assessments.
*   **Admins:** Can manage all aspects of the platform, including users, tournaments, and content.

The platform is designed to be a one-stop shop for all things Y-Ultimate, making it easier for everyone to stay organized and informed.

## Technology Stack

*   **Backend:** Python with FastAPI
*   **Frontend:** React
*   **Database:** PostgreSQL
*   **Containerization:** Docker

## Project Structure

The project is divided into two main components:

*   **`backend/`:** A Python-based backend powered by the FastAPI framework. This is responsible for handling all business logic, data storage, and API endpoints.
*   **`frontend/`:** A React-based frontend that provides the user interface for the application. It communicates with the backend via a RESTful API.

## Getting Started

### Prerequisites

*   [Docker](https://www.docker.com/products/docker-desktop/)

### Setup

1.  **Start the application:**
    ```sh
    docker-compose up -d --build
    ```
    *   Your backend will be running at `http://localhost:8000`.
    *   Your frontend will be running at `http://localhost:5173`.

2.  **Access the API documentation:**
    *   **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
    *   **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Contributing

We welcome contributions to the Y-Ultimate Management Platform! To contribute, please follow these steps:

1.  **Fork the repository.**
2.  **Create a new branch for your feature or bug fix.**
3.  **Make your changes.**

### Backend Development

The backend is a standard FastAPI application. To make changes:

1.  Navigate to the `backend/` directory.
2.  Make your desired code changes.
3.  The `docker-compose` setup uses `uvicorn` with `--reload`, so your changes will be automatically applied to the running container.

### Frontend Development

The frontend is a standard React application created with Vite. To make changes:

1.  Navigate to the `frontend/` directory.
2.  Make your desired code changes.
3.  The `docker-compose` setup uses the Vite development server, so your changes will be automatically reflected in your browser.

### Submitting Changes

1.  **Commit your changes with a clear and descriptive commit message.**
2.  **Push your changes to your forked repository.**
3.  **Create a pull request to the main repository.**

We will review your pull request as soon as possible. Thank you for your contributions!
