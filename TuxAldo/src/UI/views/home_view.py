import flet as ft



from UI.Components.UpperFrame import UpperFrame
from UI.Components.ScrollableList import ScrollableCardList
from UI.Components.custom_side_bar import CustomBottomBar


from UI.Components.period_button import PeriodButton


class HomeView(ft.View):
    def __init__(self,  page: ft.Page, data1 : dict, data2: dict, data3: dict):


        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.bottom_bar = CustomBottomBar()
        self.period_buttons = ft.Column(
            controls=[
                PeriodButton(data1),
                PeriodButton(data2),
                PeriodButton(data3)
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


                         
                         
                         
                         
        
        
        