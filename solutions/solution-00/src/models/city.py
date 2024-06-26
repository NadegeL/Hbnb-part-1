"""
City related functionality using SQLAlchemy
"""

from src import db
from src.models.base import Base

class City(Base):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

    country = db.relationship('Country', backref='cities')

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
    def create(name: str, country_id: int) -> "City":
        """Create a new city"""
        city = City(name=name, country_id=country_id)
        db.session.add(city)
        db.session.commit()
        return city
