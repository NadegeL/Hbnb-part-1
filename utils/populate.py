# utils/populate.py
import logging
from src.models.country import Country
from src.models.user import User
from src.models.amenity import Amenity
from src.models.city import City
from src.models.review import Review
from src.models.place import Place
from src.models.placeamenity import PlaceAmenity
from src.persistence.db import db  # Ensure db is imported correctly

def populate_db():
    logging.basicConfig(level=logging.INFO)
    with db.session.begin():
        if not Country.query.first():
            countries = [
                {"name": "USA", "code": "US"},
                {"name": "Canada", "code": "CA"},
                # Add more countries as needed
            ]
            for country_data in countries:
                try:
                    country = Country(name=country_data['name'], code=country_data['code'])
                    db.session.add(country)
                except Exception as e:
                    logging.error(f"Error adding country {country_data['name']}: {e}")
                    continue

        # Example to populate other models similarly
        if not User.query.first():
            users = [
                {"username": "john_doe", "email": "john@example.com"},
                # Add more users as needed
            ]
            for user_data in users:
                try:
                    user = User(username=user_data['username'], email=user_data['email'])
                    db.session.add(user)
                except Exception as e:
                    logging.error(f"Error adding user {user_data['username']}: {e}")
                    continue

        db.session.commit()
        logging.info("Database populated successfully!")
