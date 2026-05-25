import flet as ft

from UI.Components.UpperFrame import UpperFrame
from UI.Components.ScrollableList import ScrollableCardList
from UI.Components.custom_side_bar import CustomBottomBar
from UI.Components.balance_frame import BalanceFrame 
from UI.Components.Cards.general_card import GeneralCard

class PeriodView(ft.View):
    def __init__(self,  page: ft.Page, data:dict):

        self.data = data
        self.upper_frame = UpperFrame(data)
        self.transaction_list = ScrollableCardList(self.list_card_create(data))
        self.balance_frame = BalanceFrame(data)
        self.bottom_bar = CustomBottomBar()   

        
        super().__init__(
            route="/Period",
            bgcolor="#00021d",
            padding= ft.Padding.only(top=30,left=5,right=5, bottom=10),
            navigation_bar=self.bottom_bar,
            controls=[ft.Column(
                controls=[
                    
                    self.upper_frame,
                    self.transaction_list,
                    self.balance_frame,


                    
                ],
                expand=True
             
                )
            ]
        )

    def list_card_create(self, data):

        cards = []

        for d in data:
            card = GeneralCard(d)
            cards.append(card)

        return cards

            


                         
                         
                         
                         
        
        
        