import os
from src.models.user import User
from src import db


class DataManager:
    def __init__(self):
        self.use_database = os.getenv('USE_DATABASE', 'False').lower() in [
            'true', '1', 't', 'y', 'yes']

    def save_user(self, user):
        if self.use_database:
            db.session.add(user)
            db.session.commit()
        else:
            # Logique de sauvegarde basée sur les fichiers
            pass

    def get_user(self, user_id):
        if self.use_database:
            return User.query.get(user_id)
        else:
            # Logique de récupération basée sur les fichiers
            pass
