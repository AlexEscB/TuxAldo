import flet as ft
from models.Transaction import Transaction

class TransactionCard(ft.Container):
    def __init__(self, transaction_obj: Transaction):
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
        amount_color = ft.Colors.GREEN_ACCENT_400 if transaction_obj.type == 'Ingreso' or transaction_obj.type == "Income" else ft.Colors.RED_ACCENT_400
        prefix = "+" if transaction_obj.type == 'income' or transaction_obj.type == "Ingreso" else "-"

        self.content = ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[


                        ft.Text(transaction_obj.title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(transaction_obj.category, size=10, color=ft.Colors.GREY_400),

                    ]

                ),
                
                ft.Text(transaction_obj.description, size=12, color=ft.Colors.GREY_400),

                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[

                        ft.Text(
                            f"{prefix} ${transaction_obj.value:,.2f}", 
                            size=18, 
                            weight=ft.FontWeight.W_600, 
                            color=amount_color,
                            text_align=ft.TextAlign.RIGHT
                        )

                    ]



                )

                
            ]
        )