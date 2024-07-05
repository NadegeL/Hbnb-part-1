# src/repositories/sqlite_repository.py

import sqlite3
from src.models.city import City  # Adjust import path based on your project structure

class SQLiteRepository:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_all(self, model):
        table_name = model.__name__.lower() + 's'
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [model(*row) for row in rows]  # Assuming model constructor accepts a tuple of data

    def get(self, obj_id, model):
        table_name = model.__name__.lower() + 's'
        query = f"SELECT * FROM {table_name} WHERE id = ?"
        self.cursor.execute(query, (obj_id,))
        row = self.cursor.fetchone()
        if row:
            return model(*row)
        else:
            return None

    def save(self, obj):
        table_name = obj.__class__.__name__.lower() + 's'
        fields = ','.join(obj.__dict__.keys())
        placeholders = ','.join('?' * len(obj.__dict__))
        values = tuple(obj.__dict__.values())
        query = f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()
        return obj

    def update(self, obj):
        table_name = obj.__class__.__name__.lower() + 's'
        fields = ','.join(f"{key} = ?" for key in obj.__dict__.keys() if key != 'id')
        values = tuple(value for key, value in obj.__dict__.items() if key != 'id')
        query = f"UPDATE {table_name} SET {fields} WHERE id = ?"
        self.cursor.execute(query, values + (obj.id,))
        self.conn.commit()
        return obj

    def delete(self, obj):
        table_name = obj.__class__.__name__.lower() + 's'
        query = f"DELETE FROM {table_name} WHERE id = ?"
        self.cursor.execute(query, (obj.id,))
        self.conn.commit()
        return True
