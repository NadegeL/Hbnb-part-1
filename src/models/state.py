#src/models/state.py
from sqlalchemy import Column, String
from src.persistence.db import db
from src.models.base import Base, MyBaseMixin

class State(Base, MyBaseMixin):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "State":
        new_state = State(**data)
        db.session.add(new_state)
        db.session.commit()
        return new_state

    @staticmethod
    def update(state_id: str, data: dict) -> "State | None":
        state = State.get(state_id)
        if not state:
            return None

        if "name" in data:
            state.name = data["name"]

        db.session.commit()
        return state

    @staticmethod
    def get_all() -> list["State"]:
        return State.query.all()

    @staticmethod
    def delete(state_id: str) -> bool:
        state = State.get(state_id)
        if state:
            db.session.delete(state)
            db.session.commit()
            return True
        return False
