# src/models/country.py

from sqlalchemy import Column, String
from src.persistence.db import db
from src.models.base import MyBaseMixin
from typing import Optional, List

class Country(db.Model, MyBaseMixin):
    __tablename__ = 'countries'
    name = Column(String(128), nullable=False)
    code = Column(String(3), unique=True, nullable=False)

    def __repr__(self):
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Country":
        if Country.query.filter_by(code=data["code"]).first():
            raise ValueError("Country code already exists")
        new_country = Country(**data)
        db.session.add(new_country)
        db.session.commit()
        return new_country

    @staticmethod
    def update(country_id: str, data: dict) -> Optional["Country"]:
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
    def get_all() -> List["Country"]:
        return Country.query.all()

    @staticmethod
    def delete(country_id: str) -> bool:
        country = Country.get(country_id)
        if country:
            db.session.delete(country)
            db.session.commit()
            return True
        return False
