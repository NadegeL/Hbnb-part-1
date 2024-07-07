# src/persistence/sqlite_repository.py
import sqlite3
import importlib

class SQLiteRepository:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create your tables here, example:
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                    id TEXT PRIMARY KEY,
                                    username TEXT NOT NULL,
                                    email TEXT NOT NULL
                                )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                                    id TEXT PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    code TEXT NOT NULL
                                )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                                    id TEXT PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    state_id TEXT NOT NULL
                                )''')
        self.connection.commit()

    def save(self, obj):
        model_name = obj.__class__.__name__.lower()
        if model_name == 'user':
            self.cursor.execute('INSERT INTO users (id, username, email) VALUES (?, ?, ?)',
                                (obj.id, obj.username, obj.email))
        elif model_name == 'country':
            self.cursor.execute('INSERT INTO countries (id, name, code) VALUES (?, ?, ?)',
                                (obj.id, obj.name, obj.code))
        elif model_name == 'city':
            self.cursor.execute('INSERT INTO cities (id, name, state_id) VALUES (?, ?, ?)',
                                (obj.id, obj.name, obj.state_id))
        self.connection.commit()

    def get_all(self, model):
        model_name = model.__name__.lower()
        if model_name == 'user':
            self.cursor.execute('SELECT * FROM users')
            rows = self.cursor.fetchall()
            return [self._create_instance(model, row) for row in rows]
        elif model_name == 'country':
            self.cursor.execute('SELECT * FROM countries')
            rows = self.cursor.fetchall()
            return [self._create_instance(model, row) for row in rows]
        elif model_name == 'city':
            self.cursor.execute('SELECT * FROM cities')
            rows = self.cursor.fetchall()
            return [self._create_instance(model, row) for row in rows]
        return []

    def get(self, obj_id, model):
        model_name = model.__name__.lower()
        if model_name == 'user':
            self.cursor.execute('SELECT * FROM users WHERE id = ?', (obj_id,))
            row = self.cursor.fetchone()
            if row:
                return self._create_instance(model, row)
        elif model_name == 'country':
            self.cursor.execute('SELECT * FROM countries WHERE id = ?', (obj_id,))
            row = self.cursor.fetchone()
            if row:
                return self._create_instance(model, row)
        elif model_name == 'city':
            self.cursor.execute('SELECT * FROM cities WHERE id = ?', (obj_id,))
            row = self.cursor.fetchone()
            if row:
                return self._create_instance(model, row)
        return None

    def delete(self, obj):
        model_name = obj.__class__.__name__.lower()
        if model_name == 'user':
            self.cursor.execute('DELETE FROM users WHERE id = ?', (obj.id,))
        elif model_name == 'country':
            self.cursor.execute('DELETE FROM countries WHERE id = ?', (obj.id,))
        elif model_name == 'city':
            self.cursor.execute('DELETE FROM cities WHERE id = ?', (obj.id,))
        self.connection.commit()

    def _create_instance(self, model, row):
        module = importlib.import_module(f"src.models.{model.__name__.lower()}")
        cls = getattr(module, model.__name__)
        return cls(**dict(zip([column[0] for column in self.cursor.description], row)))
