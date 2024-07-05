from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base, MyBaseMixin
from src.persistence.sqlite import SQLiteRepository  # Adjust the import path if necessary

class City(Base, MyBaseMixin):
    name = Column(String(128), nullable=False)
    state_id = Column(String(36), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='city', lazy=True)

    def __repr__(self):
        """String representation of the City"""
        return f"<City {self.name} ({self.state_id})>"

    def to_dict(self):
        """Returns the dictionary representation of the city"""
        return {
            "id": self.id,
            "name": self.name,
            "state_id": self.state_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "City":
        """Create a new city"""
        new_city = City(**data)
        db.session.add(new_city)
        db.session.commit()
        return new_city

    @staticmethod
    def update(city_id: str, data: dict) -> "City | None":
        """Update an existing city"""
        city = City.get(city_id)
        if not city:
            return None

        if "name" in data:
            city.name = data["name"]
        if "state_id" in data:
            city.state_id = data["state_id"]

        db.session.commit()
        return city

    @staticmethod
    def get_all() -> list["City"]:
        """Get all cities"""
        return City.query.all()

    @staticmethod
    def delete(city_id: str) -> bool:
        """Delete a city by ID"""
        city = City.get(city_id)
        if city:
            db.session.delete(city)
            db.session.commit()
            return True
        return False

# Assuming that db is imported correctly from your db.py file
from src.persistence.db import db
