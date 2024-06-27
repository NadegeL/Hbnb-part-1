# src/create_app.py

from flask import Flask
from src.controllers.amenities import amenities_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(amenities_bp, url_prefix='/api')

    # Additional configuration, extensions, etc.

    return app
