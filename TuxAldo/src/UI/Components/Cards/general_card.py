import flet as ft
from models.Month import Month
from models.day import Day
from models.week import Week


class GeneralCard(ft.Container):
    def __init__(self, obj):
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

        prefix = "+" if obj.balance >= 0 else "-"

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[

                        ft.Text(obj.title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(self._format_date(obj), size=10, color=ft.Colors.GREY_400),
                    
                        
                    ]
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan("In: ", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)),
                                ft.TextSpan(f"${obj.incomes:,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.GREEN_ACCENT_400))
                            ],
                            size=14,


                        ),
                        ft.Text(
                            spans=[
                                ft.TextSpan("Egr: ", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)),
                                ft.TextSpan(f"${obj.expenses:,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.RED_ACCENT_400))
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
                                ft.TextSpan(f"Bal: ", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)),
                                ft.TextSpan(f"{prefix} ${abs(obj.balance):,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD,color="#ffd900"))
                            ],
                            size=14,
                            
                        ),

                        
                        
                    ]
                )
            ,
            ]
        )

    def _format_date(self, obj) -> str:
        if isinstance(obj, Day):
            return obj.date.strftime("%d/%m")
        elif isinstance(obj, Week):
            return f"{obj.start_date.strftime('%d/%m')} - {obj.end_date.strftime('%d/%m')}"
        elif isinstance(obj, Month):
            return obj.date.strftime("%Y")
    
        return ""

    def on_click(self, e):
        self.page.go("/day")

    