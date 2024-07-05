# src/controllers/cities.py

from flask import request, jsonify, abort
from src.models.city import City
from src.models.country import Country
from src.persistence.sqlite_repository import SQLiteRepository

db_path = 'database.db'
repository = SQLiteRepository(db_path)

def get_cities():
    """Returns all cities"""
    cities = repository.get_all(City)
    return [city.to_dict() for city in cities]

def create_city():
    """Creates a new city"""
    data = request.get_json()
    try:
        city = City.create(data)
        repository.save(city)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))
    return city.to_dict(), 201

def get_city_by_id(city_id: str):
    """Returns a city by ID"""
    city = repository.get(city_id, City)
    if not city:
        abort(404, f"City with ID {city_id} not found")
    return city.to_dict()

def update_city(city_id: str):
    """Updates a city by ID"""
    data = request.get_json()
    city = repository.get(city_id, City)
    if not city:
        abort(404, f"City with ID {city_id} not found")
    for key, value in data.items():
        setattr(city, key, value)
    repository.update(city)
    return city.to_dict()

def delete_city(city_id: str):
    """Deletes a city by ID"""
    city = repository.get(city_id, City)
    if not city:
        abort(404, f"City with ID {city_id} not found")
    repository.delete(city)
    return "", 204
Updated File: src/models/city.py
python
Copier le code
# src/models/city.py

"""
City related functionality
"""

from src.models.base import Base
from src.models.country import Country

class City(Base):
    """City representation"""

    name: str
    country_code: str

    def __init__(self, name: str, country_code: str, id=None, created_at=None, updated_at=None) -> None:
        """Initialize a City instance"""
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        self.name = name
        self.country_code = country_code

    def __repr__(self) -> str:
        """String representation"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "City":
        """Create a new city"""
        from src.persistence import repo

        country = Country.get(data["country_code"])
        if not country:
            raise ValueError("Country not found")

        city = City(**data)
        repo.save(city)
        return city

    @staticmethod
    def update(city_id: str, data: dict) -> "City":
        """Update an existing city"""
        from src.persistence import repo

        city = City.get(city_id)
        if not city:
            raise ValueError("City not found")

        for key, value in data.items():
            setattr(city, key, value)

        repo.update(city)
        return city

# src/controllers/cities.py

#from src.repositories.sqlite_repository import SQLiteRepository
#from src.models.city import City

#db_path = 'path/to/your/database.db'
#repository = SQLiteRepository(db_path)

#def create_city(name, country_code):
#    city = City(name, country_code)
#    repository.save(city)
#    return city

#def update_city(city_id, name, country_code):
#    city = repository.get(city_id, City)
#    if city:
#        city.name = name
#        city.country_code = country_code
#        repository.update(city)
#        return city
#    return None
#
#def delete_city(city_id):
#    city = repository.get(city_id, City)
#    if city:
#        repository.delete(city)
#        return True
#    return False
#
# Close the connection when done
#del repository
