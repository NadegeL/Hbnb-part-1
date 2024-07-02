# tests/test_database.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Place  # Assuming these are your SQLAlchemy models


@pytest.fixture(scope="module")
def setup_test():
    # Set up an in-memory SQLite database
    engine = create_engine("sqlite:///:memory:")

    # Create all tables
    Base.metadata.create_all(bind=engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example data seeding
    user = User(username="test_user", email="test@example.com")
    place = Place(name="Test Place", description="Testing Place")
    session.add(user)
    session.add(place)
    session.commit()

    yield session  # Provide the session object to the tests

    # Teardown: clean up the session and drop all tables
    session.rollback()
    session.close()
    Base.metadata.drop_all(bind=engine)


def test_user_creation(setup_test):
    """
    Test user creation and retrieval from the database
    """
    session = setup_test

    # Query for the user
    user = session.query(User).filter_by(username="test_user").first()

    # Assert that the user exists
    assert user is not None, "User should be created and retrievable"


def test_place_creation(setup_test):
    """
    Test place creation and retrieval from the database
    """
    session = setup_test

    # Query for the place
    place = session.query(Place).filter_by(name="Test Place").first()

    # Assert that the place exists
    assert place is not None, "Place should be created and retrievable"


if __name__ == "__main__":
    pytest.main()
