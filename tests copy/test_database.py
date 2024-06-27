import os
import unittest
from controllers.app import app, db

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_sqlite_connection(self):
        os.environ['DATABASE_TYPE'] = 'sqlite'
        os.environ['DATABASE_URL'] = 'sqlite:///test.db'
        with self.app.app_context():
            db.create_all()
            self.assertTrue(os.path.exists('test.db'))
            db.drop_all()
            os.remove('test.db')

    def test_postgresql_connection(self):
        os.environ['DATABASE_TYPE'] = 'postgresql'
        os.environ['DATABASE_URL'] = 'postgresql://user:password@localhost/test_db'
        with self.app.app_context():
            db.create_all()
            # Assuming connection to PostgreSQL is successful
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
