""" Entry point for the application. """

from flask.cli import FlaskGroup
from src import create_app, db

cli = FlaskGroup(create_app=create_app)

@cli.command("reset_db")
def reset_db():
    """
    Drop and recreate all tables in the database.
    """
    from src import db
    from src.models.base import Base

    with cli.create_app().app_context():
        db.drop_all()
        db.create_all()
        print("Base de données recréée avec succès!")

if __name__ == "__main__":
    cli()
