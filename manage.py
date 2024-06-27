# manage.py
""" Entry point for the application. """

from flask.cli import FlaskGroup
from src.create_app import create_app

cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
