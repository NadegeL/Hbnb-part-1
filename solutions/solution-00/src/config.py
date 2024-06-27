"""
This module exports configuration classes for the Flask application.

- DevelopmentConfig
- TestingConfig
- ProductionConfig
"""

from abc import ABC
import os
from dotenv import load_dotenv
from sqlalchemy_utils import database_exists, create_database

# Load environment variables from .env file
load_dotenv()

class Config(ABC):
    """
    Configuration de base
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """
    Configuration de développement
    """
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DEV_DATABASE_URL", "sqlite:///hbnb_dev.db")
    DEBUG = True

    @staticmethod
    def init_app(app):
        """
        Initialisation de l'application Flask
        """
        db_url = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
        if db_url.startswith('sqlite'):
            # Vérifier si la base de données SQLite existe
            if not database_exists(db_url):
                create_database(db_url)
                print(f"Database created at {db_url}")


class TestingConfig(Config):
    """
    Configuration de tests
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "TEST_DATABASE_URL", "sqlite:///:memory:")


class ProductionConfig(Config):
    """
    Configuration de production
    """
    TESTING = False
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost/hbnb_prod"
    )
