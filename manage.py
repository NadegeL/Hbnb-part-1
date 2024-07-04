#src/ manage.py
""" Entry point for the application. """

from flask_migrate import Migrate
from src.create_app import create_app
from src.persistence.db import db

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
