# src/models/user.py
from sqlalchemy import Column, String, Boolean, DateTime, func
from datetime import datetime
from src.persistence.db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    """User representation"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(String(128), nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, email: str, first_name: str, last_name: str, password: str, **kwargs):
        """Initialize the user"""
        super().__init__(**kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.set_password(password)

    def set_password(self, password):
        """Hash and set the password"""
        self.password_hash = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check the hashed password"""
        return check_password_hash(self.password_hash, password)

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
            user.set_password(data["password"])

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
