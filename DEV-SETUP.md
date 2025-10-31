# Y-Ultimate MVP Development Setup

This guide explains how to run the Y-Ultimate MVP locally for the hackathon demo.

## Prerequisites

- **Node.js** v18+ (for backend-node)
- **npm** (comes with Node.js)

## Quick Start

### 1. Backend Setup (Node.js + TypeScript + Express)

#### Install Dependencies

```bash
cd backend-node
npm install
```

#### Configure Environment Variables

The `.env` file already contains default development values:

```bash
DATABASE_URL="file:./dev.db"
JWT_SECRET="dev-secret-change-in-production"
PORT=3001
```

You can modify these if needed, but the defaults work out of the box.

#### Run Database Migrations

```bash
npm run prisma:migrate
```

This creates the SQLite database and all required tables.

#### Seed the Database

```bash
npm run seed
```

This creates:
- **3 test users**: admin, manager, and coach
- **2 sites**: Downtown Community Center, Westside Recreation Center
- **8 sample children** across both sites
- **2 sessions** with sample attendance data

**Test Credentials:**
- Admin: `admin@yultimate.com` / `password123`
- Manager: `manager@yultimate.com` / `password123`
- Coach: `coach@yultimate.com` / `password123`

#### Start the Backend Server

```bash
npm run dev
```

The backend will start on **http://localhost:3001**

You can verify it's running:
```bash
curl http://localhost:3001/health
```

### 2. Frontend Setup (React + Vite)

The frontend is currently the existing React application. To set it up:

```bash
cd frontend
npm install
npm run dev
```

The frontend will start on **http://localhost:5173**

## API Endpoints

### Authentication
- **POST** `/api/auth/login` - Login with email/password, returns JWT token

### Children
- **GET** `/api/children` - List all children (requires auth)
- **POST** `/api/children` - Create a new child (requires manager/admin role)
- **POST** `/api/import/children` - Import children from CSV (requires admin role)

### Sessions
- **GET** `/api/sessions?date=YYYY-MM-DD` - List sessions, optionally filter by date
- **POST** `/api/sessions` - Create a new session (requires manager/admin role)
- **POST** `/api/sessions/:id/attendance` - Bulk save attendance for a session

### Reports
- **GET** `/api/reports/attendance?from=YYYY-MM-DD&to=YYYY-MM-DD&site=ID` - Export attendance report as CSV

## Sample CSV Import Template

See `backend-node/sample-children-import.csv` for the format:

```csv
firstName,lastName,dateOfBirth,siteId
John,Doe,2010-05-15,1
Jane,Smith,2011-08-22,1
Michael,Johnson,2009-12-10,2
Emily,Brown,2010-03-05,2
```

**Required fields:** `firstName`, `lastName`, `siteId`
**Optional field:** `dateOfBirth` (format: YYYY-MM-DD)

## Testing the Demo Flow

### 1. Login as Coach
```bash
curl -X POST http://localhost:3001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"coach@yultimate.com","password":"password123"}'
```

Save the returned token for subsequent requests.

### 2. View Sessions
```bash
curl http://localhost:3001/api/sessions \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### 3. Mark Attendance
```bash
curl -X POST http://localhost:3001/api/sessions/1/attendance \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "attendance": [
      {"childId": 1, "present": true},
      {"childId": 2, "present": true},
      {"childId": 3, "present": false}
    ]
  }'
```

### 4. Login as Manager and Create a Child
```bash
# Login as manager
TOKEN=$(curl -s -X POST http://localhost:3001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"manager@yultimate.com","password":"password123"}' | jq -r '.token')

# Create a child
curl -X POST http://localhost:3001/api/children \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "New",
    "lastName": "Child",
    "siteId": 1
  }'
```

### 5. Login as Admin and Import Children
```bash
# Login as admin
TOKEN=$(curl -s -X POST http://localhost:3001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@yultimate.com","password":"password123"}' | jq -r '.token')

# Import children from CSV
curl -X POST http://localhost:3001/api/import/children \
  -H "Authorization: Bearer $TOKEN" \
  -F "file=@backend-node/sample-children-import.csv"
```

### 6. Export Attendance Report
```bash
curl "http://localhost:3001/api/reports/attendance?from=2025-10-01&to=2025-11-30&site=1" \
  -H "Authorization: Bearer $TOKEN" \
  -o attendance-report.csv
```

## Development Commands

### Backend
- `npm run dev` - Start development server with hot reload
- `npm run build` - Build TypeScript to JavaScript
- `npm start` - Run built JavaScript
- `npm run lint` - Run ESLint
- `npm run lint:fix` - Auto-fix linting issues
- `npm test` - Run tests
- `npm run seed` - Seed database with sample data
- `npm run prisma:generate` - Generate Prisma client
- `npm run prisma:migrate` - Run database migrations
- `npm run prisma:studio` - Open Prisma Studio (GUI for database)

### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## Database Management

The SQLite database is stored in `backend-node/prisma/dev.db`.

To reset the database:
```bash
cd backend-node
rm prisma/dev.db
npm run prisma:migrate
npm run seed
```

To view/edit data with Prisma Studio:
```bash
cd backend-node
npm run prisma:studio
```

This opens a GUI at **http://localhost:5555**

## Docker Support

Build and run the backend with Docker:

```bash
cd backend-node
docker build -t y-ultimate-backend .
docker run -p 3001:3001 y-ultimate-backend
```

## Troubleshooting

### Port Already in Use
If port 3001 is already in use, change the `PORT` in `backend-node/.env`:
```
PORT=3002
```

### Database Connection Issues
Make sure you're in the `backend-node` directory when running Prisma commands. The database path is relative to this directory.

### Authentication Errors
Make sure to include the JWT token in the Authorization header:
```
Authorization: Bearer YOUR_TOKEN_HERE
```

## Architecture

- **Backend**: Node.js + TypeScript + Express
- **Database**: SQLite via Prisma ORM
- **Authentication**: JWT tokens (24-hour expiry)
- **Frontend**: React + Vite + Tailwind CSS

## Notes for Hackathon Demo

- This is a **minimal prototype** for demo purposes
- Uses SQLite for simplicity (production would use PostgreSQL)
- JWT secret should be changed in production
- No offline support or OAuth in this version
- Basic role-based access control (admin, manager, coach)
