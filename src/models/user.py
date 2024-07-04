#src/models/users.py
from sqlalchemy import Column, String, Boolean, DateTime, func
from datetime import datetime
from src.persistence.db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    """User representation"""
    __tablename__ = 'users'

    id = db.Column(String(36), primary_key=True)
    email = db.Column(String(120), unique=True, nullable=False)
    password_hash = db.Column(String(128), nullable=False)
    first_name = db.Column(String, nullable=False)
    last_name = db.Column(String, nullable=False)
    is_admin = db.Column(Boolean, default=False)
    created_at = db.Column(DateTime, default=func.current_timestamp())
    updated_at = db.Column(DateTime, onupdate=func.current_timestamp())

    def __init__(self, email: str, first_name: str, last_name: str, password: str, **kwargs):
        """Initialize the user"""
        super().__init__(**kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = generate_password_hash(password).decode('utf8')

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
        new_user = User(**user)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> "User":
        """Update an existing user"""
        user = User.query.get(user_id)
        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "password" in data:
            user.password_hash = generate_password_hash(data["password"]).decode('utf8')

        db.session.commit()
        return user

    @staticmethod
    def get(user_id: str) -> "User":
        """Get a user by ID"""
        return User.query.get(user_id)

    @staticmethod
    def get_all() -> list["User"]:
        """Get all users"""
        return User.query.all()
