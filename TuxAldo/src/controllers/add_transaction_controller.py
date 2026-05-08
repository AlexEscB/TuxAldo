
from datetime import datetime
from models.Transaction import Transaction
from Database.Repositories.Repository_Transaction import TransactionDao

class AddTransactionRepository():
    def __init__(self, view):

        self.view = view
        self.dao = TransactionDao()
    
    def on_save(self,e):
        pass