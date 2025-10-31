"""
SQLAlchemy Declarative Base

This file creates the "Base" class that all database models will inherit from.

In SQLAlchemy's "declarative" style, you create a Base class once, and then
all your model classes (User, Tournament, Team, etc.) inherit from it.

Why is this needed?
  1. SQLAlchemy uses the Base to track all model classes
  2. Alembic (the migration tool) uses the Base to detect model changes
  3. The Base.metadata object contains information about all tables

When you import all models that inherit from Base, SQLAlchemy can:
  - Create all tables: Base.metadata.create_all(engine)
  - Generate migrations: Alembic inspects Base.metadata to see what changed
"""

from sqlalchemy.orm import declarative_base

# Create the declarative base class
# All models (User, Tournament, etc.) will inherit from this
Base = declarative_base()
