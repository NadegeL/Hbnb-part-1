""" Abstract base class for all models """

from datetime import datetime
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

# Initialisation de SQLAlchemy
db = SQLAlchemy()

# Configuration de la base de données
# Remplacez par votre URL de base de données
DATABASE_URL = "sqlite:///hbnb_dev.db"

engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(bind=engine))


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

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
