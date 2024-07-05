#src/routes/amenities.py
"""
This module contains the routes for the amenities endpoints.
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from src.controllers.amenities import (
    create_amenity,
    delete_amenity,
    get_amenity_by_id,
    get_amenities,
    update_amenity,
)

amenities_bp = Blueprint("amenities", __name__, url_prefix="/amenities")

@amenities_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_amenities():
    return get_amenities()

@amenities_bp.route("/", methods=["POST"])
@jwt_required()
def add_amenity():
    return create_amenity()

@amenities_bp.route("/<amenity_id>", methods=["GET"])
@jwt_required()
def get_specific_amenity(amenity_id):
    return get_amenity_by_id(amenity_id)

@amenities_bp.route("/<amenity_id>", methods=["PUT"])
@jwt_required()
def update_specific_amenity(amenity_id):
    return update_amenity(amenity_id)

@amenities_bp.route("/<amenity_id>", methods=["DELETE"])
@jwt_required()
def delete_specific_amenity(amenity_id):
    return delete_amenity(amenity_id)
