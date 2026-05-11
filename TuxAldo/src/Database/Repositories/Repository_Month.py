import sqlite3 as sql
from Database.database_connector import DatabaseConnector
from models.Month import Month

class MonthDao:

    def __init__(self):

        self.db = DatabaseConnector()

    #funcion de guardado en la base de datos 
        #toma 
    def save_month(self, year_id, month_title, month_date):
        cursor = self.db.cursor
        cursor.execute('''
            INSERT INTO months (year_id, month_title, date_start)
            VALUES (?, ?, ?)
        ''', (year_id, month_title, month_date))
        self.db.conn.commit()
        return cursor.lastrowid

    def get_months_by_year(self, year_id):

        cursor = self.db.cursor

        cursor.execute('''
            SELECT id, year_id, month_title, date
            FROM months
            WHERE year_id = ?
        ''', (year_id,))

        rows = cursor.fetchall()

        months = []
        for row in rows:
            month = Month(month_title=row[2], date=row[3], year=row[1])
            months.append(month)

        return months

