import flet as ft

class UpperFrame(ft.Container):
    def __init__(self, data: dict):
        super().__init__()
        self.frame_data = data
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
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(self.frame_data["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(self.frame_data["display_date"], size=12, color=ft.Colors.GREY_400)
            ]
        )