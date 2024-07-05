from flask import Blueprint, abort, request
from src.models.amenity import Amenity
from src.repositories.sqlite_repository import SQLiteRepository

amenities_bp = Blueprint('amenities', __name__)

@amenities_bp.route('/amenities', methods=['GET'])
def get_amenities():
    """Returns all amenities"""
    amenities = Amenity.get_all()
    return [amenity.to_dict() for amenity in amenities]

@amenities_bp.route('/amenities', methods=['POST'])
def create_amenity():
    """Creates a new amenity"""
    data = request.get_json()
    try:
        amenity = Amenity.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))
    return amenity.to_dict(), 201

@amenities_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity_by_id(amenity_id: str):
    """Returns an amenity by ID"""
    amenity = Amenity.get(amenity_id)
    if not amenity:
        abort(404, f"Amenity with ID {amenity_id} not found")
    return amenity.to_dict()

@amenities_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id: str):
    """Updates an amenity by ID"""
    data = request.get_json()
    updated_amenity = Amenity.update(amenity_id, data)
    if not updated_amenity:
        abort(404, f"Amenity with ID {amenity_id} not found")
    return updated_amenity.to_dict()

@amenities_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id: str):
    """Deletes an amenity by ID"""
    if not Amenity.delete(amenity_id):
        abort(404, f"Amenity with ID {amenity_id} not found")
    return '', 204
