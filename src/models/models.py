# src/models/models.py
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from typing import Union, List
from src.sqlalchemy_base import Base

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(Base):
    __tablename__ = 'users'
    
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "User":
        if User.query.filter_by(email=data["email"]).first():
            raise ValueError("User already exists")

        new_user = User(**data)
        new_user.set_password(data["password"])
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> Union["User", None]:
        user = User.get(user_id)
        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "password" in data:
            user.set_password(data["password"])
        if "is_admin" in data:
            user.is_admin = data["is_admin"]

        db.session.commit()
        return user

    @staticmethod
    def get_all() -> List["User"]:
        return User.query.all()

    @staticmethod
    def delete(user_id: str) -> bool:
        user = User.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

class Place(Base):
    __tablename__ = 'places'
    
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    city_id = db.Column(db.String(36), db.ForeignKey('cities.id'), nullable=False)

    def __repr__(self):
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "city_id": self.city_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Place":
        if Place.query.filter_by(name=data["name"]).first():
            raise ValueError("Place already exists")

        new_place = Place(**data)
        db.session.add(new_place)
        db.session.commit()
        return new_place

    @staticmethod
    def update(place_id: str, data: dict) -> Union["Place", None]:
        place = Place.get(place_id)
        if not place:
            return None

        for key, value in data.items():
            setattr(place, key, value)

        db.session.commit()
        return place

    @staticmethod
    def get_all() -> List["Place"]:
        return Place.query.all()

    @staticmethod
    def delete(place_id: str) -> bool:
        place = Place.get(place_id)
        if place:
            db.session.delete(place)
            db.session.commit()
            return True
        return False

class Amenity(Base):
    __tablename__ = 'amenities'

    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Amenity":
        if Amenity.query.filter_by(name=data["name"]).first():
            raise ValueError("Amenity already exists")

        new_amenity = Amenity(**data)
        db.session.add(new_amenity)
        db.session.commit()
        return new_amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> Union["Amenity", None]:
        amenity = Amenity.get(amenity_id)
        if not amenity:
            return None

        for key, value in data.items():
            setattr(amenity, key, value)

        db.session.commit()
        return amenity

    @staticmethod
    def get_all() -> List["Amenity"]:
        return Amenity.query.all()

    @staticmethod
    def delete(amenity_id: str) -> bool:
        amenity = Amenity.get(amenity_id)
        if amenity:
            db.session.delete(amenity)
            db.session.commit()
            return True
        return False

class Review(Base):
    __tablename__ = 'reviews'

    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self):
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Review":
        if Review.query.filter_by(comment=data["comment"]).first():
            raise ValueError("Review already exists")

        new_review = Review(**data)
        db.session.add(new_review)
        db.session.commit()
        return new_review

    @staticmethod
    def update(review_id: str, data: dict) -> Union["Review", None]:
        review = Review.get(review_id)
        if not review:
            return None

        for key, value in data.items():
            setattr(review, key, value)

        db.session.commit()
        return review

    @staticmethod
    def get_all() -> List["Review"]:
        return Review.query.all()

    @staticmethod
    def delete(review_id: str) -> bool:
        review = Review.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False
