# src/manage.py

""" Entry point for the application. """

from flask_migrate import Migrate
from src.__init__ import create_app
from flask.cli import FlaskGroup

cli = FlaskGroup(create_app=create_app)

app = create_app()
migrate = Migrate(app)

@cli.command("create_db")
def create_db():
    with app.app_context():
        from src.persistence.sqlite_repository import SQLiteRepository
        db_path = 'database.db'
        repository = SQLiteRepository(db_path)
        repository.create_tables()
        print("Database created successfully!")

if __name__ == "__main__":
    cli()
