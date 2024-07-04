"""
User related functionality
"""
from src import db
from src.models.base import Base
from src import bcrypt
import sqlalchemy as sa
import uuid

class User(Base, db.Model):
    __tablename__ = 'users'

    id = sa.Column(sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = sa.Column(sa.String(120), unique=True, nullable=False)
    first_name = sa.Column(sa.String(50), nullable=False)
    last_name = sa.Column(sa.String(50), nullable=False)
    password_hash = sa.Column(sa.String(128), nullable=False)
    is_admin = sa.Column(sa.Boolean, default=False)

    def __init__(self, email: str, first_name: str, last_name: str, password: str, is_admin: bool = False, **kwargs):
        """Init method"""
        super().__init__(**kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.set_password(password)
        self.is_admin = is_admin

    def __repr__(self) -> str:
        """Representation of the object"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def set_password(self, password: str) -> None:
        """Set the user's password"""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        """Check the user's password"""
        return bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def get_all() -> list["User"]:
        """Get all users"""
        return User.query.all()

    @staticmethod
    def get(user_id: str) -> "User | None":
        """Get a user by their id"""
        return User.query.get(user_id)

    @staticmethod
    def create(data: dict) -> "User":
        """Create a new user"""
        if User.query.filter_by(email=data["email"]).first():
            raise ValueError("User already exists")

        user = User(
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            password=data["password"],
            is_admin=data.get("is_admin", False)
        )
        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def update(user_id: str, data: dict) -> "User | None":
        """Update an existing user"""
        user = User.query.get(user_id)
        if not user:
            return None

        for key, value in data.items():
            if key == "password":
                user.set_password(value)
            else:
                setattr(user, key, value)

        db.session.commit()
        return user

    @staticmethod
    def delete(user_id: str) -> bool:
        """Delete a user by their id"""
        user = User.get(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True
