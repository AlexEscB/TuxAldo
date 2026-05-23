import sqlite3 as sql
from config import DB_NAME
from models.week import Week
from .Repository_Transaction import TransactionDao

class WeekDao:

    def save_week(self, month_id, start_date, end_date):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO weeks (month_id, start_date, end_date)
                VALUES (?, ?, ?)
            ''', (month_id, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))

            return cursor.lastrowid

    def get_weeks_by_month(self, month_id):
        with sql.connect(DB_NAME) as conn:      
            cursor = conn.cursor()

            cursor.execute('''
                SELECT  start_date, end_date
                FROM weeks
                WHERE month_id = ?
            ''', (month_id,))

            rows_date = cursor.fetchall()
            dao_trans = TransactionDao()
            week_number = 1
            weeks = []
            for row in rows_date:
                info_week = dao_trans.get_transactions_in_range(row[0],row[1])
                info_week["title"] = "Semana " + str(week_number)
                info_week["start_date"] = row[0]
                info_week["end_date"] = row[1]
                week_number += 1
                weeks.append(info_week)

            return weeks

                




                
                


        
    
        
            