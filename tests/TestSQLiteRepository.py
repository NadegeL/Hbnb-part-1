import unittest
import sqlite3
from src.repositories.sqlite_repository import SQLiteRepository
from src.models.city import City

class TestSQLiteRepository(unittest.TestCase):

    def setUp(self):
        # Set up SQLite in-memory database
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        
        # Create tables (assuming you have a method in SQLiteRepository for this)
        self.repository = SQLiteRepository(':memory:')
        self.repository.create_tables()  # Create tables if not exists

    def tearDown(self):
        # Clean up: Close connections and clean the database
        self.conn.close()

    def test_get_all(self):
        # Insert mock data
        mock_cities = [
            City("City1", "C1"),
            City("City2", "C2"),
            City("City3", "C3")
        ]
        for city in mock_cities:
            self.repository.save(city)

        # Test get_all method
        cities = self.repository.get_all(City)
        self.assertEqual(len(cities), 3)
        self.assertEqual(cities[0].name, "City1")

    def test_get(self):
        # Insert mock data
        city = City("City1", "C1")
        self.repository.save(city)

        # Test get method
        retrieved_city = self.repository.get(city.id, City)
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city.name, "City1")

    def test_save(self):
        # Create a new city
        new_city = City("New City", "NC")

        # Test save method
        saved_city = self.repository.save(new_city)
        self.assertIsNotNone(saved_city.id)
        self.assertEqual(saved_city.name, "New City")

    def test_update(self):
        # Insert a mock city
        city = City("City1", "C1")
        self.repository.save(city)

        # Modify city attributes
        city.name = "Updated City"

        # Test update method
        updated_city = self.repository.update(city)
        self.assertEqual(updated_city.name, "Updated City")

    def test_delete(self):
        # Insert a mock city
        city = City("City1", "C1")
        self.repository.save(city)

        # Test delete method
        result = self.repository.delete(city)
        self.assertTrue(result)

        # Ensure city is deleted
        deleted_city = self.repository.get(city.id, City)
        self.assertIsNone(deleted_city)

if __name__ == "__main__":
    unittest.main()

