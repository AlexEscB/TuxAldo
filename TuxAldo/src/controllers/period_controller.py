import flet as ft

from Database.Repositories.Repository_Month import MonthDao
from Database.Repositories.Repository_Week import WeekDao
from Database.Repositories.Repository_Transaction import TransactionDao
from UI.views.period_view import PeriodView


class PeriodController():
    def __init__(self, data: dict, page: ft.Page):
        self.data = data
        self.page = page
        self.m_dao = MonthDao()
        self.w_dao = WeekDao()
        self.t_dao = TransactionDao()

    def load_period(self):
        if self.data["type"] == "year":
            self.load_year()
        elif self.data["type"] == "month":
            self.load_month()
        elif self.data["type"] == "week":
            self.load_week()
        elif self.data["type"] == "day":
            self.load_day()

    def load_year(self):
        data_year = self.m_dao.get_month_summaries_by_year(self.data["id"])
        new_view = PeriodView(self.page, self.data, data_year)
        self.page.views.append(new_view)
        self.page.update()
    
    def load_month(self):
        data_month = self.w_dao.get_weeks_by_month(self.data["id"])
        new_view = PeriodView(self.page, self.data, data_month)
        self.page.views.append(new_view)
        self.page.update()
    
    def load_week(self):
        data_week = self.t_dao.get_day_summaries_by_week(self.data["start_date"],self.data["end_date"])
        new_view = PeriodView(self.page, self.data, data_week)
        self.page.views.append(new_view)
        self.page.update()
    
    def load_day(self):
        result = self.t_dao.get_transactions_and_data(self.data["date"])
        
        self.data["incomes"] = result["balance_data"]["incomes"]
        self.data["expenses"] = result["balance_data"]["expenses"]
        self.data["balance"] = result["balance_data"]["balance"]
        
        new_view = PeriodView(self.page, self.data, result["transactions"])
        self.page.views.append(new_view)
        self.page.update()

    
    


