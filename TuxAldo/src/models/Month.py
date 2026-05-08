import datetime
from .week import Week

class Month:
    def __init__(self, id, title, date_start):
        self.id = id
        self.title = title    
        self.date = datetime.datetime.strptime(date_start, '%Y-%m-%d')
        self.weeks = []
        self.balance = 0
        self.incomes = 0
        self.expenses = 0
    

    def calculate_balance(self):

        self.incomes = 0
        self.expenses = 0
        self.balance = 0


        for week in self.weeks:

            self.incomes += week.incomes
            self.expenses += week.expenses
            self.balance += week.balance

    def add_week(self, week):

        self.weeks.append(week)
        self.calculate_balance()