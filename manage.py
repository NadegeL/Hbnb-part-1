from flask.cli import FlaskGroup
from src import create_app, db
from flask_migrate import Migrate

app = create_app()
cli = FlaskGroup(create_app=create_app)
migrate = Migrate(app, db)

@cli.command("reset_db")
def reset_db():
    """
    Drop and recreate all tables in the database.
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Base de données recréée avec succès!")

if __name__ == "__main__":
    cli()
