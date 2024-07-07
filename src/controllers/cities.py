# src/controllers/cities.py
from flask import request, jsonify, abort
from src.models.city import City
from src.persistence.sqlite_repository import SQLiteRepository

# Initialize repository with the path to your SQLite database
db_path = 'database.db'
repository = SQLiteRepository(db_path)

def get_cities():
    """Endpoint to get all cities"""
    cities = repository.get_all(City)
    return jsonify([city.to_dict() for city in cities])

def get_city_by_id(city_id):
    """Endpoint to get a city by ID"""
    city = repository.get(city_id, City)
    if city is None:
        abort(404, description="City not found")
    return jsonify(city.to_dict())

def create_city():
    """Endpoint to create a new city"""
    data = request.get_json()
    try:
        city = City.create(data)
        repository.save(city)
    except Exception as e:
        abort(400, description=str(e))
    return jsonify(city.to_dict()), 201

def update_city(city_id):
    """Endpoint to update an existing city"""
    data = request.get_json()
    city = repository.get(city_id, City)
    if city is None:
        abort(404, description="City not found")

    for key, value in data.items():
        setattr(city, key, value)
    repository.update(city)
    return jsonify(city.to_dict())

def delete_city(city_id):
    """Endpoint to delete a city by ID"""
    city = repository.get(city_id, City)
    if city is None:
        abort(404, description="City not found")
    repository.delete(city)
    return '', 204
