# src/models/amenity.py

from src.app import db
from datetime import datetime
from typing import Union, List

class Amenity(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name: str, description: str = "", **kwargs):
        """Initialize the amenity"""
        super().__init__(**kwargs)
        self.name = name
        self.description = description

    def __repr__(self):
        """String representation of the Amenity"""
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self):
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Amenity":
        """Create a new amenity"""
        if Amenity.query.filter_by(name=data["name"]).first():
            raise ValueError("Amenity already exists")

        new_amenity = Amenity(**data)
        db.session.add(new_amenity)
        db.session.commit()
        return new_amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> Union["Amenity", None]:
        """Update an existing amenity"""
        amenity = Amenity.query.get(amenity_id)

        if not amenity:
            return None

        if "name" in data:
            amenity.name = data["name"]
        if "description" in data:
            amenity.description = data["description"]

        db.session.commit()
        return amenity

    @staticmethod
    def get_all() -> List["Amenity"]:
        """Get all amenities"""
        return Amenity.query.all()

    @staticmethod
    def delete(amenity_id: str) -> bool:
        """Delete an amenity by ID"""
        amenity = Amenity.query.get(amenity_id)
        if amenity:
            db.session.delete(amenity)
            db.session.commit()
            return True
        return False
