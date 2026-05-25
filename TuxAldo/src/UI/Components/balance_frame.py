import flet as ft

class BalanceFrame(ft.Container):
    def __init__(self, data: dict):
        super().__init__()
        self.data = data
        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 50
        self.border_radius = 20
        self.padding = ft.Padding.symmetric(vertical=10, horizontal=15)
        self.margin = ft.Margin.symmetric(horizontal=5, vertical=0)
        self.border = ft.Border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 4)
        )

        prefix = "+" if data["balance"] >= 0 else "-"

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[

                ft.Text(
                    spans=[
                        ft.TextSpan(f"Bal: ", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)),
                        ft.TextSpan(f"{prefix} ${abs(data['balance']):,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD,color="#ffd900"))
                    ],
                    size=14,
                )   
            ]
        )

        

