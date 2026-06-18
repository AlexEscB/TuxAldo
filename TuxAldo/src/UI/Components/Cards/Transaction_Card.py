import flet as ft
from models.Transaction import Transaction
from UI.Components.context_menu_custom import ContextMenuCustom

class TransactionCard(ft.Container):
    def __init__(self, transaction_obj: Transaction, on_edit=None, on_delete=None):

        self.transaction = transaction_obj
        super().__init__()
        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 120
        self.border_radius = 20
        self.padding = 15
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15, 
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK), 
            offset=ft.Offset(0, 4)
        )

        # Definimos el color según el tipo
        amount_color = ft.Colors.GREEN_ACCENT_400 if self.transaction.type == 'Ingreso' or self.transaction.type == "Income" else ft.Colors.RED_ACCENT_400
        prefix = "+" if self.transaction.type == 'income' or self.transaction.type == "Ingreso" else "-"

        card_content = ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(self.transaction.title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(self.transaction.category, size=10, color=ft.Colors.GREY_400),
                    ]
                ),
                ft.Text(self.transaction.description, size=12, color=ft.Colors.GREY_400),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Text(
                            f"{prefix} ${self.transaction.value:,.2f}",
                            size=18,
                            weight=ft.FontWeight.W_600,
                            color=amount_color,
                            text_align=ft.TextAlign.RIGHT
                        )
                    ]
                )
            ],
        )

        # Envolvemos la Column en un Container con superficie pintada
        # para que el área de detección del ContextMenu cubra toda la card
        card_surface = ft.Container(
            content=card_content,
            bgcolor=ft.Colors.TRANSPARENT,
            expand=True,
        )

        self.content = ContextMenuCustom(
            content=card_surface,
            items=[
                ("Editar", lambda e: on_edit(self.transaction) if on_edit else None),
                ("Eliminar", lambda e: on_delete(self.transaction) if on_delete else None),
            ]
        )