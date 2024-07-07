# src/models/base.py
from datetime import datetime
import uuid
from src.persistence.db import db  # Ensure this is Flask-SQLAlchemy instance
from typing import Any, List, Optional

class MyBaseMixin:
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class Base(db.Model, MyBaseMixin):
    __abstract__ = True  # This ensures that Base itself isn't created as a table

    @classmethod
    def get(cls, id: str) -> Optional["Any"]:
        return db.session.query(cls).get(id)

    @classmethod
    def get_all(cls) -> List["Any"]:
        return db.session.query(cls).all()

    @classmethod
    def delete(cls, id: str) -> bool:
        obj = cls.get(id)
        if not obj:
            return False
        db.session.delete(obj)
        db.session.commit()
        return True

    @staticmethod
    def create(data: dict) -> Any:
        instance = cls(**data)
        db.session.add(instance)
        db.session.commit()
        return instance

    @staticmethod
    def update(entity_id: str, data: dict) -> Optional[Any]:
        instance = cls.query.get(entity_id)
        if instance:
            for key, value in data.items():
                setattr(instance, key, value)
            db.session.commit()
            return instance
        return None
