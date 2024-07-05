# src/config.py
"""
This module exports configuration classes for the Flask application.

- DevelopmentConfig
- TestingConfig
- ProductionConfig
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file if present

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'anothersecretkey'
    USE_DATABASE = True  # Default to using a database; change as needed

class DevelopmentConfig(Config):
    """
    Development configuration settings
    This configuration is used when running the application locally.
    This is useful for development and debugging purposes.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///hbnb_dev.db")
    DEBUG = True

class TestingConfig(Config):
    """
    Testing configuration settings
    This configuration is used when running tests.
    You can enable/disable things across the application.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # Use in-memory SQLite for tests
    USE_DATABASE = False  # Use file-based storage for testing if necessary

class ProductionConfig(Config):
    """
    Production configuration settings
    This configuration is used when you create a
    production build of the application.
    The debug or testing options are disabled in this configuration.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/hbnb_prod")
    DEBUG = False
    TESTING = False
