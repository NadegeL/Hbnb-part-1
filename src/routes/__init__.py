# src/routes/__init__.py
from flask import Flask
from .users import users_bp
from .countries import countries_bp
from .cities import cities_bp
from .places import places_bp
from .amenities import amenities_bp
from .reviews import reviews_bp

def register_routes(app: Flask):
    app.register_blueprint(users_bp)
    app.register_blueprint(countries_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(amenities_bp)
