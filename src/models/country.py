# src/models/country.py

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.models.base import Base, MyBaseMixin
from src.persistence.db import db

class Country(Base, MyBaseMixin):
    name = Column(String(128), nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    code = db.Column(db.String(3), unique=True, nullable=False)
    cities = db.relationship('City', backref='country', lazy=True)

    def __repr__(self):
        """String representation of the Country"""
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self):
        """Returns the dictionary representation of the country"""
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Country":
        """Create a new country"""
        if Country.query.filter_by(code=data["code"]).first():
            raise ValueError("Country code already exists")

        new_country = Country(**data)
        db.session.add(new_country)
        db.session.commit()
        return new_country

    @staticmethod
    def update(country_id: str, data: dict) -> "Country | None":
        """Update an existing country"""
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
    def get_all() -> list["Country"]:
        """Get all countries"""
        return Country.query.all()

    @staticmethod
    def delete(country_id: str) -> bool:
        """Delete a country by ID"""
        country = Country.get(country_id)
        if country:
            db.session.delete(country)
            db.session.commit()
            return True
        return False
