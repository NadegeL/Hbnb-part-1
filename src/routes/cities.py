#src/routes/cities.py
"""
This module contains the routes for the cities endpoints.
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from src.controllers.cities import (
    create_city,
    delete_city,
    get_city_by_id,
    get_cities,
    update_city,
)

cities_bp = Blueprint("cities", __name__, url_prefix="/cities")

@cities_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_cities():
    return get_cities()

@cities_bp.route("/", methods=["POST"])
@jwt_required()
def add_city():
    return create_city()

@cities_bp.route("/<city_id>", methods=["GET"])
@jwt_required()
def get_specific_city(city_id):
    return get_city_by_id(city_id)

@cities_bp.route("/<city_id>", methods=["PUT"])
@jwt_required()
def update_specific_city(city_id):
    return update_city(city_id)

@cities_bp.route("/<city_id>", methods=["DELETE"])
@jwt_required()
def delete_specific_city(city_id):
    return delete_city(city_id)
