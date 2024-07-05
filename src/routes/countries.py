#src/routes/countries.py
"""
This module contains the routes for the countries endpoints.
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from src.controllers.countries import (
    get_all_countries,
    get_country_by_code,
    create_country,
)

countries_bp = Blueprint("countries", __name__, url_prefix="/countries")

@countries_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return get_all_countries()

@countries_bp.route("/<code>", methods=["GET"])
@jwt_required()
def get_country(code):
    return get_country_by_code(code)

@countries_bp.route("/", methods=["POST"])
@jwt_required()
def add_country():
    return create_country()
