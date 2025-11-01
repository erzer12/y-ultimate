# This file is used to create the SQLAlchemy 'Base'
# All of our models (like User, Tournament, etc.)
# will inherit from this class.

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
