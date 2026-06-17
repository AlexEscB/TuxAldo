import flet as ft

class GeneralCard(ft.Container):
    def __init__(self, data: dict, page: ft.Page, on_click=None):
        super().__init__()
        self.card_data = data
        self._page = page
        self.on_click = on_click
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

        prefix = "+" if data["balance"] >= 0 else "-"

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(self.card_data["title"], size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(self.card_data["display_date"], size=10, color=ft.Colors.GREY_400),
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan("In: ", ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)),
                                ft.TextSpan(f"${data['incomes']:,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_ACCENT_400))
                            ],
                            size=14,
                        ),
                        ft.Text(
                            spans=[
                                ft.TextSpan("Egr: ", ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)),
                                ft.TextSpan(f"${self.card_data['expenses']:,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.RED_ACCENT_400))
                            ],
                            size=14,
                        ),
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan(f"Bal: ", ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)),
                                ft.TextSpan(f"{prefix} ${abs(self.card_data['balance']):,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD, color="#ffd900"))
                            ],
                            size=14,
                        ),
                    ]
                ),
            ]
        )