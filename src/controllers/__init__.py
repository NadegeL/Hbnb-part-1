# src/__init__.py
from flask import Flask
from src.config import app_config  # Assuming app_config is defined in config.py
from src.persistence.db import db  # Assuming db is defined in persistence/db.py
from src.routes.users import users_bp  # Assuming users_bp is defined in routes/users.py

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)

    app.register_blueprint(users_bp)

    # Create the database tables
    with app.app_context():
        db.create_all()

    return app
