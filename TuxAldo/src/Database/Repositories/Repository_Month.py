import sqlite3 as sql
import calendar
from datetime import datetime


from config import DB_NAME
from models.Month import Month
from .Repository_Transaction import TransactionDao

class MonthDao:


    #funcion de guardado en la base de datos 
        #toma 
    def save_month(self, year_id, month_title, month_date):
        with sql.connect(DB_NAME) as conn:

            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO months (year_id, month_title, date_start)
                VALUES (?, ?, ?)
            ''', (year_id, month_title, month_date))


            return cursor.lastrowid

    def get_months_by_year(self, year_id):

        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id, year_id, month_title, date_start
                FROM months
                WHERE year_id = ?
            ''', (year_id,))

            rows = cursor.fetchall()

            months = []
            for row in rows:
                month = Month(id=row[0],title=row[2], date_start=row[3])
                months.append(month)

        return months
    
    def get_month_summaries_by_year(self, year_id):

        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id, month_title, date_start
                FROM months
                WHERE year_id = ?
            ''',(year_id))

        rows = cursor.fetchall()
        dao_transac = TransactionDao()
        months = []
        for row in rows:
            date_start = datetime.strptime( row[2], "%Y-%m-%d")
            last_day = calendar.monthrange(date_start.year, date_start.month)[1]
            end_date = f"{date_start.year}-{date_start.month}-{last_day}"
            info_month = dao_transac.get_transactions_in_range(date_start, end_date)
            info_month["title"] = row[1]
            info_month["date_start"] = row [2]
            info_month["month_id"] = row[0]
            months.append(info_month)

        return months




 
        



