#models/sqlalchemmy_base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# memory.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from .base import Base

class MemoryRepository(Base):
    __tablename__ = 'memory_repository'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Additional attributes and methods