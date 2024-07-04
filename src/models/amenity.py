# src/models/amenity.py

from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime
from typing import Union, List  # Import Union and List
from src.persistence.db import db

class Amenity(db.Model):
    """Amenity representation"""
    __tablename__ = 'amenities'

    id = Column(String(36), primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __init__(self, name: str, description: str = "", **kwargs):
        """Initialize the amenity"""
        super().__init__(**kwargs)
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        """String representation of the Amenity"""
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(amenity: dict) -> "Amenity":
        """Create a new amenity"""
        amenities: List["Amenity"] = Amenity.get_all()

        for a in amenities:
            if a.name == data["name"]:
                raise ValueError("Amenity already exists")

        new_amenity = Amenity(**data)
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
        if "description" in data:
            amenity.description = data["description"]

        repo.update(amenity)
        return amenity

    @staticmethod
    def get_all() -> List["Amenity"]:
        from src.persistence import repo
        return repo.get_all("amenity")

    @staticmethod
    def delete(amenity_id: str) -> bool:
        from src.persistence import repo
        amenity = Amenity.get(amenity_id)
        if amenity:
            repo.delete(amenity)
            return True
        return False