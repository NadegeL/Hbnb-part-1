# src/controllers/users.py

from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.models.user import User
from src.persistence.sqlite_repository import SQLiteRepository

db_path = 'database.db'
repository = SQLiteRepository(db_path)

def get_users():
    """Returns all users"""
    users = repository.get_all(User)
    return jsonify([user.to_dict() for user in users])

def create_user():
    """Creates a new user"""
    data = request.get_json()

    try:
        user = User.create(data)
        repository.save(user)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))

    if user is None:
        abort(400, "User already exists")

    return jsonify(user.to_dict()), 201

def get_user_by_id(user_id: str):
    """Returns a user by ID"""
    user = repository.get(user_id, User)

    if not user:
        abort(404, f"User with ID {user_id} not found")

    return jsonify(user.to_dict()), 200

def update_user(user_id: str):
    """Updates a user by ID"""
    data = request.get_json()
    user = repository.get(user_id, User)

    if not user:
        abort(404, f"User with ID {user_id} not found")

    for key, value in data.items():
        setattr(user, key, value)

    repository.update(user)
    return jsonify(user.to_dict()), 200

def delete_user(user_id: str):
    """Deletes a user by ID"""
    user = repository.get(user_id, User)

    if not user:
        abort(404, f"User with ID {user_id} not found")

    repository.delete(user)
    return "", 204

# Assuming you have a Blueprint setup for your routes
users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/", methods=["GET"])
@jwt_required()  # Ensure JWT authentication is required
def get_all_users():
    return get_users()

@users_bp.route("/", methods=["POST"])
def add_new_user():
    return create_user()

@users_bp.route("/<user_id>", methods=["GET"])
@jwt_required()  # Ensure JWT authentication is required
def get_specific_user(user_id):
    return get_user_by_id(user_id)

@users_bp.route("/<user_id>", methods=["PUT"])
@jwt_required()  # Ensure JWT authentication is required
def update_specific_user(user_id):
    return update_user(user_id)

@users_bp.route("/<user_id>", methods=["DELETE"])
@jwt_required()  # Ensure JWT authentication is required
def delete_specific_user(user_id):
    return delete_user(user_id)
