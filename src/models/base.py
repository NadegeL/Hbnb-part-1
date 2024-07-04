""" Abstract base class for all models """

from datetime import datetime
from typing import Any,Optional
import uuid
from abc import abstractmethod
import sqlalchemy as sa
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Configuration de la base de données
# Remplacez par votre URL de base de données
DATABASE_URL = "sqlite:///hbnb_dev.db"


class Base(db.Model):
    __abstract__ = True
    id = sa.Column(sa.String(36), primary_key=True)
    created_at = sa.Column(sa.DateTime, default=func.now())
    updated_at = sa.Column(sa.DateTime, default=func.now())

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def delete(cls, id):
        obj = cls.query.get(id)
        if not obj:
            return False
        db.session.delete(obj)
        db.session.commit()
        return True

    @staticmethod
    def create(data):
        raise NotImplementedError("Subclasses should implement this method.")

    @staticmethod
    def update(entity_id, data):
        raise NotImplementedError("Subclasses should implement this method.")
