# src/config.py

class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'  # Example DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'  # Example DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
