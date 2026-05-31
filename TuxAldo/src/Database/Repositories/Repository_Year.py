import sqlite3 as sql
from config import DB_NAME
from .Repository_Transaction import TransactionDao


class YearDao:



    def save_year(self, year_number):

        with sql.connect(DB_NAME) as conn:

            cursor = conn.cursor()

            cursor.execute('''
                INSERT OR IGNORE INTO years (year_number)
                VALUES (?)
            ''', (year_number,))

            return cursor.lastrowid

    def get_all_years(self):

        with sql.connect(DB_NAME) as conn:

            cursor = conn.cursor()

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
        start = f"{date.year}-01-01"
        end   = f"{date.year}-12-31"
        t_dao = TransactionDao()
        values = t_dao.get_transactions_in_range(start, date)

        return {
            "id" : rows[0],
            "year_number" : year,
            "title": year,
            "display_date" : year,
            "type" : "year",
            "balance" : values["balance"],
            "incomes" : values["incomes"],
            "expenses" : values["expenses"]



        }
    
