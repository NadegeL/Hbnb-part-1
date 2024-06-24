# src/persistence/repository.py

# Import necessary components and modules
from src.persistence.file import FileStorage
from src.persistence.db import db
from src.models.user import User
from flask import current_app

class DataManager:
    def __init__(self):
        self.file_storage = FileStorage('data.json')

    def save_user(self, user_data):
        """Save user data to the appropriate storage"""
        if current_app.config['USE_DATABASE']:
            user = User(**user_data)
            db.session.add(user)
            db.session.commit()
        else:
            self.file_storage.add_user(user_data)

    def get_user(self, user_id):
        """Get user data from the appropriate storage"""
        if current_app.config['USE_DATABASE']:
            return User.query.get(user_id)
        else:
            return self.file_storage.get_user(user_id)

    def get_all_users(self):
        """Get all user data from the appropriate storage"""
        if current_app.config['USE_DATABASE']:
            return User.query.all()
        else:
            return self.file_storage.get_all_users()

    def update_user(self, user_data):
        """Update user data in the appropriate storage"""
        if current_app.config['USE_DATABASE']:
            user = User.query.get(user_data['id'])
            if user:
                for key, value in user_data.items():
                    setattr(user, key, value)
                db.session.commit()
        else:
            self.file_storage.update_user(user_data)
