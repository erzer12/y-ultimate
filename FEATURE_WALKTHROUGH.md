# Feature Walkthrough - Y-Ultimate Management Platform

This guide walks through the key features of the Y-Ultimate Management Platform for each user role.

## 🎯 Table of Contents
- [Getting Started](#getting-started)
- [User Roles Overview](#user-roles-overview)
- [Authentication](#authentication)
- [Dashboard](#dashboard)
- [Coaching Programme Features](#coaching-programme-features)
- [Tournament Management](#tournament-management)
- [Reporting & Analytics](#reporting--analytics)

---

## Getting Started

### Accessing the Platform

1. Navigate to **http://localhost:5173** (or your deployed URL)
2. You'll see the animated hero section introducing Y-Ultimate
3. Click "Get Started" or navigate to Login

### First Time Setup

1. Login with default admin credentials:
   - **Email**: `admin@yultimate.org`
   - **Password**: `password123`
2. The dashboard loads with an overview of programme statistics

---

## User Roles Overview

### 1. Programme Director / Admin
**Full Access** - Can manage all aspects of the platform

**Capabilities:**
- Create and manage users
- Assign roles and permissions
- View all data across programmes and tournaments
- Generate comprehensive reports
- Manage system settings

### 2. Programme Manager
**Management Access** - Oversees programmes and teams

**Capabilities:**
- Manage child profiles
- Assign coaches to sessions
- View and generate reports
- Approve registrations
- Track coach workloads

### 3. Coach / Facilitator
**Coach Access** - Day-to-day session management

**Capabilities:**
- Mark attendance for sessions
- Record home visits
- Conduct LSAS assessments
- View assigned children and sessions
- Update session notes

### 4. Reporting / Data Team
**Sub-Admin** - Data analysis and validation

**Capabilities:**
- View all data (read-only for most)
- Generate reports and analytics
- Export data to CSV/Excel
- Validate data integrity

### 5. Community / School Coordinator
**Site-Level** - Local programme oversight

**Capabilities:**
- View children at their site
- Monitor attendance at their location
- View session schedules
- Track local programme progress

---

## Authentication

### Login Flow

1. **Navigate to Login**: Click "Profile" or "Login" button
2. **Enter Credentials**: Email and password
3. **JWT Token**: System generates a secure JWT token
4. **Dashboard Redirect**: Automatically redirects to role-appropriate dashboard

### User Sessions

- Sessions are maintained via JWT tokens
- Tokens expire after 30 minutes of inactivity
- Automatic re-login required after expiration

---

## Dashboard

### Hero Section
![Hero Animation]
- **Parallax scrolling** with animated frisbee disc
- **Dynamic layers** moving at different speeds
- **Call-to-action buttons** for key features

### Statistics Overview

**Four Key Metrics:**
1. **Active Children** - Total enrolled children with monthly growth
2. **Total Sessions** - Completed sessions with weekly count
3. **Tournaments** - Upcoming and past tournaments
4. **Attendance Rate** - Overall attendance with trend

### Quick Actions

**Fast access to common tasks:**
- Mark Attendance
- Add New Child
- Create Session
- Schedule Home Visit

### Recent Activity Feed

**Real-time updates showing:**
- Recently completed sessions
- New assessments
- Tournament registrations
- System notifications

---

## Coaching Programme Features

### 1. Child Profile Management

#### Creating a Child Profile

**Navigation:** Dashboard → Children → Add New Child

**Required Information:**
- Full Name
- Date of Birth
- Gender
- Parent/Guardian Name
- Parent Contact (Phone & Email)
- Address

**Programme Enrollment:**
- ☑️ School Programme
- ☑️ Community Programme
- Can be enrolled in both simultaneously

**API Endpoint:**
```
POST /api/v1/profiles/
```

#### Viewing Child Profiles

**List View:**
- Searchable by name or parent
- Filter by school, community, or active status
- Pagination support (100 per page)

**Detail View:**
- Complete profile information
- Attendance statistics
- Assessment history with progress chart
- Home visit records
- Transfer history

**API Endpoint:**
```
GET /api/v1/profiles/
GET /api/v1/profiles/{profile_id}
GET /api/v1/profiles/{profile_id}/stats
```

#### Transferring Children

**Process:**
1. Select child profile
2. Click "Transfer"
3. Enter:
   - From Location (current school/community)
   - To Location (new school/community)
   - Transfer Date
   - Reason (optional)
4. System records in transfer history (JSON)

**API Endpoint:**
```
POST /api/v1/profiles/{profile_id}/transfer
```

### 2. Session Management

#### Creating a Session

**Navigation:** Dashboard → Sessions → Create New

**Session Types:**
- **School**: Regular school-based training
- **Community**: Community center sessions
- **Tournament Prep**: Pre-tournament training

**Required Fields:**
- Title
- Session Type
- Location (field/venue)
- School or Community
- Scheduled Start/End Time
- Assigned Coach
- Travel Hours (for workload tracking)

**API Endpoint:**
```
POST /api/v1/sessions/
```

#### Active Session Tracking

**Starting a Session:**
1. Navigate to scheduled session
2. Click "Start Session"
3. System records actual start time
4. Session marked as `is_active: true`

**Ending a Session:**
1. Click "End Session"
2. System records actual end time
3. Calculates actual duration
4. Updates coach's total hours
5. Session marked as `is_completed: true`

**API Endpoints:**
```
POST /api/v1/sessions/{session_id}/start
POST /api/v1/sessions/{session_id}/end
```

### 3. Attendance Tracking

#### Marking Attendance (Individual)

**Process:**
1. Navigate to active session
2. View list of enrolled children
3. Mark each child as Present/Absent
4. Add optional notes
5. Save attendance record

**API Endpoint:**
```
POST /api/v1/attendance/
```

#### Bulk Attendance Marking

**For entire session at once:**

**Process:**
1. Select session
2. Click "Mark All Attendance"
3. System shows all expected children
4. Quick toggle Present/Absent for each
5. Bulk save all records

**API Endpoint:**
```
POST /api/v1/attendance/bulk
Body: {
  "session_id": 123,
  "coach_id": 5,
  "attendance_records": [
    {"child_id": 1, "present": true, "notes": "Great participation"},
    {"child_id": 2, "present": false, "notes": "Sick"}
  ]
}
```

#### Viewing Attendance Reports

**Filters available:**
- By Child
- By Session
- By Coach
- By Date Range

**Statistics shown:**
- Total sessions for child
- Sessions attended
- Attendance rate (percentage)
- Trend over time

### 4. Home Visit Tracking

#### Recording a Home Visit

**Navigation:** Child Profile → Record Home Visit

**Visit Types:**
- **Baseline**: Initial home assessment
- **Follow-up**: Regular check-in
- **Emergency**: Urgent situation

**Required Information:**
- Visit Date
- Visit Type
- Purpose
- Observations
- Action Items

**API Endpoint:**
```
POST /api/v1/home-visits/
```

#### Viewing Visit History

**Per Child:**
- Chronological list of all visits
- Filter by visit type
- View notes and action items
- Track completion of action items

### 5. LSAS Assessments

#### Conducting an Assessment

**Navigation:** Child Profile → Conduct Assessment

**Assessment Types:**
- **Baseline**: Initial skill evaluation (at enrollment)
- **Mid-term**: Progress check (quarterly)
- **Endline**: Final evaluation (annually)
- **Follow-up**: Post-programme check

**Scoring Categories (0-100):**
1. Leadership Score
2. Teamwork Score
3. Communication Score
4. Confidence Score
5. Resilience Score
6. Overall Score (average)

**Additional Fields:**
- Assessor Notes
- Strengths
- Areas for Improvement
- Assessed By (coach name)

**API Endpoint:**
```
POST /api/v1/assessments/
```

#### Progress Tracking

**Child Progress View:**
- Line chart showing score improvements
- Comparison between baseline and latest
- Individual skill breakdowns
- Trend analysis

**Calculations:**
- Overall Improvement = Latest Overall - Baseline Overall
- Skill-specific improvements
- Time between assessments

**API Endpoint:**
```
GET /api/v1/assessments/child/{child_id}/progress
```

### 6. Coach Workload Tracking

**Automatically tracked:**
- Total Session Hours (from completed sessions)
- Total Travel Hours (from session records)
- Total Home Visits (count)

**Updated when:**
- Session is marked complete
- Home visit is recorded

**Viewing Workload:**
- Coach list shows totals
- Individual coach profile with detailed breakdown
- Filter by date range

---

## Tournament Management

### 1. Creating a Tournament

**Navigation:** Dashboard → Tournaments → Create New

**Basic Information:**
- Tournament Name
- Description
- Location & Venue
- Start Date & End Date

**Registration Settings:**
- Registration Open Date
- Registration Close Date
- Maximum Teams

**Tournament Configuration:**
- Format: Round Robin, Bracket, Pool Play
- Age Division: U12, U15, U18, Open
- Rules and Notes

**Status Options:**
- Draft
- Open Registration
- Registration Closed
- In Progress
- Completed
- Cancelled

**API Endpoint:**
```
POST /api/v1/tournaments/
```

### 2. Team Registration

#### Creating a Team

**Required Information:**
- Team Name
- School or Community
- Coach Name
- Coach Contact

**Linked to:**
- Tournament ID

**API Endpoint:**
```
POST /api/v1/teams/
```

#### Player Registration

**Process:**
1. Tournament administrator opens registration
2. Players/Parents submit registration:
   - Child Profile (linked)
   - Team Assignment
   - Jersey Number & Size
   - Emergency Contact
   - Medical Information
   - Dietary Restrictions

**Approval Workflow:**
1. Registration submitted (`is_approved: false`)
2. Manager reviews registration
3. Approval or rejection
4. Player assigned to team roster

**API Endpoints:**
```
POST /api/v1/registrations/
POST /api/v1/registrations/{id}/approve
```

### 3. Match Scheduling

#### Creating Matches

**Match Information:**
- Match Number
- Round (Pool Play, Quarterfinal, etc.)
- Pool (if applicable)
- Team 1 vs Team 2
- Scheduled Time
- Field Assignment

**API Endpoint:**
```
POST /api/v1/matches/
```

### 4. Live Scoring

#### Recording Match Scores

**During/After Match:**
1. Navigate to match
2. Enter scores:
   - Team 1 Score
   - Team 2 Score
3. Enter Spirit Scores:
   - Team 1 Spirit Score (0-20)
   - Team 2 Spirit Score (0-20)
4. Mark match as completed

**Automatic Updates:**
- Winner determined
- Team statistics updated:
  - Wins/Losses/Draws
  - Points For/Against
  - Spirit Score Total
- Leaderboard automatically recalculated

**API Endpoint:**
```
PUT /api/v1/matches/{match_id}/score
```

### 5. Leaderboards & Standings

**Calculated Automatically:**

**Team Rankings by:**
1. Wins (primary)
2. Point Differential (tiebreaker)
3. Spirit Score (ultimate tiebreaker)

**Statistics Shown:**
- Wins / Losses / Draws
- Points For / Against
- Win Percentage
- Average Spirit Score

**API Endpoint:**
```
GET /api/v1/tournaments/{tournament_id}/stats
GET /api/v1/teams/{team_id}/stats
```

---

## Reporting & Analytics

### Dashboard Analytics

**Programme-wide Metrics:**
- Total Children Enrolled
- Active vs Inactive
- Attendance Trends
- Assessment Score Averages
- Coach Workload Summary

### Custom Reports

**Available Filters:**
- Date Range
- School/Community
- Gender
- Age Group
- Programme Type

**Report Types:**
1. **Participation Report**
   - Enrollment numbers
   - Gender breakdown
   - Retention rates

2. **Attendance Report**
   - Session-level attendance
   - Child-level attendance rates
   - Trends over time

3. **Assessment Report**
   - Average scores by category
   - Improvement tracking
   - Skill development trends

4. **Coach Report**
   - Session hours by coach
   - Home visits completed
   - Children per coach

5. **Tournament Report**
   - Participation numbers
   - Match results
   - Spirit scores

### Data Export

**Formats:**
- CSV (for spreadsheets)
- Excel (formatted reports)
- JSON (for integrations)

**Export Options:**
- Single entity (e.g., one child's data)
- Filtered list (e.g., all children at a school)
- Complete dataset (admin only)

---

## Mobile Experience

### Responsive Design

**The platform is fully responsive:**
- Mobile-first navigation menu
- Touch-friendly buttons and forms
- Optimized layouts for tablets
- Quick actions accessible on mobile

### Key Mobile Features

**Coaches can:**
- Mark attendance on-the-go
- Record home visit notes
- View session schedules
- Check child profiles

**Coordinators can:**
- Monitor site-specific data
- View real-time attendance
- Access contact information

---

## Tips & Best Practices

### For Coaches

1. **Start sessions on time** - Use "Start Session" button
2. **Mark attendance during session** - Real-time tracking
3. **Complete assessments quarterly** - Track progress consistently
4. **Record home visits promptly** - Don't lose details

### For Managers

1. **Review attendance reports weekly** - Identify at-risk children
2. **Monitor coach workloads** - Balance session assignments
3. **Generate monthly reports** - Track programme impact
4. **Approve registrations quickly** - Keep tournaments on schedule

### For Coordinators

1. **Communicate with coaches** - Ensure accurate data entry
2. **Monitor local participation** - Address drops early
3. **Share success stories** - Report to community stakeholders

---

## Troubleshooting

### Common Issues

**Can't see children/sessions:**
- Verify your role permissions
- Check site/location filters
- Contact administrator

**Attendance not saving:**
- Ensure session is active
- Check internet connection
- Verify child is enrolled

**Assessment scores not calculating:**
- Ensure all required fields are filled
- Check score ranges (0-100)
- Refresh the page

---

## Support & Feedback

For technical support or feature requests:
- GitHub Issues: https://github.com/erzer12/y-ultimate/issues
- Documentation: See SETUP.md and CONTRIBUTING.md

---

**Thank you for using Y-Ultimate Management Platform!** 🏐
