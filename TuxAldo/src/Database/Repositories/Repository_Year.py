import sqlite3 as sql
from config import DB_NAME

from Database import database_connector


class YearDao:

    def __init__(self):

        self.db = database_connector.DatabaseConnector()


    def save_year(self, year_number):

        cursor = self.db.cursor

        cursor.execute('''
            INSERT INTO years (year_number)
            VALUES (?)
        ''', (year_number,))

        self.db.conn.commit()

        return cursor.lastrowid

    def get_all_years(self):

        cursor = self.db.cursor

        cursor.execute('''
            SELECT id, year_number
            FROM years
            ORDER BY year_number ASC
        ''')

        rows = cursor.fetchall()

        years = []
        for row in rows:
            year = {
                'id': row[0],
                'year_number': row[1]
            }
            years.append(year)

        return years
    
    def get_year_by_date(self, date):

        year = str(date.year)


        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id
                FROM years
                WHERE year_number = ?
            ''',(year,))

        rows = cursor.fetchone()

        return {
            "id" : rows[0],
            "year_number" : year,
            "title": year,
            "display_date" : year,
            "type" : "year"



        }
    
