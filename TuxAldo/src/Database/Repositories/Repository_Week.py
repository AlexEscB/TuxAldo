import sqlite3 as sql

from Database.database_connector import DatabaseConnector
from models.week import Week

class WeekDao:

    def __init__(self):

        self.db = sql.connect('kakebo.db')
        self.cursor = self.db.cursor()

    def save_week(self, month_id, start_date, end_date):

        self.cursor.execute('''
            INSERT INTO weeks (month_id, start_date, end_date)
            VALUES (?, ?, ?)
        ''', (month_id, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))

        self.db.commit()

    def get_weeks_by_month(self, month_id):

        self.cursor.execute('''
            SELECT id, month_id, start_date, end_date
            FROM weeks
            WHERE month_id = ?
        ''', (month_id,))

        rows = self.cursor.fetchall()

        weeks = []
        for row in rows:
            week = {
                'id': row[0],
                'month_id': row[1],
                'start_date': row[2],
                'end_date': row[3]
            }
            weeks.append(week)

        return weeks