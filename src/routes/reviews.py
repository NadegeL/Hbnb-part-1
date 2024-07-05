#src/routes/reviews.py
"""
This module contains the routes for the reviews endpoints.
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from src.controllers.reviews import (
    create_review,
    delete_review,
    get_review_by_id,
    get_reviews,
    update_review,
)

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

@reviews_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_reviews():
    return get_reviews()

@reviews_bp.route("/", methods=["POST"])
@jwt_required()
def add_review():
    return create_review()

@reviews_bp.route("/<review_id>", methods=["GET"])
@jwt_required()
def get_specific_review(review_id):
    return get_review_by_id(review_id)

@reviews_bp.route("/<review_id>", methods=["PUT"])
@jwt_required()
def update_specific_review(review_id):
    return update_review(review_id)

@reviews_bp.route("/<review_id>", methods=["DELETE"])
@jwt_required()
def delete_specific_review(review_id):
    return delete_review(review_id)
