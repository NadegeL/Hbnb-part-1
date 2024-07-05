# src/data_manager.py

from src.models.user import User
from src.models.place import Place
from src.models.amenity import Amenity
from src.models.city import City
from src.models.country import Country
from src.models.review import Review
from src.app import db, app


class DataManager:
    @staticmethod
    def save_user(user):
        if app.config['USE_DATABASE']:
            db.session.add(user)
            db.session.commit()
        else:
            # Implement file-based save logic
            pass

    @staticmethod
    def get_user_by_id(user_id):
        if app.config['USE_DATABASE']:
            return User.query.get(user_id)
        else:
            # Implement file-based get logic
            pass

    @staticmethod
    def save_place(place):
        if app.config['USE_DATABASE']:
            db.session.add(place)
            db.session.commit()
        else:
            # Implement file-based save logic
            pass

    @staticmethod
    def get_place_by_id(place_id):
        if app.config['USE_DATABASE']:
            return Place.query.get(place_id)
        else:
            # Implement file-based get logic
            pass

    @staticmethod
    def save_amenity(amenity):
        if app.config['USE_DATABASE']:
            db.session.add(amenity)
            db.session.commit()
        else:
            # Implement file-based save logic
            pass

    @staticmethod
    def get_amenity_by_id(amenity_id):
        if app.config['USE_DATABASE']:
            return Amenity.query.get(amenity_id)
        else:
            # Implement file-based get logic
            pass

    @staticmethod
    def save_city(city):
        if app.config['USE_DATABASE']:
            db.session.add(city)
            db.session.commit()
        else:
            # Implement file-based save logic
            pass

    @staticmethod
    def get_city_by_id(city_id):
        if app.config['USE_DATABASE']:
            return City.query.get(city_id)
        else:
            # Implement file-based get logic
            pass

    @staticmethod
    def save_country(country):
        if app.config['USE_DATABASE']:
            db.session.add(country)
            db.session.commit()
        else:
            # Implement file-based save logic
            pass

    @staticmethod
    def get_country_by_code(code):
        if app.config['USE_DATABASE']:
            return Country.query.filter_by(code=code).first()
        else:
            # Implement file-based get logic
            pass

    @staticmethod
    def save_review(review):
        if app.config['USE_DATABASE']:
            db.session.add(review)
            db.session.commit()
        else:
            # Implement file-based save logic
            pass

    @staticmethod
    def get_review_by_id(review_id):
        if app.config['USE_DATABASE']:
            return Review.query.get(review_id)
        else:
            # Implement file-based get logic
            pass
