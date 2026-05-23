import sqlite3 as sql
from config import DB_NAME
from models.Transaction import Transaction

class TransactionDao:

    def save_transaction(self, transaction):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO transactions (title, date, value, category, type, description)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (transaction.title, transaction.date.strftime('%Y-%m-%d'),
                  transaction.value, transaction.category,
                  transaction.type, transaction.description))
            return cursor.lastrowid

    def find_by_date(self, date):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, title, date, value, category, type, description
                FROM transactions WHERE date = ?
            ''', (date.strftime('%Y-%m-%d'),))
            rows = cursor.fetchall()
        return [Transaction(id=r[0], title=r[1], date=r[2],
                            value=r[3], category=r[4],
                            type=r[5], description=r[6]) for r in rows]

    def find_by_range(self, start_date, end_date):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, title, date, value, category, type, description
                FROM transactions WHERE date BETWEEN ? AND ?
                ORDER BY date ASC
            ''', (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
            rows = cursor.fetchall()
        return [Transaction(id=r[0], title=r[1], date=r[2],
                            value=r[3], category=r[4],
                            type=r[5], description=r[6]) for r in rows]
    

    def get_transactions_in_range(self, start_date, end_date):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute(''' 
                SELECT  
                    SUM(CASE WHEN type = 'Ingreso' THEN value ELSE 0 END),
                    SUM(CASE WHEN type = 'Egreso' THEN value ELSE 0 END)
                FROM transactions
                WHERE date BETWEEN ? AND ?

            ''', (start_date, end_date))
            rows = cursor.fetchone()
            incomes  = rows[0] or 0
            expenses = rows[1] or 0
            return {
                "incomes": incomes,
                "expenses": expenses,
                "balance": incomes - expenses
            }
        
    def get_day_summaries_by_week(self, start_date, end_date):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT date, 
                    SUM(CASE WHEN type = 'Ingreso' THEN value ELSE 0 END),
                    SUM(CASE WHEN type = 'Egreso' THEN value ELSE 0 END)
                FROM transactions
                WHERE date BETWEEN ? AND ?
                GROUP BY date



            ''',(start_date,  end_date))

            rows = cursor.fetchall()
            days = []

            for row in rows:
                day_date = row[0]
                incomes  = row[1] or 0
                expenses = row[2] or 0
                info_day = {
                    "date": day_date,
                    "incomes": incomes,
                    "expenses": expenses,
                    "balance": incomes - expenses
                }
                days.append(info_day)

            return days
            