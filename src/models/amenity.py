# src/models/amenity.py

from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime
from typing import Union, List  # Import Union and List
from src.persistence.db import db
from src.persistence import repo

class Amenity(db.Model):
    """Amenity representation"""
    __tablename__ = 'amenities'

    id = Column(String(36), primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __init__(self, name: str, **kwargs):
        """Initialize the amenity"""
        super().__init__(**kwargs)
        self.name = name

    def __repr__(self) -> str:
        """String representation of the Amenity"""
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(amenity: dict) -> "Amenity":
        """Create a new amenity"""
        amenities: List["Amenity"] = Amenity.get_all()

        for a in amenities:
            if a.name == amenity["name"]:
                raise ValueError("Amenity already exists")

        new_amenity = Amenity(**amenity)
        repo.save(new_amenity)

        return new_amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> Union["Amenity", None]:
        """Update an existing amenity"""
        amenity: Union["Amenity", None] = Amenity.get(amenity_id)

        if not amenity:
            return None

        if "name" in data:
            amenity.name = data["name"]

        repo.update(amenity)
        return amenity

    @staticmethod
    def get(amenity_id: str) -> Union["Amenity", None]:
        """Get an amenity by ID"""
        return repo.get(amenity_id, Amenity)

    @staticmethod
    def delete(amenity_id: str) -> bool:
        """Delete an amenity by ID"""
        amenity: Union["Amenity", None] = Amenity.get(amenity_id)

        if not amenity:
            return False

        repo.delete(amenity)
        return True

    @staticmethod
    def get_all() -> list["Amenity"]:
        """Get all amenities"""
        return repo.get_all(Amenity)
