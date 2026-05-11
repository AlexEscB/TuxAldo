import sqlite3 as sql

from Database.database_connector import DatabaseConnector
from models.Transaction import Transaction

class TransactionDao:

    def __init__(self):

        self.db = DatabaseConnector()


    def save_transaction(self, transaction):

        self.db.connect()


        self.db.cursor.execute('''
            INSERT INTO transactions (title, date, value, category, type, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (transaction.title, transaction.date.strftime('%Y-%m-%d'), transaction.value, transaction.category, transaction.type, transaction.description))
    
        self.db.disconnect()
    def find_by_date(self, date):

        cursor = self.db.cursor

        cursor.execute('''
            SELECT id, title, date, value, category, type, description
            FROM transactions
            WHERE date = ?
        ''', (date.strftime('%Y-%m-%d'),))

        rows = cursor.fetchall()

        transactions = []
        for row in rows:
            transaction = Transaction(id=row[0], title=row[1], date=row[2], value=row[3], category=row[4], type=row[5], description=row[6])
            transactions.append(transaction)

        return transactions
    

        
    def find_by_range(self, start_date, end_date):
        cursor = self.db.cursor
        cursor.execute('''
            SELECT id, title, date, value, category, type, description
            FROM transactions
            WHERE date BETWEEN ? AND ?
            ORDER BY date ASC
        ''', (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
    
        rows = cursor.fetchall()
        transactions = []
        for row in rows:
            transaction = Transaction(id=row[0], title=row[1], date=row[2], value=row[3], category=row[4], type=row[5], description=row[6])
            transactions.append(transaction)
        return transactions