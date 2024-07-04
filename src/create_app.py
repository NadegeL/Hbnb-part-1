from flask import Flask
from src.persistence.db import db
from src.routes.amenities import amenities_bp
from src.routes.cities import cities_bp
from src.routes.countries import countries_bp
from src.routes.places import places_bp
from src.routes.reviews import reviews_bp
from src.routes.users import users_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://matrix_sql:SQL2024@localhost/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(amenities_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(countries_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(users_bp)

    return app
