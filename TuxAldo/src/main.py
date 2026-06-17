import flet as ft
import asyncio
import config
from Database.database_connector import DatabaseConnector
from controllers.controller_create_mwd import ControllerCreateMWD
from UI.views.home_view import HomeView
from UI.views.period_view import PeriodView
from UI.views.add_Transaccion import AddTransaccionView
from controllers.period_controller import PeriodController
from utils.update_checker import check_for_update


async def main(page: ft.Page):
    page.title = "TuxAldo"
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(
        popup_menu_theme=ft.PopupMenuTheme(
            color="#04002B",
            shadow_color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            shape=ft.RoundedRectangleBorder(radius=10),
        )
    )
    page.bgcolor = "#00021d"
    page.padding = 0

    DatabaseConnector().create_tables()
    ControllerCreateMWD().create_year()

    def route_change(e):
        if page.route == "/":
            return
        if config.needs_refresh:
            config.needs_refresh = False
            prev_view = page.views[-1]
            if isinstance(prev_view, HomeView):
                page.views.pop()
                page.views.append(HomeView(page))
            elif isinstance(prev_view, PeriodView):
                # Antes: prev_view.data (chocaba con el atributo interno de ft.View)
                period_data = prev_view.period_data
                page.views.pop()
                PeriodController(period_data, page).load_period()
        page.update()

    async def view_pop(e):
        if len(page.views) <= 1:
            return
        page.views.pop()
        if page.views:
            await page.push_route(page.views[-1].route)

    async def check_updates_async():
        result = check_for_update()
        print("check updates ejecutado")
        if result:
            hay_actualizacion, version_nueva, url = result
            if hay_actualizacion:
                snack = ft.SnackBar(
                    content=ft.Text(f"Nueva versión disponible: {version_nueva}"),
                    action="Descargar",
                    on_action=lambda e: asyncio.ensure_future(page.launch_url(url)),
                    open=True
                )
                page.overlay.append(snack)
                page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.on_back_press = view_pop
    page.views.append(HomeView(page))
    page.update()
    page.run_task(check_updates_async)


ft.run(main)