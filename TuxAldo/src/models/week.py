import datetime

class Week:
    def __init__(self, id, title, start_date, end_date):

        self.title = title
        self.id = id
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        self.days = []
        self.balance = 0
        self.incomes = 0
        self.expenses = 0

    def add_day(self, day):

        self.days.append(day)
        self.calculate_balance()

    def calculate_balance(self):
        
        self.balance = 0
        self.incomes = 0
        self.expenses = 0

        for day in self.days:

            day.calculate_balance()
            
            self.incomes += day.incomes
            self.expenses += day.expenses
            self.balance += day.balance