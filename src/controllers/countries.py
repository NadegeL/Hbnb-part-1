# src/controllers/countries.py
from flask import request, jsonify
from src.models.country import Country
from src.persistence.sqlite_repository import SQLiteRepository  # Adjusted import

db_path = 'database.db'
repository = SQLiteRepository(db_path)

def get_all_countries():
    countries = repository.get_all(Country)
    return jsonify([country.to_dict() for country in countries])

def get_country_by_code(code):
    country = repository.get(code, Country)
    if not country:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(country.to_dict())

def create_country():
    data = request.get_json()
    country = Country.create(data)
    repository.save(country)
    return jsonify(country.to_dict()), 201
