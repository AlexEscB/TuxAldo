import flet as ft

class ContextMenuCustom(ft.ContextMenu):
    def __init__(self, content, items: list[tuple[str, callable]]):
        # items: lista de tuplas (label, callback)
        menu_items = [
            ft.PopupMenuItem(
                content=ft.Text(label, color=ft.Colors.WHITE),
                on_click=callback,
            )
            for label, callback in items
        ]

        super().__init__(
            content=content,
            primary_items=menu_items,
            primary_trigger=ft.ContextMenuTrigger.LONG_PRESS,
        )