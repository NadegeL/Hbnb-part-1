from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.models.user import User
from src import db, bcrypt

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    """Returns all users"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@users_bp.route('/users', methods=['POST'])
def create_user():
    """Creates a new user"""
    data = request.get_json()

    if not data.get('password'):
        abort(400, "Missing field: password")

    try:
        user = User.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))

    return user.to_dict(), 201

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """Returns a user by ID"""
    user = User.query.get(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")
    return user.to_dict(), 200

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates a user by ID"""
    data = request.get_json()

    try:
        user = User.update(user_id, data)
    except ValueError as e:
        abort(400, str(e))

    if not user:
        abort(404, f"User with ID {user_id} not found")

    return user.to_dict(), 200

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a user by ID"""
    user = User.query.get(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")

    db.session.delete(user)
    db.session.commit()
    return "", 204

@users_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200

    return abort(401, 'Wrong email or password')

@users_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_email = get_jwt_identity()
    return jsonify(logged_in_as=current_user_email), 200
