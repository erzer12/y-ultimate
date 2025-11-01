"""
Seed script to populate the database with mock data for development and testing.

Usage:
    python scripts/seed_data.py
"""

import sys
import os
from pathlib import Path
from datetime import datetime, date, timedelta
import random

# Add parent directory to path to import app modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.models import (
    User, UserRole, Coach, ChildProfile, Gender,
    Session, Attendance, HomeVisit,
    LSASAssessment, AssessmentType,
    Tournament, TournamentStatus, Team, Match, PlayerRegistration
)
from app.core.security import get_password_hash


def create_tables():
    """Create all database tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created")


def seed_users(db):
    """Create sample users with different roles"""
    print("\nSeeding users...")
    
    users_data = [
        {"email": "admin@yultimate.org", "full_name": "Admin User", "role": UserRole.ADMIN, "is_admin": True},
        {"email": "manager@yultimate.org", "full_name": "Programme Manager", "role": UserRole.MANAGER},
        {"email": "coach1@yultimate.org", "full_name": "Sarah Johnson", "role": UserRole.COACH},
        {"email": "coach2@yultimate.org", "full_name": "Michael Brown", "role": UserRole.COACH},
        {"email": "coach3@yultimate.org", "full_name": "Emily Davis", "role": UserRole.COACH},
        {"email": "reporting@yultimate.org", "full_name": "Data Analyst", "role": UserRole.REPORTING},
        {"email": "coordinator@yultimate.org", "full_name": "Community Coordinator", "role": UserRole.COORDINATOR},
    ]
    
    users = []
    for user_data in users_data:
        user = User(
            email=user_data["email"],
            hashed_password=get_password_hash("password123"),
            full_name=user_data["full_name"],
            role=user_data["role"],
            is_admin=user_data.get("is_admin", False),
            is_active=True
        )
        db.add(user)
        users.append(user)
    
    db.commit()
    print(f"✓ Created {len(users)} users")
    return users


def seed_coaches(db, users):
    """Create coach profiles linked to coach users"""
    print("\nSeeding coaches...")
    
    coach_users = [u for u in users if u.role == UserRole.COACH]
    coaches = []
    
    for user in coach_users:
        coach = Coach(
            user_id=user.id,
            name=user.full_name,
            phone=f"+27 {random.randint(600000000, 699999999)}",
            email=user.email,
            total_session_hours=random.uniform(50, 200),
            total_travel_hours=random.uniform(10, 50),
            total_home_visits=random.randint(5, 25)
        )
        db.add(coach)
        coaches.append(coach)
    
    db.commit()
    print(f"✓ Created {len(coaches)} coaches")
    return coaches


def seed_children(db):
    """Create sample child profiles"""
    print("\nSeeding child profiles...")
    
    first_names = ["Thabo", "Lerato", "Sipho", "Nokuthula", "Mandla", "Zanele", "Bongani", "Precious",
                   "Dumisani", "Ayanda", "Siyabonga", "Nomsa", "Mpho", "Thandeka", "Jabu", "Lindiwe"]
    
    last_names = ["Nkosi", "Dlamini", "Khumalo", "Mthembu", "Zulu", "Ngwenya", "Sibiya", "Mahlangu"]
    
    schools = ["Hillside Primary", "Valley View School", "Riverside Academy", "Mountain High School"]
    communities = ["Alexandra", "Soweto", "Diepsloot", "Orange Farm"]
    
    children = []
    for i in range(50):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        child = ChildProfile(
            name=f"{first_name} {last_name}",
            date_of_birth=date.today() - timedelta(days=random.randint(2555, 5110)),
            gender=random.choice(list(Gender)),
            parent_name=f"Parent of {first_name}",
            parent_phone=f"+27 {random.randint(700000000, 799999999)}",
            school=random.choice(schools) if random.random() > 0.3 else None,
            community=random.choice(communities) if random.random() > 0.3 else None,
            enrolled_in_school_program=random.random() > 0.4,
            enrolled_in_community_program=random.random() > 0.6,
            is_active=random.random() > 0.1,
            enrollment_date=date.today() - timedelta(days=random.randint(30, 730))
        )
        db.add(child)
        children.append(child)
    
    db.commit()
    print(f"✓ Created {len(children)} child profiles")
    return children


def main():
    """Main seeding function"""
    print("=" * 60)
    print("Y-Ultimate Database Seeding Script")
    print("=" * 60)
    
    create_tables()
    db = SessionLocal()
    
    try:
        users = seed_users(db)
        coaches = seed_coaches(db, users)
        children = seed_children(db)
        
        print("\n" + "=" * 60)
        print("✓ Database seeding completed successfully!")
        print("=" * 60)
        print(f"\nCreated {len(users)} users, {len(coaches)} coaches, {len(children)} children")
        print("\nDefault Login: admin@yultimate.org / password123")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
