import flet as ft

import config
from datetime import datetime
from models.Transaction import Transaction
from Database.Repositories.Repository_Transaction import TransactionDao
from controllers.home_controller import HomeController
from controllers.period_controller import PeriodController

class AddTransactionController():
    def __init__(self, view):

        self._view = view
        self._dao = TransactionDao()


    
    def on_save(self, e):
        print("Botón guardar presionado")

        title = self._view.title_component.title_textfield.value
        description = self._view.details_component.details_textfield.value
        raw_value = self._view.value_comp.value_textfield.value
        tipo = self._view._selected_type
        category = self._view.category_comp.dropdown.dropdown.value

        print("Título:", title)
        print("Descripción:", description)
        print("Valor:", raw_value)
        print("Tipo:", tipo)
        print("Categoría:", category)

        if not self._is_valid(title, raw_value, tipo, category):
            print("Validación falló")
            return

        print("Validación correcta")

        value = float(raw_value.replace(",", "."))

        transac = Transaction(
            id=None,
            title=title,
            date=datetime.now().strftime('%Y-%m-%d'),
            value=value,
            category=category,
            type=tipo,
            description=description,
        )

        self._dao.save_transaction(transac)

        print("Transacción guardada")
        self._show_message("Transacción guardada correctamente")
        config.needs_refresh = True
        self._view.page.views.pop()
        self._view.page.go(self._view.page.views[-1].route)


    def on_cancel(self, e):
        self._view.page.views.pop()
        self._view.page.update()
        

    def _is_valid(self, title, raw_value, tipo, category):
    
        if not title or not title.strip():
            self._show_message("Debes ingresar un título")
            return False

        if not raw_value or not raw_value.strip():
            self._show_message("Debes ingresar un valor")
            return False

        if not tipo:
            self._show_message("Selecciona el tipo de transacción")
            return False

        if not category:
            self._show_message("Selecciona una categoría")
            return False

        try:
            float(raw_value.replace(",", "."))
        except ValueError:
            self._show_message("El valor debe ser numérico")
            return False

        return True
    
    def _show_message(self, message):
        self._view.page.snack_bar = ft.SnackBar(
            content=ft.Text(message)
        )
        self._view.page.snack_bar.open = True
        self._view.page.update()