"""
Amenity related functionality
"""

from src.models.base import Base
from src import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



class Amenity(Base):
    """Amenity representation"""

    __tablename__ = "amenities"
    name = db.Column(db.String(120), nullable=False)

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


class PlaceAmenity(Base):
    """PlaceAmenity representation"""

    __tablename__ = "place_amenities"
    place_id = db.Column(db.String, ForeignKey('places.id'), primary_key=True)
    amenity_id = db.Column(db.String, ForeignKey('amenities.id'), primary_key=True)

    place = relationship("Place", back_populates="place_amenities")
    amenity = relationship("Amenity", back_populates="place_amenities")

    def __init__(self, place_id: str, amenity_id: str, **kwargs):
        """Init method"""
        super().__init__(**kwargs)
        self.place_id = place_id
        self.amenity_id = amenity_id

    def __repr__(self) -> str:
        """Representation of the object"""
        return f"<PlaceAmenity ({self.place_id} - {self.amenity_id})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "place_id": self.place_id,
            "amenity_id": self.amenity_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get(place_id: str, amenity_id: str) -> "PlaceAmenity | None":
        """Get a PlaceAmenity object by place_id and amenity_id"""
        from src.persistence import repo

        return repo.get("PlaceAmenity", (place_id, amenity_id))

    @staticmethod
    def create(data: dict) -> "PlaceAmenity":
        """Create a new PlaceAmenity object"""
        from src.persistence import repo

        new_place_amenity = PlaceAmenity(**data)
        repo.save(new_place_amenity)
        return new_place_amenity

    @staticmethod
    def delete(place_id: str, amenity_id: str) -> bool:
        """Delete a PlaceAmenity object by place_id and amenity_id"""
        from src.persistence import repo

        place_amenity = PlaceAmenity.get(place_id, amenity_id)

        if not place_amenity:
            return False

        repo.delete(place_amenity)
        return True

    @staticmethod
    def update(entity_id: str, data: dict):
        """Not implemented, isn't needed"""
        raise NotImplementedError(
            "This method is defined only because of the Base class"
        )
