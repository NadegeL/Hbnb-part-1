from flask.cli import FlaskGroup
from src import create_app, db
from flask_migrate import Migrate

app = create_app()
cli = FlaskGroup(create_app=create_app)
migrate = Migrate(app, db)

@cli.command("create_db")
def create_db():
    
        db.create_all()
        print("Base de données créer avec succès!")

if __name__ == "__main__":
    cli()
