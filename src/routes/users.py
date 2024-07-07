# src/routes/users.py

from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required
from src.models.user import User
from src.persistence import repo

def get_users():
    users = repo.get_all(User)
    return jsonify([user.to_dict() for user in users])

def create_user():
    data = request.get_json()
    try:
        user = User.create(data)
        repo.save(user)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))

    if user is None:
        abort(400, "User already exists")

    return jsonify(user.to_dict()), 201

def get_user_by_id(user_id: str):
    user = repo.get(user_id, User)
    if not user:
        abort(404, f"User with ID {user_id} not found")
    return jsonify(user.to_dict()), 200

def update_user(user_id: str):
    data = request.get_json()
    user = repo.get(user_id, User)
    if not user:
        abort(404, f"User with ID {user_id} not found")

    for key, value in data.items():
        setattr(user, key, value)

    repo.update(user)
    return jsonify(user.to_dict()), 200

def delete_user(user_id: str):
    user = repo.get(user_id, User)
    if not user:
        abort(404, f"User with ID {user_id} not found")

    repo.delete(user)
    return "", 204

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_users():
    return get_users()

@users_bp.route("/", methods=["POST"])
def add_new_user():
    return create_user()

@users_bp.route("/<user_id>", methods=["GET"])
@jwt_required()
def get_specific_user(user_id):
    return get_user_by_id(user_id)

@users_bp.route("/<user_id>", methods=["PUT"])
@jwt_required()
def update_specific_user(user_id):
    return update_user(user_id)

@users_bp.route("/<user_id>", methods=["DELETE"])
@jwt_required()
def delete_specific_user(user_id):
    return delete_user(user_id)
