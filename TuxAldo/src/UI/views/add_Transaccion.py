import flet as ft
 

from UI.Components.custom_side_bar import CustomBottomBar
from UI.Components.add_trasaction_components import DetailsComponent
from UI.Components.add_trasaction_components import TitleComponent
from UI.Components.add_trasaction_components import ValueComponent
from UI.Components.add_trasaction_components import CategoryComponent
from UI.Components.add_trasaction_components import RowButtons
from controllers.add_transaction_controller import  AddTransactionController


class AddTransaccionView(ft.View):
    def __init__(self, page: ft.Page):
        self.bottom_bar = CustomBottomBar()

        # Estado de la transacción
        self._selected_type     = None
        self._selected_category = None

        # Componentes existentes
        self.title_component   = TitleComponent()
        self.details_component = DetailsComponent()
        self.value_comp        = ValueComponent()
        self.row_bottoms = RowButtons()
        # Nuevo componente: recibe callbacks de la view
        self.category_comp = CategoryComponent(
            on_type_change=self._on_type_change,
            on_category_change=self._on_category_change,
        )

        # controlador

        self.controller = AddTransactionController(self)

        # Conectamos los botones DESPUÉS de crear el controlador
        self.row_bottoms.save_button.on_click   = self.controller.on_save
        self.row_bottoms.cancel_button.on_click = self.controller.on_cancel

        super().__init__(
            route="/add_transaccion",
            bgcolor="#00021d",
            navigation_bar=self.bottom_bar,
            padding=ft.Padding.only(top=30, left=10, right=10, bottom=10),
            controls=[
                ft.Column(
                    controls=[
                        self.title_component,
                        self.category_comp,    # ← entre título y detalles
                        self.details_component,
                        self.value_comp,
                        self.row_bottoms,
                    ],
                    expand=True,
                    scroll=ft.ScrollMode.HIDDEN,  # por si el contenido no cabe
                )
            ],
        )

    def _on_type_change(self, tipo: str):
        """Se dispara cuando el usuario elige Expense o Income."""
        self._selected_type = tipo
        print(f"Tipo seleccionado: {tipo}")  # reemplaza con tu lógica

    def _on_category_change(self, categoria: str):
        """Se dispara cuando el usuario elige una categoría."""
        self._selected_category = categoria
        print(f"Categoría seleccionada: {categoria}")  # reemplaza con tu lógica
