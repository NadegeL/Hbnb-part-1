"""
Amenity related functionality
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.persistence.db import db
from src import db



class Amenity(db.Model):
    """Amenity representation"""

    __tablename__ = "amenities"
    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)
    created_at = Column(DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=db.func.current_timestamp(), nullable=False)
    
    places = relationship("Place", secondary="place_amenities", back_populates="amenities")

    def __repr__(self) -> str:
        """Representation of the object"""
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Amenity":
        """Create a new amenity"""
        from src.persistence import repo

        amenity = Amenity(**data)
        repo.save(amenity)
        return amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> "Amenity | None":
        """Update an existing amenity"""
        from src.persistence import repo

        amenity: Amenity | None = repo.get('Amenity', amenity_id)

        if not amenity:
            return None

        if "name" in data:
            amenity.name = data["name"]

        repo.update(amenity)
        return amenity


class PlaceAmenity(db.Model):
    """PlaceAmenity representation"""

    __tablename__ = "place_amenities"
    place_id = Column(String, ForeignKey('places.id'), primary_key=True)
    amenity_id = Column(String, ForeignKey('amenities.id'), primary_key=True)

    place = relationship("Place", back_populates="place_amenities")
    amenity = relationship("Amenity", back_populates="place_amenities")

    def __repr__(self) -> str:
        """Representation of the object"""
        return f"<PlaceAmenity {self.place_id} - {self.amenity_id}>"