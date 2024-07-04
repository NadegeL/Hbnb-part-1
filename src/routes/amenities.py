#src/routes/amenities.py
"""
This module contains the routes for the amenities blueprint
"""

from flask import Blueprint
from src.controllers.amenities import (
    create_amenity,
    delete_amenity,
    get_amenity_by_id,
    get_amenities,
    update_amenity,
)

amenities_bp = Blueprint("amenities", __name__, url_prefix="/amenities")

@amenities_bp.route("/", methods=["GET"])
def get_all_amenities():
    return get_amenities()

@amenities_bp.route("/", methods=["POST"])
def add_new_amenity():
    return create_amenity()

@amenities_bp.route("/<amenity_id>", methods=["GET"])
def get_specific_amenity(amenity_id):
    return get_amenity_by_id(amenity_id)

@amenities_bp.route("/<amenity_id>", methods=["PUT"])
def update_specific_amenity(amenity_id):
    return update_amenity(amenity_id)

@amenities_bp.route("/<amenity_id>", methods=["DELETE"])
def delete_specific_amenity(amenity_id):
    return delete_amenity(amenity_id)
