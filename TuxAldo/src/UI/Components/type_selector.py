import flet as ft


# ─────────────────────────────────────────────
# CustomButton
# ─────────────────────────────────────────────
class CustomButton(ft.Container):
    def __init__(self, text, on_click=None, **kwargs):
        super().__init__(**kwargs)

        # Guardamos el callback con nombre privado para no pisar
        # propiedades internas de ft.Container
        self._on_click_callback = on_click
        self.text = text

        # Estilo visual
        self.bgcolor = "#00021d"
        self.width = 100
        self.height = 40
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


        self.content = ft.Row(        # Usamos _text_color() en lugar de self.color para evitar
        # depender de una propiedad que aún no existe en este punto
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(self.text, color=self._text_color(), size=14, weight=ft.FontWeight.BOLD)
            ],
        )

        # Asignamos el handler interno como manejador de clic
        self.on_click = self._handle_click

    def _text_color(self):
        """Devuelve el color del texto según el tipo de botón."""
        if self.text == "Egreso":
            return ft.Colors.RED_ACCENT_400
        return ft.Colors.GREEN_ACCENT_400

    def _handle_click(self, e):
        """Handler interno: dispara el callback externo si existe."""
        if self._on_click_callback:
            self._on_click_callback(self.text)

    def set_active(self, is_active: bool):
        """Marca visualmente el botón como seleccionado o no."""
        if is_active:
            self.border = ft.Border.all(2, self._text_color())
            self.bgcolor = "#2A3F5F"
        else:
            self.border = ft.Border.all(1, "#1B263B")
            self.bgcolor = "#00021d"
        self.update()


# ─────────────────────────────────────────────
# TypeSelector
# ─────────────────────────────────────────────
class TypeSelector(ft.Row):
    def __init__(self, on_change=None, **kwargs):
        super().__init__(**kwargs)



        # Callback privado que se dispara cuando cambia la selección
        self._on_selection_change = on_change


        # Creamos los dos botones y les pasamos nuestro handler
        self.expense_button = CustomButton("Egreso", on_click=self._handle_selection)
        self.income_button = CustomButton("Ingreso", on_click=self._handle_selection)

        # Asignamos los controles directamente (no usar self.add() en __init__)
        self.controls = [self.expense_button, self.income_button]

        self.alignment = ft.MainAxisAlignment.CENTER
        self.spacing = 80
        self.expand = True

    def _handle_selection(self, selected_type: str):
        """Actualiza el estado visual de ambos botones y notifica al padre."""
        self.expense_button.set_active(selected_type == "Egreso")
        self.income_button.set_active(selected_type == "Ingreso")

        if self._on_selection_change:
            self._on_selection_change(selected_type)


# ─────────────────────────────────────────────
# DropdownCategory
# ─────────────────────────────────────────────
class DropdownCategory(ft.Container):

    # Constante de clase: no cambia por instancia, se comparte entre todas
    CATEGORIES = {
        "Ingreso": [
            "Salario",
            "Honorarios",
            "Venta de Productos",
            "Rendimientos / Inversiones",
            "Transferencias Recibidas",
            "Bonos o Premios",
            "Reembolsos",
            "Ganancias Ocasionales",
        ],
        "Egreso": [
            "Alquiler / Hipoteca",
            "Servicios Públicos",
            "Mercado",
            "Restaurantes",
            "Pasabocas",
            "Transporte",
            "vehiculo",
            "Salud",
            "Suscripciones",
            "Educación",
            "Ropa",
            "Hogar",
            "Ocio",
            "Deudas",
            "Mascotas",
            "Imprevistos",
        ],
    }

    def __init__(self, on_change=None, **kwargs):
        super().__init__(**kwargs)

        self._on_change_callback = on_change

        # Estilo del contenedor
        self.bgcolor = "#00021d"
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

        # El dropdown empieza vacío con un hint informativo
        self.dropdown = ft.Dropdown(
            hint_text="Selecciona Egreso o Ingreso primero",
            options=[],
            expand=True,
            height=40,
            border_radius=10,
            border=ft.Border.all(1, "#1B263B"),
            bgcolor="#1B263B",
            color=ft.Colors.WHITE,
        )
        self.dropdown.on_change = self._handle_change 

        self.content = self.dropdown

    def _handle_change(self, e):
        print("Drpdown cambio:  ", e.control.value )
        if self._on_change_callback:
            self._on_change_callback(self.dropdown.value)

    def update_categories(self, tipo: str):
        categorias = self.CATEGORIES.get(tipo, [])

        self.dropdown.options = [
            ft.dropdown.Option(cat) for cat in categorias
        ]

        self.dropdown.value = None
        self.dropdown.hint_text = "Selecciona una categoría"

        self.update()