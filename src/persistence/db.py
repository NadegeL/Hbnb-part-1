from src.models.base import Base
from src.persistence.repository import Repository
from src import db
from typing import Type, Any

class DBRepository(Repository):
    """Database repository implementing the Repository (Storage) interface."""

    def __init__(self) -> None:
        from src.models.user import User
        from src.models.amenity import Amenity
        from src.models.city import City
        from src.models.country import Country
        from src.models.place import Place
        from src.models.review import Review

        self.models: dict[str, Type[Base]] = {
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Country": Country,
            "Place": Place,
            "Review": Review,
        }

    def get_all(self, model_name: str) -> list[Base]:
        """Get all objects of a specific model."""
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model {model_name} not found")
        return db.session.query(model).all()

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Get a single object by its ID."""
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model {model_name} not found")
        return db.session.query(model).get(obj_id)

    def save(self, obj: Base) -> None:
        """Save a new object to the database."""
        db.session.add(obj)
        db.session.commit()

    def update(self, obj: Base) -> Base:
        """Update an existing object in the database."""
        db.session.merge(obj)
        db.session.commit()
        return obj

    def delete(self, obj: Base) -> bool:
        """Delete an object from the database."""
        try:
            db.session.delete(obj)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def reload(self) -> None:
        """Reload data from the database (if needed)."""
        pass  # This can be implemented if necessary for your application.
