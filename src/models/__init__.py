"""
Initialisation de SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Définir l'URL de la base de données
DATABASE_URL = "mysql+mysqldb://<username>:<password>@<host>/<database_name>"

# Créer un moteur SQLAlchemy
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Créer une session SQLAlchemy
Session = scoped_session(sessionmaker(bind=engine))

# Exemple d'utilisation de la session
# session = Session()
# session.close()
