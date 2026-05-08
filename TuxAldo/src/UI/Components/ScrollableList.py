import flet as ft
from typing import List

class ScrollableCardList(ft.Container):
    def __init__(self,  cards: List[ft.Container] = None):
        super().__init__()
        self.expand = True
        self.padding = 0

        
        
        # El contenedor interno que realmente hace el scroll
        self.scroll_area = ft.Column(
            controls=cards if cards else [],
            scroll=ft.ScrollMode.HIDDEN,  # Scroll suave
            expand=True,
            spacing=1,  # Espacio consistente entre tarjetas
        )
        

        # Estructura visual de la lista
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=self.scroll_area,
                    padding=ft.Padding.symmetric(horizontal=8),
                    expand=True,
                )
            ],
    
        )

    def add_card(self, card: ft.Container):
        self.scroll_area.controls.append(card)
        self.scroll_area.update()

    def replace_cards(self, new_cards: List[ft.Container]):
        self.scroll_area.controls = new_cards
        self.scroll_area.update()