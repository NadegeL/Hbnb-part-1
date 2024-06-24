# config.py

# Import the necessary module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Set the SQLAlchemy Database URI
# Here we're using SQLite for development purposes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set the configuration for using the database or file storage
# This can be set as an environment variable in a production environment
app.config['USE_DATABASE'] = True
