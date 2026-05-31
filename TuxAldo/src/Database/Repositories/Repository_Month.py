import sqlite3 as sql
import calendar
from datetime import datetime
from utils.date_utils import get_month_name_es


from config import DB_NAME
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


    def get_month_summaries_by_year(self, year_id):

        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id, month_title, date_start
                FROM months
                WHERE year_id = ?
            ''',(year_id,))

        rows = cursor.fetchall()
        dao_transac = TransactionDao()
        months = []
        for row in rows:
            date_start = datetime.strptime( row[2], "%Y-%m-%d")
            last_day = calendar.monthrange(date_start.year, date_start.month)[1]
            end_date = f"{date_start.year}-{date_start.month}-{last_day}"
            info_month = dao_transac.get_transactions_in_range(date_start.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            info_month["title"] = get_month_name_es(row[1])
            info_month["date_start"] = row [2]
            info_month["month_id"] = row[0]
            info_month["type"] = "month"
            info_month["display_date"] = datetime.strptime(row[2], "%Y-%m-%d").strftime("%m/%Y")
            months.append(info_month)

        return months
    
    def get_month_by_year(self, year_id,date):


        with sql.connect(DB_NAME) as conn:

            title_month = calendar.month_name[date.month]

            cursor = conn.cursor()



            cursor.execute('''
                SELECT id, date_start
                FROM months
                WHERE year_id = ? AND month_title = ?
            ''',(year_id, title_month))

            rows = cursor.fetchone()
            date_start = datetime.strptime( rows[1], "%Y-%m-%d")
            last_day = calendar.monthrange(date_start.year, date_start.month)[1]
            end_date = f"{date_start.year}-{date_start.month}-{last_day}"
            t_dao = TransactionDao()

            values = t_dao.get_transactions_in_range(date_start, end_date)

            return {
                "id" : rows[0],
                "year_id" : year_id,
                "title" : get_month_name_es(title_month),
                "date_start" : rows[1],
                "display_date" : datetime.strptime(rows[1], "%Y-%m-%d").strftime("%m/%Y"),
                "type" : "month",
                "balance" : values["balance"],
                "incomes" : values["incomes"],
                "expenses" : values["expenses"]
                


            }




 
        



