# src/config.py

# Import necessary components
from flask import Flask
from src.persistence.db import db

# Initialize Flask app
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Configure whether to use database or file storage
app.config['USE_DATABASE'] = True  # Set to False to use file storage
