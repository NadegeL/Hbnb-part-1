#src/models/placeamenity.py
from sqlalchemy import Column, String, ForeignKey
from src.models.base import Base, MyBaseMixin
from src.persistence.db import db

class PlaceAmenity(Base, MyBaseMixin):
    place_id = Column(String(36), ForeignKey('places.id'), nullable=False)
    amenity_id = Column(String(36), ForeignKey('amenities.id'), nullable=False)

    def __repr__(self):
        """String representation of the PlaceAmenity"""
        return f"<PlaceAmenity place_id={self.place_id} amenity_id={self.amenity_id}>"

    def to_dict(self):
        """Returns the dictionary representation of the place amenity"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "amenity_id": self.amenity_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "PlaceAmenity":
        """Create a new place amenity"""
        new_place_amenity = PlaceAmenity(**data)
        db.session.add(new_place_amenity)
        db.session.commit()
        return new_place_amenity

    @staticmethod
    def update(place_amenity_id: str, data: dict) -> "PlaceAmenity | None":
        """Update an existing place amenity"""
        place_amenity = PlaceAmenity.get(place_amenity_id)
        if not place_amenity:
            return None

        if "place_id" in data:
            place_amenity.place_id = data["place_id"]
        if "amenity_id" in data:
            place_amenity.amenity_id = data["amenity_id"]

        db.session.commit()
        return place_amenity

    @staticmethod
    def get_all() -> list["PlaceAmenity"]:
        """Get all place amenities"""
        return PlaceAmenity.query.all()

    @staticmethod
    def delete(place_amenity_id: str) -> bool:
        """Delete a place amenity by ID"""
        place_amenity = PlaceAmenity.get(place_amenity_id)
        if place_amenity:
            db.session.delete(place_amenity)
            db.session.commit()
            return True
        return False
