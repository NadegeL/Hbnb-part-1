# src/routes/users.py

from flask import Blueprint, request, jsonify
from src.controllers.users import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.route('/', methods=['GET'])
def get_users():
    return jsonify(get_all_users())

@users_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@users_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    return jsonify(create_user(data))

@users_bp.route('/<user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.get_json()
    return jsonify(update_user(user_id, data))

@users_bp.route('/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    return jsonify(delete_user(user_id))
