# src/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import os

# Initialize Flask extensions globally
db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class="src.config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///hbnb-dev.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key')

    # Initialize app with all extensions
    db.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from src.routes import register_routes
    register_routes(app)

    with app.app_context():
        db.create_all()  # Creates all database tables if they don't exist
        from utils.populate import populate_db
        populate_db()  # Make sure this is called within the app context

    print("Database checked/created successfully!")
    return app
