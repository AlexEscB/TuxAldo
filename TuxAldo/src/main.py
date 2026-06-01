import flet as ft
import asyncio

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
    page.bgcolor = "#00021d"
    page.padding = 0

    

    DatabaseConnector().create_tables()
    ControllerCreateMWD().create_year()

    async def route_change(e=None):
        page.views.clear()
        route = page.route

        if route == "/" or route == "":
            page.views.append(HomeView(page))

        elif route.startswith("/period/month/"):
            month_id = int(route.split("/")[-1])
            page.views.append(PeriodView(page, period_type="month", period_id=month_id))

        elif route.startswith("/period/week/"):
            week_id = int(route.split("/")[-1])
            page.views.append(PeriodView(page, period_type="week", period_id=week_id))

        elif route.startswith("/period/day/"):
            date = route.split("/")[-1]  # "2026-05-22"
            page.views.append(PeriodView(page, period_type="day", period_id=date))

        elif route == "/add_transaccion":
            page.views.append(AddTransaccionView(page))

        page.update()

    #async def view_pop(e):
        #if len(page.views) > 1:
            #page.views.pop()
            #page.update()

    async def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()  # cierra la vista actual
            prev_view = page.views[-1]
            if isinstance(prev_view, HomeView):
                page.views.pop()
                page.views.append(HomeView(page))
            elif isinstance(prev_view, PeriodView):
                
                data = prev_view.data
                page.views.pop()
                PeriodController(data, page).load_period()
            page.update()

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
    page.views.append(HomeView(page))
    page.update()
    page.run_task(check_updates_async)


ft.run(main)