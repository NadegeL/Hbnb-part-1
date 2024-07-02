""" Populate the database with some data at the start of the application"""

from src.models import db
from src.models.city import City
from src.models.country import Country

def populate_db(repo):
    # Exemple de données pour peupler la base de données
    countries = [
        country(name="Uruguay", code="UY"),
        country(name="France", code="FR"),
        country(name="Germany", code="DE")
    ]
    
    cities = [
        city(name="Montevideo", country=countries[0]),
        city(name="Paris", country=countries[1]),
        city(name="Berlin", country=countries[2])
    ]

    for country in countries:
        db.session.add(country)
    
    for city in cities:
        db.session.add(city)
    
    db.session.commit()
