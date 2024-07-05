# src/create_app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from src.routes.amenities import amenities_bp
    from src.routes.cities import cities_bp
    from src.routes.countries import countries_bp
    from src.routes.places import places_bp
    from src.routes.reviews import reviews_bp
    from src.routes.users import users_bp
    from src.routes.auth import auth_bp

    app.register_blueprint(amenities_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(countries_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)

    return app

if __name__ == "__main__":
    app = create_app('config.DevelopmentConfig')
    app.run(debug=True)
