# src/models/place.py
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.models.base import Base, MyBaseMixin
from src.persistence.db import db

class Place(Base, MyBaseMixin):
    __tablename__ = 'places'

    name = Column(String(128), nullable=False)
    city_id = Column(String(36), ForeignKey('cities.id'), nullable=False)  # Reference to the City table
    description = Column(String(1024))

    def __repr__(self):
        return f"<Place {self.name} ({self.city_id})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "city_id": self.city_id,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Place":
        new_place = Place(**data)
        db.session.add(new_place)
        db.session.commit()
        return new_place

    @staticmethod
    def update(place_id: str, data: dict) -> "Place | None":
        place = Place.get(place_id)
        if not place:
            return None

        if "name" in data:
            place.name = data["name"]
        if "city_id" in data:
            place.city_id = data["city_id"]
        if "description" in data:
            place.description = data["description"]

        db.session.commit()
        return place

    @staticmethod
    def get_all() -> list["Place"]:
        return Place.query.all()

    @staticmethod
    def delete(place_id: str) -> bool:
        place = Place.get(place_id)
        if place:
            db.session.delete(place)
            db.session.commit()
            return True
        return False
