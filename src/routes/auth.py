from flask import Blueprint
from src.controllers.auth import register_user, login_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    return register_user()

@auth_bp.route('/login', methods=['POST'])
def login():
    return login_user()
