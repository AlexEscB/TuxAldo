import flet as ft

class CustomBuPrincipal(ft.Container):

    def __init__(self, text, color, colortext=None, on_click=None, **kwargs):
        super().__init__(**kwargs)

        # Guardamos el callback con nombre privado para no pisar
        # propiedades internas de ft.Container
        self._on_click_callback = on_click
        self.text = text

        # Estilo visual
        self.bgcolor = color
        self.width = 100
        self.height = 40
        self.border_radius = 10
        self.padding = 10
        self.colortxt = colortext
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.ink = True
        self.shadow = ft.BoxShadow(
            blur_radius=5,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 2),
        )


        self.content = ft.Row(        # Usamos _text_color() en lugar de self.color para evitar
        # depender de una propiedad que aún no existe en este punto
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(self.text, color= self._set_color_text(), size=14, weight=ft.FontWeight.BOLD)
            ],
        )

        # Asignamos el handler interno como manejador de clic
        self.on_click = self._handle_click

    
    def _handle_click(self, e):
        if self._on_click_callback:
            self._on_click_callback(e)

    def _set_color_text(self):
        if self.colortxt == None:
            return ft.Colors.WHITE
        else:
            return self.colortxt


class ButtonAddTracs(ft.Container):
    def __init__(self, on_clic=None):
        super().__init__()
        self.bgcolor = "#ffd900"
        self.width = 20
        self.height = 20
        self.border_radius = 10
        self.padding = 10
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.ink = True
        self.shadow = ft.BoxShadow(
            blur_radius=5,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 2),
        )
        
    

