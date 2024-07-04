""" Initialize the Flask app. """

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Importer Flask-Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()  # Initialiser Migrate
jwt = JWTManager()   # Initialize JWTManager
bcrypt = Bcrypt()    # Initialize Bcrypt


def create_app(config_class="src.config.DevelopmentConfig") -> Flask:
    """
    Create a Flask app with the given configuration class.
    The default configuration class is DevelopmentConfig.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config.from_object(config_class)
    app.config['JWT_SECRET_KEY'] = 'super-strong-secret-key'  # a strong secret key


    register_extensions(app)
    register_routes(app)
    register_handlers(app)

    with app.app_context():
        # Crée toutes les tables SQLAlchemy si elles n'existent pas
        db.create_all()
        print("Base de données vérifiée/créée avec succès!")

    return app


def register_extensions(app: Flask) -> None:
    """Register the extensions for the Flask app"""
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)  # Initialize SQLAlchemy
    migrate.init_app(app, db)  # Initialiser Flask-Migrate avec l'application et la base de données
    # Further extensions can be added here


def register_routes(app: Flask) -> None:
    """Import and register the routes for the Flask app"""

    # Import the routes here to avoid circular imports
    from src.routes.users import users_bp
    from src.routes.countries import countries_bp
    from src.routes.cities import cities_bp
    from src.routes.places import places_bp
    from src.routes.amenities import amenities_bp
    from src.routes.reviews import reviews_bp

    # Register the blueprints in the app
    app.register_blueprint(users_bp)
    app.register_blueprint(countries_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(amenities_bp)


def register_handlers(app: Flask) -> None:
    """Register the error handlers for the Flask app."""
    app.errorhandler(404)(lambda e: (
        {"error": "Not found", "message": str(e)}, 404
    ))
    app.errorhandler(400)(lambda e: (
        {"error": "Bad request", "message": str(e)}, 400
    ))
