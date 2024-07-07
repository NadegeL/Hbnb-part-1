# src/persistence/db.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    from src.models.state import State  # Import State model
    from src.models.city import City  # Import City model
    from src.models.place import Place  # Import Place model
    # Import other models here

    db.create_all()
