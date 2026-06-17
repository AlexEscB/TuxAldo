import flet as ft
from datetime import datetime

from UI.Components.UpperFrame import UpperFrame
from UI.Components.ScrollableList import ScrollableCardList
from UI.Components.custom_side_bar import CustomBottomBar
from UI.Components.balance_frame import BalanceFrame
from UI.Components.Cards.general_card import GeneralCard
from UI.Components.Cards.Transaction_Card import TransactionCard
from UI.Components.CustomButton2 import ButtonAddTracs


class PeriodView(ft.View):
    def __init__(self, page: ft.Page, data: dict, children: list):
        # Renombrado de self.data -> self.period_data para evitar
        # choque con el atributo interno "data" que ya define ft.View
        self.period_data = data
        self._page = page
        self.children = children

        self.upper_frame = UpperFrame(data)
        self.transaction_list = ScrollableCardList(self.list_card_create())
        self.balance_frame = BalanceFrame(data)
        self.bottom_bar = CustomBottomBar()

        super().__init__(
            route=f"/period/{data['type']}",
            bgcolor="#00021d",
            padding=ft.Padding.only(top=30, left=5, right=5, bottom=10),
            navigation_bar=self.bottom_bar,
            controls=[
                ft.Column(
                    controls=[
                        self.upper_frame,
                        self.transaction_list,
                        self.balance_frame,
                    ],
                    expand=True
                )
            ]
        )

    def list_card_create(self):
        from controllers.period_controller import PeriodController
        cards = []

        if self.period_data["type"] == "day":
            for c in self.children:
                card = TransactionCard(
                    c,
                    on_edit=self.handle_edit,
                    on_delete=self.handle_delete,
                )
                cards.append(card)

            from UI.views.add_Transaccion import AddTransaccionView
            if self.period_data["date"].date() == datetime.now().date():
                cards.append(ft.Row(
                    controls=[
                        ButtonAddTracs(
                            on_click=lambda e: (
                                self._page.views.append(AddTransaccionView(self._page)),
                                self._page.update()
                            ))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ))
        else:
            for c in self.children:
                card = GeneralCard(
                    c, self._page,
                    on_click=lambda e, c=c: PeriodController(c, self._page).load_period()
                )
                cards.append(card)

        return cards

    def handle_delete(self, transaction):
        from Database.Repositories.Repository_Transaction import TransactionDao
        dao = TransactionDao()
        if dao.delete_transaction(transaction.id):
            card = next(
                (c for c in self.transaction_list.scroll_area.controls
                 if isinstance(c, TransactionCard) and c.transaction.id == transaction.id),
                None
            )
            if card:
                self.transaction_list.remove_card(card)

    def handle_edit(self, transaction):
        # Pendiente: depende de cómo armes la vista de edición
        pass