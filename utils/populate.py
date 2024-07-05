# utils/populate.py

""" Populate the database with some data at the start of the application"""

def populate_db(repository):
    from src.models.country import Country
    from src.models.user import User
    from src.models.amenity import Amenity
    from src.models.city import City
    from src.models.review import Review
    from src.models.place import Place
    from src.models.placeamenity import PlaceAmenity

    # Example: Add countries to the repository
    country1 = Country(name="Country1")
    country2 = Country(name="Country2")

    repository.save(country1)
    repository.save(country2)

    # Add similar logic for other models if necessary
