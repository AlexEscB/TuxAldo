import flet as ft
from datetime import datetime

from UI.Components.custom_textfield import CustomTextField
from UI.Components.custom_textfield import CustomTextFiNumber
from UI.Components.type_selector import TypeSelector, DropdownCategory
from UI.Components.CustomButton2 import CustomBuPrincipal

class TitleComponent(ft.Container):

    def __init__(self):
        super().__init__()

        self.today = datetime.now().strftime("%d/%m")
        self.title_textfield = CustomTextField("Pago de ...", 1, 1,  False, False)

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

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        
                        ft.Text("Movimiento", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(self.today, size=10, color=ft.Colors.GREY_400),
                    ]
                ),
                self.title_textfield




            ]

        )


class DetailsComponent (ft.Container):

    def __init__(self):
        super().__init__()

        self.details_textfield = CustomTextField( "se paga la factura del mes ....", 4, 4, True, False)

        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 200
        self.border_radius = 20
        self.padding = 15
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15, 
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK), 
            offset=ft.Offset(0, 4)
        )

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        
                        ft.Text("Detalles", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ]
                ),
                self.details_textfield




            ]

        )

class ValueComponent(ft.Container):

    def __init__(self):
        super().__init__()

        self.value_textfield = CustomTextFiNumber(hiden_text="COP")

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

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[


                        
                ft.Text("Valor", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                self.value_textfield
                




            ]

        )


class CategoryComponent(ft.Container):
    """
    Agrupa TypeSelector y DropdownCategory en un solo componente.
    Recibe on_type_change y on_category_change desde la view.
    """
    def __init__(self, on_type_change=None, on_category_change=None):
        super().__init__()

        self._on_type_change = on_type_change
        self._on_category_change = on_category_change

        # Dropdown se crea primero porque TypeSelector necesita referenciarlo
        self.dropdown = DropdownCategory(on_change=self._handle_category_change)

        self.selector = TypeSelector(on_change=self._handle_type_change)

        # Estilo igual al resto de componentes
        self.bgcolor = "#04002B"
        self.expand = True
        self.border_radius = 20
        self.padding = 15
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        )

        self.content = ft.Column(
            spacing=10,
            controls=[
                ft.Text("Categoría", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                self.selector,
                self.dropdown,
            ],
        )

    def _handle_type_change(self, tipo: str):
        """Actualiza el dropdown y notifica a la view."""
        self.dropdown.update_categories(tipo)
        if self._on_type_change:
            self._on_type_change(tipo)

    def _handle_category_change(self, categoria: str):
        """Notifica a la view la categoría elegida."""
        if self._on_category_change:
            self._on_category_change(categoria)
    
class RowButtons(ft.Row):
    def __init__(self, **kwds):
        super().__init__(**kwds)

        self.save_button = CustomBuPrincipal("Añadir", "#ffd900", "#00021d")
        self.cancel_button = CustomBuPrincipal("Cancelar", "#04002B")

        self.controls = [
            
            self.cancel_button,
            self.save_button,
            
        ]
        
        self.alignment = ft.MainAxisAlignment.CENTER
        self.spacing = 80
        self.expand = True