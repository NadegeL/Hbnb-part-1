# src/models/__init__.py
"""
Initialization of SQLite and model imports.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src import db

Base = declarative_base()

# Setting up the database URL from environment variables, defaulting to a local SQLite database
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///mydatabase.db')

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Import all models here to ensure they are registered properly on the metadata
    from .base import Base, MyBaseMixin
    from .state import State
    from .city import City
    from .place import Place
    # Import other models here as needed

    Base.metadata.create_all(bind=engine)

