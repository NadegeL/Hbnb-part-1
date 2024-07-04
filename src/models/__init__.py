<<<<<<< Updated upstream
#models/__init__.py
from sqlalchemy.ext.declarative import declarative_base
from .user import User

Base = declarative_base()

# Import all your models here to ensure they are registered with Base
from .user import User  # assuming you have a user.py with a User model

=======
"""
Initialisation de SQLLite
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src import db

Base = declarative_base()

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///mydatabase.db')

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)


# Exemple d'utilisation de la session
# session = Session()
# session.close()
>>>>>>> Stashed changes
