# src/routes/users.py
"""
This module contains the routes for the users endpoints.
"""

from flask import Blueprint
from src.controllers.users import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/", methods=["GET"])
def get_all_users():
    return get_users()

@users_bp.route("/", methods=["POST"])
def add_new_user():
    return create_user()

@users_bp.route("/<user_id>", methods=["GET"])
def get_specific_user(user_id):
    return get_user_by_id(user_id)

@users_bp.route("/<user_id>", methods=["PUT"])
def update_specific_user(user_id):
    return update_user(user_id)

@users_bp.route("/<user_id>", methods=["DELETE"])
def delete_specific_user(user_id):
    return delete_user(user_id)
