#src/ manage.py
""" Entry point for the application. """

from flask_migrate import Migrate
from src.create_app import create_app
from src.persistence.db import db

app = create_app()
migrate = Migrate(app, db)

@cli.command("create_db")
def create_db():
    db.create_all()
    print("Base de données créée avec succès!")

if __name__ == "__main__":
    cli()
