# test_app.py

# Import necessary modules and components
import unittest
from flask import current_app
from src.config import app, db
from src.models.user import User
from src.persistence.repository import DataManager

class TestApp(unittest.TestCase):
    def setUp(self):
        """Set up the Flask app context and initialize the database"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
        self.data_manager = DataManager()

    def tearDown(self):
        """Tear down the database"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_save_user_db(self):
        """Test saving a user using the database"""
        self.app.config['USE_DATABASE'] = True
        user_data = {
            'id': '123',
            'email': 'test@example.com',
            'password': 'securepassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'is_admin': False
        }
        self.data_manager.save_user(user_data)
        with self.app.app_context():
            user = User.query.get('123')
            self.assertIsNotNone(user)
            self.assertEqual(user.email, 'test@example.com')

    def test_save_user_file(self):
        """Test saving a user using file storage"""
        self.app.config['USE_DATABASE'] = False
        user_data = {
            'id': '124',
            'email': 'file@example.com',
            'password': 'filepassword',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'is_admin': False
        }
        self.data_manager.save_user(user_data)
        user = self.data_manager.get_user('124')
        self.assertIsNotNone(user)
        self.assertEqual(user['email'], 'file@example.com')

if __name__ == '__main__':
    unittest.main()
