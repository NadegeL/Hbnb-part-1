"""
Country related functionality
"""

from src import db
from sqlalchemy.orm import relationship
import uuid

class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
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
        }

    @staticmethod
    def get_all() -> list["Country"]:
        return Country.query.all()

    @staticmethod
    def get(code: str) -> "Country | None":
        return Country.query.filter_by(code=code).first()

    @staticmethod
    def create(name: str, code: str) -> "Country":
        country = Country(name=name, code=code)
        db.session.add(country)
        db.session.commit()
        return country
