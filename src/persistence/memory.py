# src/persistence/memory.py

"""
This module exports a Repository that does not persist data,
it only stores it in memory
"""

from datetime import datetime
from src.models.base import Base
from src.persistence.repository import Repository
from utils.populate import populate_db


class MemoryRepository(Repository):
    """
    A Repository that does not persist data, it only stores it in memory

    Every time the server is restarted, the data is lost
    """

    __data: dict[str, list] = {
        "country": [],
        "user": [],
        "amenity": [],
        "city": [],
        "review": [],
        "place": [],
        "placeamenity": [],
    }

    def __init__(self) -> None:
        """Calls reload method"""
        self.reload()

    def get_all(self, model: type) -> list:
        """Get all objects of a given model"""
        model_name = model.__name__.lower()
        return self.__data.get(model_name, [])

    def get(self, obj_id: str, model: type):
        """Get an object by its ID"""
        model_name = model.__name__.lower()
        for obj in self.get_all(model):
            if obj.id == obj_id:
                return obj
        return None

    def reload(self):
        """Populates the database with some dummy data"""
        populate_db(self)

    def save(self, obj: Base):
        """Save an object"""
        model_name = obj.__class__.__name__.lower()
        if obj not in self.__data[model_name]:
            self.__data[model_name].append(obj)
        return obj

    def update(self, obj: Base):
        """Update an object"""
        model_name = obj.__class__.__name__.lower()
        for i, o in enumerate(self.__data[model_name]):
            if o.id == obj.id:
                obj.updated_at = datetime.now()
                self.__data[model_name][i] = obj
                return obj
        return None

    def delete(self, obj: Base) -> bool:
        """Delete an object"""
        model_name = obj.__class__.__name__.lower()
        if obj in self.__data[model_name]:
            self.__data[model_name].remove(obj)
            return True
        return False
