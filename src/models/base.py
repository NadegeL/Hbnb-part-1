from datetime import datetime
from typing import Any, List, Optional
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, String, DateTime
import uuid
from src.persistence.db import db

@as_declarative()
class Base:
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class MyBaseMixin:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

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

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> Any:
        raise NotImplementedError("create method not implemented")

    @staticmethod
    def update(entity_id: str, data: dict) -> Optional[Any]:
        raise NotImplementedError("update method not implemented")
