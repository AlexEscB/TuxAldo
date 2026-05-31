import flet as ft

from controllers.home_controller import HomeController
from UI.Components.custom_side_bar import CustomBottomBar


from UI.Components.period_button import PeriodButton


class HomeView(ft.View):
    def __init__(self, page: ft.Page):


        self.control = HomeController()
        self.list_data = self.control.access_data()
        self.bottom_bar = CustomBottomBar()
        self.period_buttons = ft.Column(
            controls=[
                PeriodButton(self.list_data[0]),
                PeriodButton(self.list_data[1]),
                PeriodButton(self.list_data[2]),
                PeriodButton(self.list_data[3])
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        )
        
        
        super().__init__(
            route="/",
            bgcolor="#00021d",
            padding= ft.Padding.only(top=30,left=5,right=5, bottom=10),
            navigation_bar=self.bottom_bar,
            controls=[ft.Column(
                controls=[

                    self.period_buttons

                    
                ],
                expand=True
             
                )
            ]
        )


                         
                         
                         
                         
        
        
        