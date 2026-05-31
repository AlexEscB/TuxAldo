from datetime import datetime
from Database.Repositories.Repository_Month import MonthDao
from Database.Repositories.Repository_Year import YearDao
from Database.Repositories.Repository_Week import WeekDao
from utils.date_utils import get_day_name_es


class HomeController:
    def __init__(self):
        self.date = datetime.now()
        self.year_dao = YearDao()
        self.month_dao = MonthDao()
        self.week_dao = WeekDao()
        self.list_data = []
        self.display_date_day = self.date.strftime('%d/%m')



    def access_data(self):
        year_data = self.year_dao.get_year_by_date(self.date)
        month_data = self.month_dao.get_month_by_year(year_data["id"] ,self.date)
        week_data = self.week_dao.get_week_by_month(month_data["id"],self.date)
        day_data = {
            "title" : get_day_name_es(self.date),
            "date"  : self.date,
            "display_date" : self.display_date_day,
            "type" : "day"
            
            }

        self.list_data.append(year_data)
        self.list_data.append(month_data)
        self.list_data.append(week_data)
        self.list_data.append(day_data)
        

        return self.list_data








