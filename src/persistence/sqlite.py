# src/persistence/sqlite.py

import sqlite3

class SQLiteRepository:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()  # Ensure tables are created when repository is instantiated

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        self.conn.commit()  # Commit the table creation

    def get_all(self, model):
        table_name = model.__name__.lower() + 's'
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [model(*row) for row in rows]

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

    def __del__(self):
        self.conn.close()
