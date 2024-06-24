import unittest
from src import create_app, db
from src.models.user import User
from src.persistence import repo
import os

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_ENV'] = 'testing'
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user_db(self):
        with self.app.app_context():
            user = User(email='test@example.com', first_name='Test', last_name='User')
            repo.save(user)
            saved_user = User.query.filter_by(email='test@example.com').first()
            self.assertIsNotNone(saved_user)
            self.assertEqual(saved_user.first_name, 'Test')

    def test_create_user_file(self):
        self.app.config['USE_DATABASE'] = False
        with self.app.app_context():
            user = User(email='test2@example.com', first_name='Test2', last_name='User2')
            repo.save(user)
            # Implement file-based retrieval logic for test
            saved_user = repo.get(user.id)
            self.assertIsNotNone(saved_user)
            self.assertEqual(saved_user.first_name, 'Test2')

if __name__ == '__main__':
    unittest.main()
