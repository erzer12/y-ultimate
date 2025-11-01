# Data Model Documentation

## Entity-Relationship Overview

The Y-Ultimate Management Platform uses a relational database with the following core entities:

## 📊 Core Entities

### 1. User Management
- **User**: System users with role-based access
  - Roles: Admin, Manager, Coach, Reporting, Coordinator
  - Authentication via JWT tokens

### 2. Coaching Programme
- **ChildProfile**: Central entity for child participants
- **Coach**: Coach information and workload tracking
- **Session**: Coaching sessions (school, community, tournament prep)
- **Attendance**: Session attendance tracking
- **HomeVisit**: Home visit records
- **LSASAssessment**: Life Skills Assessment System records

### 3. Tournament Management
- **Tournament**: Tournament events
- **Team**: Participating teams
- **Match**: Individual games
- **PlayerRegistration**: Tournament player registrations

## 🔗 Relationships

```
User (1) ──── (1) Coach
  │
  └──── (many) Tournament (owner)

ChildProfile (1) ──── (many) Attendance
  │
  ├──── (many) LSASAssessment
  ├──── (many) HomeVisit
  └──── (many) PlayerRegistration

Coach (1) ──── (many) Session
  │
  ├──── (many) Attendance (recorded by)
  └──── (many) HomeVisit

Session (1) ──── (many) Attendance

Tournament (1) ──── (many) Team
  │
  ├──── (many) Match
  └──── (many) PlayerRegistration

Team (1) ──── (many) PlayerRegistration
  │
  └──── (many) Match (as team1 or team2)
```

## 📋 Detailed Entity Schemas

### User
```python
- id: Integer (PK)
- email: String (Unique)
- hashed_password: String
- full_name: String
- role: Enum (admin, manager, coach, reporting, coordinator)
- is_active: Boolean
- is_admin: Boolean (legacy)
```

### ChildProfile
```python
- id: Integer (PK)
- name: String
- date_of_birth: Date
- gender: Enum (male, female, other, prefer_not_to_say)
- parent_name: String
- parent_phone: String
- parent_email: String
- address: Text
- school: String
- community: String
- enrolled_in_school_program: Boolean
- enrolled_in_community_program: Boolean
- is_active: Boolean
- enrollment_date: Date
- exit_date: Date
- exit_reason: Text
- transfer_history: Text (JSON)
- medical_notes: Text
- general_notes: Text
```

### Coach
```python
- id: Integer (PK)
- user_id: Integer (FK -> User, Unique)
- name: String
- phone: String
- email: String
- total_session_hours: Float
- total_travel_hours: Float
- total_home_visits: Integer
```

### Session
```python
- id: Integer (PK)
- title: String
- session_type: String (school, community, tournament_prep)
- location: String
- school: String
- community: String
- scheduled_start: DateTime
- scheduled_end: DateTime
- actual_start: DateTime
- actual_end: DateTime
- coach_id: Integer (FK -> Coach)
- duration_hours: Float
- travel_hours: Float
- is_active: Boolean
- is_completed: Boolean
- notes: Text
```

### Attendance
```python
- id: Integer (PK)
- session_id: Integer (FK -> Session)
- child_id: Integer (FK -> ChildProfile)
- coach_id: Integer (FK -> Coach)
- present: Boolean
- marked_at: DateTime
- notes: Text
```

### HomeVisit
```python
- id: Integer (PK)
- child_id: Integer (FK -> ChildProfile)
- coach_id: Integer (FK -> Coach)
- visit_date: Date
- visit_type: String (baseline, follow_up, emergency)
- purpose: Text
- observations: Text
- action_items: Text
```

### LSASAssessment
```python
- id: Integer (PK)
- child_id: Integer (FK -> ChildProfile)
- assessment_type: Enum (baseline, endline, follow_up, mid_term)
- assessment_date: Date
- overall_score: Float
- leadership_score: Float
- teamwork_score: Float
- communication_score: Float
- confidence_score: Float
- resilience_score: Float
- assessor_notes: Text
- strengths: Text
- areas_for_improvement: Text
- assessed_by: String
```

### Tournament
```python
- id: Integer (PK)
- name: String
- description: Text
- location: String
- venue: String
- start_date: Date
- end_date: Date
- registration_open_date: Date
- registration_close_date: Date
- max_teams: Integer
- tournament_format: String (round_robin, bracket, pool_play)
- age_division: String (U12, U15, U18, Open)
- status: Enum (draft, open_registration, registration_closed, in_progress, completed, cancelled)
- is_published: Boolean
- logo_url: String
- banner_url: String
- organizer_name: String
- organizer_email: String
- organizer_phone: String
- owner_id: Integer (FK -> User)
- rules: Text
- notes: Text
```

### Team
```python
- id: Integer (PK)
- name: String
- school: String
- community: String
- coach_name: String
- coach_contact: String
- tournament_id: Integer (FK -> Tournament)
- wins: Integer
- losses: Integer
- draws: Integer
- points_for: Integer
- points_against: Integer
- spirit_score_total: Integer
- is_active: Boolean
- notes: Text
```

### Match
```python
- id: Integer (PK)
- tournament_id: Integer (FK -> Tournament)
- match_number: Integer
- round: String (pool_play, quarterfinal, semifinal, final)
- pool: String
- team1_id: Integer (FK -> Team)
- team2_id: Integer (FK -> Team)
- scheduled_time: DateTime
- field: String
- team1_score: Integer
- team2_score: Integer
- winner_id: Integer (FK -> Team)
- team1_spirit_score: Float
- team2_spirit_score: Float
- is_completed: Boolean
- is_forfeit: Boolean
```

### PlayerRegistration
```python
- id: Integer (PK)
- tournament_id: Integer (FK -> Tournament)
- child_id: Integer (FK -> ChildProfile)
- team_id: Integer (FK -> Team)
- registration_date: DateTime
- jersey_number: Integer
- jersey_size: String
- is_approved: Boolean
- approval_date: DateTime
- approved_by: Integer (FK -> User)
- emergency_contact_name: String
- emergency_contact_phone: String
- dietary_restrictions: Text
- medical_conditions: Text
- notes: Text
```

## 📈 Key Features

### 1. Dual Programme Support
ChildProfile supports enrollment in both school and community programmes simultaneously through boolean flags.

### 2. Transfer History
Transfer history is stored as JSON in ChildProfile.transfer_history, allowing complete tracking of a child's movement between schools/communities.

### 3. Workload Tracking
Coach model automatically tracks session hours, travel hours, and home visits for workload management.

### 4. Progress Tracking
LSASAssessment allows tracking of skill development over time with multiple assessment types (baseline, mid-term, endline, follow-up).

### 5. Live Scoring
Match model includes automatic winner determination and team statistics updates when matches are completed.

### 6. Spirit Scores
Ultimate Frisbee's spirit of the game is tracked at the match level with team1_spirit_score and team2_spirit_score fields.

## 🔍 Indexes

Key indexes for performance:
- ChildProfile: name, school, community, is_active
- Session: coach_id, session_type, is_active
- Attendance: session_id, child_id, coach_id
- Match: tournament_id, team1_id, team2_id
- User: email (unique)
- Coach: user_id (unique)

## 🔒 Constraints

- Users must have unique emails
- Coaches must have unique user_id (one coach per user)
- All foreign keys have proper referential integrity
- Dates are validated (end_date > start_date)
- Scores are non-negative integers/floats

---

For database migrations and schema changes, see [SETUP.md](SETUP.md#database-setup).
