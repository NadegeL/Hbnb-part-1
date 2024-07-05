# src/persistence/memory.py

from datetime import datetime
from typing import Type
from src.persistence.repository import Repository
from src.models.base import Base
from utils.populate import populate_db

class MemoryRepository(Repository):
    _data: dict[str, list] = {
        "country": [],
        "user": [],
        "amenity": [],
        "city": [],
        "review": [],
        "place": [],
        "placeamenity": [],
    }

    def __init__(self) -> None:
        super().__init__()
        self.reload()

    def get_all(self, model: Type[Base]) -> list[Base]:
        model_name = model.__name__.lower()
        return self._data.get(model_name, [])

    def get(self, obj_id: str, model: Type[Base]) -> Base | None:
        model_name = model.__name__.lower()
        for obj in self.get_all(model):
            if obj.id == obj_id:
                return obj
        return None

    def reload(self) -> None:
        populate_db(self)

    def save(self, obj: Base) -> Base:
        model_name = obj.__class__.__name__.lower()
        if obj not in self._data[model_name]:
            self._data[model_name].append(obj)
        return obj

    def update(self, obj: Base) -> Base | None:
        model_name = obj.__class__.__name__.lower()
        for i, o in enumerate(self._data[model_name]):
            if o.id == obj.id:
                obj.updated_at = datetime.now()
                self._data[model_name][i] = obj
                return obj
        return None

    def delete(self, obj: Base) -> bool:
        model_name = obj.__class__.__name__.lower()
        if obj in self._data[model_name]:
            self._data[model_name].remove(obj)
            return True
        return False
