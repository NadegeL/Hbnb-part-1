# src/__init__.py

# Import necessary components and modules
from flask import Flask
from src.config import app
from src.persistence.db import db

# Import Blueprints
from src.routes.users import users_bp

# Register Blueprints
app.register_blueprint(users_bp)

# Create the database tables
with app.app_context():
    db.create_all()
