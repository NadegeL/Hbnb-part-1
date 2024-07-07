# manage.py
from flask_migrate import Migrate
from src.create_app import create_app
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
        from utils.populate import populate_db
        populate_db()
        print("Database created and populated successfully!")

if __name__ == "__main__":
    cli()
