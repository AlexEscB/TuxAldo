import sqlite3 as sql
from config import DB_NAME

from .Repository_Transaction import TransactionDao
from datetime import datetime

class WeekDao:

    def save_week(self, month_id, start_date, end_date):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                INSERT OR IGNORE INTO weeks (month_id, start_date, end_date)
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
                date_s = datetime.strptime(row[0], "%Y-%m-%d").strftime('%d/%m')
                date_e = datetime.strptime(row[1], "%Y-%m-%d").strftime('%d/%m')      
                info_week["display_date"] = date_s + " - " + date_e
                info_week["type"] = "week"
                week_number += 1
                weeks.append(info_week)

            return weeks
        
    def get_week_by_month(self, month_id, date):
        with sql.connect(DB_NAME) as conn:      
            cursor = conn.cursor()

            cursor.execute('''
                SELECT  id, start_date, end_date
                FROM weeks
                WHERE month_id = ? AND ? BETWEEN start_date AND end_date
            ''', (month_id, date.strftime('%Y-%m-%d')))

            rows = cursor.fetchone()
            date_s = datetime.strptime(rows[1], "%Y-%m-%d").strftime('%d/%m')
            date_e = datetime.strptime(rows[2], "%Y-%m-%d").strftime('%d/%m')   

            t_dao = TransactionDao()

            values = t_dao.get_transactions_in_range(rows[1], rows[2])

            return {
                "id" : rows[0],
                "title" : "Semana Actual",
                "month_id" : month_id,
                "start_date" : rows[1],
                "end_date" : rows[2],
                "display_date" : date_s + " - " + date_e,
                "type" : "week",
                "balance" : values["balance"],
                "incomes" : values["incomes"],
                "expenses" : values["expenses"]

            }


                




                
                


        
    
        
        