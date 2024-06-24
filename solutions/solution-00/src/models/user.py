# src/models/user.py

# Import necessary components from SQLAlchemy and Flask
from sqlalchemy import Column, String, Boolean, DateTime
from src.persistence.db import db
from datetime import datetime
from typing import Union, List
from src.persistence import repo

class User(db.Model):
    """User representation"""
    __tablename__ = 'users'  # Specify the table name

    id = Column(String(36), primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __init__(self, email: str, first_name: str, last_name: str, **kwargs):
        """Initialize the user"""
        super().__init__(**kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """String representation of the User"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(user: dict) -> "User":
        """Create a new user"""
        users: List["User"] = User.get_all()

        for u in users:
            if u.email == user["email"]:
                raise ValueError("User already exists")

        new_user = User(**user)
        repo.save(new_user)

        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> Union["User", None]:
        """Update an existing user"""
        user: Union["User", None] = User.get(user_id)

        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]

        repo.update(user)
        return user

    @staticmethod
    def get(user_id: str) -> Union["User", None]:
        """Get a user by ID
