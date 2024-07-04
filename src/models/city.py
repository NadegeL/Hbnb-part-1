"""
City related functionality using SQLAlchemy
"""

from src import db
from src.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    country_id = db.Column(db.Integer, ForeignKey('countries.id'), nullable=False)

    country = relationship('Country', back_populates='cities')

    def __init__(self, name: str, country_id: int, **kwargs):
        """Init method"""
        super().__init__(**kwargs)
        self.name = name
        self.country_id = country_id

    def __repr__(self) -> str:
        """Representation of the object"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the city"""
        return {
            "id": self.id,
            "name": self.name,
            "country_id": self.country_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get_all() -> list["City"]:
        """Get all cities"""
        return City.query.all()

    @staticmethod
    def get(city_id: int) -> "City | None":
        """Get a city by its id"""
        return City.query.get(city_id)

    @staticmethod
    def create(data: dict) -> "City":
        """Create a new city"""
        city = City(**data)
        db.session.add(city)
        db.session.commit()
        return city

    @staticmethod
    def update(city_id: int, data: dict) -> "City | None":
        """Update an existing city"""
        city = City.get(city_id)
        if not city:
            return None

        if "name" in data:
            city.name = data["name"]
        if "country_id" in data:
            city.country_id = data["country_id"]

        db.session.commit()
        return city

    @staticmethod
    def delete(city_id: int) -> bool:
        """Delete a city by its id"""
        city = City.get(city_id)
        if not city:
            return False

        db.session.delete(city)
        db.session.commit()
        return True
