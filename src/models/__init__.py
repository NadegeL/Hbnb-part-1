#models/__init__.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all your models here to ensure they are registered with Base
from .user import User  # assuming you have a user.py with a User model

