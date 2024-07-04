"""
Country related functionality
"""

from src import db
from sqlalchemy.orm import relationship
import uuid

class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(3), nullable=False, unique=True)

    cities = relationship('City', backref='country', lazy=True)

    def __init__(self, name: str, code: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get_all() -> list["Country"]:
        return Country.query.all()

    @staticmethod
    def get(country_id: str) -> "Country | None":
        return Country.query.get(country_id)

    @staticmethod
    def create(data: dict) -> "Country":
        country = Country(**data)
        db.session.add(country)
        db.session.commit()
        return country

    @staticmethod
    def update(country_id: str, data: dict) -> "Country | None":
        country = Country.get(country_id)
        if not country:
            return None

        if "name" in data:
            country.name = data["name"]
        if "code" in data:
            country.code = data["code"]

        db.session.commit()
        return country

    @staticmethod
    def delete(country_id: str) -> bool:
        country = Country.get(country_id)
        if not country:
            return False

        db.session.delete(country)
        db.session.commit()
        return True
