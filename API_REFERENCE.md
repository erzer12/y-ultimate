# API Reference - Y-Ultimate Management Platform

Quick reference guide for all API endpoints. For interactive documentation, visit: **http://localhost:8000/docs**

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication

All endpoints (except login) require JWT authentication via Bearer token in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

---

## 🔐 Authentication Endpoints

### Login
```http
POST /api/v1/auth/login
Content-Type: application/x-www-form-urlencoded

username=admin@yultimate.org&password=password123
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

---

## 👥 Child Profiles

### List Children
```http
GET /api/v1/profiles/?skip=0&limit=100&is_active=true&school=Hillside
```

### Get Child Profile
```http
GET /api/v1/profiles/{profile_id}
```

### Get Child with Statistics
```http
GET /api/v1/profiles/{profile_id}/stats
```

**Response includes:**
- Total sessions
- Sessions attended
- Attendance rate
- Latest assessment date & score

### Create Child Profile
```http
POST /api/v1/profiles/
Content-Type: application/json

{
  "name": "John Doe",
  "date_of_birth": "2010-05-15",
  "gender": "male",
  "parent_name": "Jane Doe",
  "parent_phone": "+27 712345678",
  "school": "Hillside Primary",
  "enrolled_in_school_program": true,
  "enrolled_in_community_program": false
}
```

### Update Child Profile
```http
PUT /api/v1/profiles/{profile_id}
Content-Type: application/json

{
  "school": "New School Name",
  "is_active": true
}
```

### Transfer Child
```http
POST /api/v1/profiles/{profile_id}/transfer
Content-Type: application/json

{
  "child_id": 1,
  "from_location": "Hillside Primary",
  "to_location": "Valley View School",
  "transfer_date": "2024-01-15",
  "reason": "Family relocation"
}
```

### Delete (Soft Delete) Child Profile
```http
DELETE /api/v1/profiles/{profile_id}
```

---

## 👨‍🏫 Coaches

### List Coaches
```http
GET /api/v1/coaches/?skip=0&limit=100
```

### Get Coach
```http
GET /api/v1/coaches/{coach_id}
```

### Create Coach
```http
POST /api/v1/coaches/
Content-Type: application/json

{
  "user_id": 3,
  "name": "Sarah Johnson",
  "phone": "+27 723456789",
  "email": "sarah@yultimate.org"
}
```

### Update Coach
```http
PUT /api/v1/coaches/{coach_id}
Content-Type: application/json

{
  "total_session_hours": 120.5,
  "total_travel_hours": 25.0,
  "total_home_visits": 15
}
```

---

## 📅 Sessions

### List Sessions
```http
GET /api/v1/sessions/?is_active=true&coach_id=5&session_type=school
```

**Query Parameters:**
- `is_active`: Filter by active status
- `is_completed`: Filter by completion status
- `coach_id`: Filter by coach
- `session_type`: school, community, tournament_prep

### Get Session
```http
GET /api/v1/sessions/{session_id}
```

### Get Session with Attendance
```http
GET /api/v1/sessions/{session_id}/attendance
```

**Response includes:**
- All session details
- `attendance_count`: Total children marked
- `children_present`: Number present

### Create Session
```http
POST /api/v1/sessions/
Content-Type: application/json

{
  "title": "Weekly Training Session",
  "session_type": "school",
  "location": "Hillside Sports Ground",
  "school": "Hillside Primary",
  "scheduled_start": "2024-02-01T14:00:00",
  "scheduled_end": "2024-02-01T16:00:00",
  "coach_id": 5,
  "travel_hours": 0.5
}
```

### Update Session
```http
PUT /api/v1/sessions/{session_id}
Content-Type: application/json

{
  "is_active": false,
  "is_completed": true,
  "notes": "Great session, high participation"
}
```

### Start Session
```http
POST /api/v1/sessions/{session_id}/start
```

### End Session
```http
POST /api/v1/sessions/{session_id}/end
```

---

## ✅ Attendance

### List Attendance Records
```http
GET /api/v1/attendance/?session_id=10&child_id=5
```

### Get Attendance Record
```http
GET /api/v1/attendance/{attendance_id}
```

### Create Attendance Record
```http
POST /api/v1/attendance/
Content-Type: application/json

{
  "session_id": 10,
  "child_id": 5,
  "coach_id": 3,
  "present": true,
  "notes": "Active participation"
}
```

### Bulk Create Attendance
```http
POST /api/v1/attendance/bulk
Content-Type: application/json

{
  "session_id": 10,
  "coach_id": 3,
  "attendance_records": [
    {"child_id": 1, "present": true, "notes": "Great effort"},
    {"child_id": 2, "present": false, "notes": "Absent - sick"},
    {"child_id": 3, "present": true, "notes": ""}
  ]
}
```

### Update Attendance
```http
PUT /api/v1/attendance/{attendance_id}
Content-Type: application/json

{
  "present": false,
  "notes": "Left early due to emergency"
}
```

---

## 🏠 Home Visits

### List Home Visits
```http
GET /api/v1/home-visits/?child_id=5&coach_id=3&visit_type=baseline
```

### Get Home Visit
```http
GET /api/v1/home-visits/{visit_id}
```

### Create Home Visit
```http
POST /api/v1/home-visits/
Content-Type: application/json

{
  "child_id": 5,
  "coach_id": 3,
  "visit_date": "2024-02-01",
  "visit_type": "baseline",
  "purpose": "Initial family assessment",
  "observations": "Supportive home environment",
  "action_items": "Follow up on school supplies"
}
```

### Update Home Visit
```http
PUT /api/v1/home-visits/{visit_id}
Content-Type: application/json

{
  "observations": "Updated observations after follow-up",
  "action_items": "Completed - supplies provided"
}
```

---

## 📊 LSAS Assessments

### List Assessments
```http
GET /api/v1/assessments/?child_id=5&assessment_type=baseline
```

### Get Assessment
```http
GET /api/v1/assessments/{assessment_id}
```

### Get Child Assessment Progress
```http
GET /api/v1/assessments/child/{child_id}/progress
```

**Response includes:**
- All assessments chronologically
- Progress calculations (improvements between baseline and latest)
- Individual skill improvements

### Create Assessment
```http
POST /api/v1/assessments/
Content-Type: application/json

{
  "child_id": 5,
  "assessment_type": "baseline",
  "assessment_date": "2024-02-01",
  "overall_score": 65.5,
  "leadership_score": 70.0,
  "teamwork_score": 75.0,
  "communication_score": 60.0,
  "confidence_score": 55.0,
  "resilience_score": 67.0,
  "assessor_notes": "Shows good potential",
  "strengths": "Great teamwork skills",
  "areas_for_improvement": "Confidence needs development",
  "assessed_by": "Coach Sarah"
}
```

### Update Assessment
```http
PUT /api/v1/assessments/{assessment_id}
Content-Type: application/json

{
  "overall_score": 75.0,
  "assessor_notes": "Significant improvement observed"
}
```

---

## 🏆 Tournaments

### List Tournaments
```http
GET /api/v1/tournaments/?status=open_registration&is_published=true
```

### Get Tournament
```http
GET /api/v1/tournaments/{tournament_id}
```

### Get Tournament with Statistics
```http
GET /api/v1/tournaments/{tournament_id}/stats
```

**Response includes:**
- Tournament details
- Total teams
- Total matches
- Completed matches
- Total registrations
- Approved registrations

### Create Tournament
```http
POST /api/v1/tournaments/
Content-Type: application/json

{
  "name": "Spring Ultimate Cup 2024",
  "description": "Annual youth tournament",
  "location": "Johannesburg",
  "venue": "Wanderers Stadium",
  "start_date": "2024-03-15",
  "end_date": "2024-03-17",
  "registration_open_date": "2024-02-01",
  "registration_close_date": "2024-03-10",
  "max_teams": 16,
  "tournament_format": "pool_play",
  "age_division": "U15",
  "owner_id": 1
}
```

### Update Tournament
```http
PUT /api/v1/tournaments/{tournament_id}
Content-Type: application/json

{
  "status": "in_progress",
  "is_published": true
}
```

---

## 👥 Teams

### List Teams
```http
GET /api/v1/teams/?tournament_id=1&is_active=true
```

### Get Team
```http
GET /api/v1/teams/{team_id}
```

### Get Team with Statistics
```http
GET /api/v1/teams/{team_id}/stats
```

**Response includes:**
- Team details
- Total matches played
- Win percentage
- Average spirit score
- Point differential

### Create Team
```http
POST /api/v1/teams/
Content-Type: application/json

{
  "name": "Phoenix Rising",
  "school": "Hillside Primary",
  "community": "Alexandra",
  "coach_name": "Coach Mike",
  "coach_contact": "+27 723456789",
  "tournament_id": 1
}
```

### Update Team
```http
PUT /api/v1/teams/{team_id}
Content-Type: application/json

{
  "wins": 5,
  "losses": 2,
  "points_for": 85,
  "points_against": 60
}
```

---

## 🎯 Matches

### List Matches
```http
GET /api/v1/matches/?tournament_id=1&is_completed=false&round=semifinal
```

### Get Match with Team Names
```http
GET /api/v1/matches/{match_id}
```

**Response includes:**
- Match details
- `team1_name`, `team2_name`, `winner_name`

### Create Match
```http
POST /api/v1/matches/
Content-Type: application/json

{
  "tournament_id": 1,
  "match_number": 1,
  "round": "pool_play",
  "pool": "Pool A",
  "team1_id": 5,
  "team2_id": 8,
  "scheduled_time": "2024-03-15T10:00:00",
  "field": "Field 1"
}
```

### Update Match Score (Live Scoring)
```http
PUT /api/v1/matches/{match_id}/score
Content-Type: application/json

{
  "team1_score": 15,
  "team2_score": 12,
  "team1_spirit_score": 18.5,
  "team2_spirit_score": 19.0,
  "is_completed": true
}
```

**Note:** When `is_completed: true`, team statistics are automatically updated.

---

## 📝 Player Registrations

### List Registrations
```http
GET /api/v1/registrations/?tournament_id=1&is_approved=false
```

### Get Registration
```http
GET /api/v1/registrations/{registration_id}
```

### Create Registration
```http
POST /api/v1/registrations/
Content-Type: application/json

{
  "tournament_id": 1,
  "child_id": 5,
  "team_id": 3,
  "jersey_number": 7,
  "jersey_size": "M",
  "emergency_contact_name": "Jane Doe",
  "emergency_contact_phone": "+27 712345678",
  "dietary_restrictions": "Vegetarian",
  "medical_conditions": "Asthma - has inhaler"
}
```

### Approve/Reject Registration
```http
POST /api/v1/registrations/{registration_id}/approve
Content-Type: application/json

{
  "is_approved": true,
  "approved_by": 1
}
```

### Update Registration
```http
PUT /api/v1/registrations/{registration_id}
Content-Type: application/json

{
  "team_id": 5,
  "jersey_number": 10
}
```

---

## 📄 Response Formats

### Success Response
```json
{
  "id": 1,
  "name": "John Doe",
  "created_at": "2024-01-15T10:30:00",
  ...
}
```

### Error Response
```json
{
  "detail": "Error message here"
}
```

### Common HTTP Status Codes
- `200` - OK (successful GET, PUT)
- `201` - Created (successful POST)
- `204` - No Content (successful DELETE)
- `400` - Bad Request (validation error)
- `401` - Unauthorized (missing/invalid token)
- `403` - Forbidden (insufficient permissions)
- `404` - Not Found
- `500` - Internal Server Error

---

## 🔧 Pagination

For list endpoints:
```http
GET /api/v1/profiles/?skip=0&limit=100
```

**Parameters:**
- `skip`: Number of records to skip (default: 0)
- `limit`: Max records to return (default: 100, max: 100)

---

## 🔍 Filtering

Most list endpoints support filtering via query parameters:

```http
# Filter children by school and active status
GET /api/v1/profiles/?school=Hillside&is_active=true

# Filter sessions by coach and type
GET /api/v1/sessions/?coach_id=5&session_type=school

# Filter matches by tournament and completion
GET /api/v1/matches/?tournament_id=1&is_completed=true
```

---

## 📊 Statistics Endpoints

Special endpoints that return aggregated data:

- `/api/v1/profiles/{id}/stats` - Child statistics
- `/api/v1/sessions/{id}/attendance` - Session attendance stats
- `/api/v1/assessments/child/{id}/progress` - Assessment progress
- `/api/v1/tournaments/{id}/stats` - Tournament statistics
- `/api/v1/teams/{id}/stats` - Team statistics

---

## 🛠️ Testing with curl

### Login Example
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin@yultimate.org&password=password123"
```

### Authenticated Request Example
```bash
TOKEN="your_jwt_token_here"

curl -X GET http://localhost:8000/api/v1/profiles/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## 📖 Interactive Documentation

For full interactive API documentation with try-it-out functionality:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

For more information, see:
- [Setup Guide](SETUP.md)
- [Feature Walkthrough](FEATURE_WALKTHROUGH.md)
- [Data Model](DATA_MODEL.md)
