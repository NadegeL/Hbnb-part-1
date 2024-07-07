# src/persistence/pickled.py

import pickle
from src.persistence.repository import Repository
from utils.constants import PICKLE_STORAGE_FILENAME

class PickleRepository(Repository):
    __filename = PICKLE_STORAGE_FILENAME
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
        self.reload()

    def _save_to_file(self):
        with open(self.__filename, "wb") as file:
            pickle.dump(self.__data, file)

    def get_all(self, model_name: str) -> list:
        return self.__data.get(model_name, [])

    def get(self, model_name: str, obj_id: str) -> None:
        for obj in self.__data[model_name]:
            if obj.id == obj_id:
                return obj
        return None

    def reload(self):
        try:
            with open(self.__filename, "rb") as file:
                self.__data = pickle.load(file)
        except FileNotFoundError:
            self._save_to_file()  # Saves the initial empty structure if not found.

    def save(self, obj, save_to_file=True):
        self.__data[obj.__class__.__name__.lower()].append(obj)
        if save_to_file:
            self._save_to_file()

    def update(self, obj):
        for i, o in enumerate(self.__data[obj.__class__.__name__.lower()]):
            if o.id == obj.id:
                self.__data[obj.__class__.__name__.lower()][i] = obj
                self._save_to_file()
                return

    def delete(self, obj) -> bool:
        obj_list = self.__data[obj.__class__.__name__.lower()]
        obj_list = [o for o in obj_list if o.id != obj.id]
        self.__data[obj.__class__.__name__.lower()] = obj_list
        self._save_to_file()
        return True
