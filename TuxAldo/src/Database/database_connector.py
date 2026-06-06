import sqlite3 as sql
from config import DB_NAME

class DatabaseConnector:

    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def create_tables(self):
        with sql.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS years (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    year_number INTEGER NOT NULL UNIQUE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS months (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    year_id INTEGER NOT NULL,
                    month_title TEXT NOT NULL,
                    date_start TEXT NOT NULL UNIQUE,
                    FOREIGN KEY (year_id) REFERENCES years (id) ON DELETE CASCADE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS weeks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    month_id INTEGER NOT NULL,
                    start_date TEXT NOT NULL UNIQUE,
                    end_date TEXT NOT NULL UNIQUE,
                    FOREIGN KEY (month_id) REFERENCES months (id) ON DELETE CASCADE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    date TEXT NOT NULL,
                    value REAL NOT NULL,
                    category TEXT NOT NULL,
                    type TEXT NOT NULL,
                    description TEXT
                )
            ''')