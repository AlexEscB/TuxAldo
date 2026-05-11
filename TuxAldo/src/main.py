import flet as ft

from models.Transaction import Transaction
from models.day import Day
from models.week import Week
from models.Month import Month

from UI.Components.Cards.Transaction_Card import TransactionCard
from UI.Components.Cards.general_card import GeneralCard
from UI.views.period_view import PeriodView
from UI.views.home_view import HomeView
from UI.views.add_Transaccion import AddTransaccionView



async def main(page: ft.Page):


    page.title = "TuxAldo"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#00021d"
    page.padding = 0
        
    # Título de la sección

    # Transacción de prueba
    transac = Transaction(1, "Salario", "2024-06-15", 1750000, "Trabajo", "income", "Pago mensual de nómina")
    transac2 = Transaction(2, "Supermercado", "2024-06-15", 250000, "Comida", "expense", "Compra semanal")
    transac3 = Transaction(3, "Compra de medicamentos", "2024-06-16", 22000, "Salud", "expense", "compra de medicacion")
    transac4 = Transaction(1, "Mesada semanal", "2024-06-17", 100000, "Ganancia ocasional", "income", "Pago mensual de nómina")
    transac5 = Transaction(1, "Venta de ropa usada", "2024-06-17", 50000, "Ganancia ocasional", "income", "Pago mensual")
    transac6 = Transaction(1, "Cena con amigos", "2024-06-18", 80000, "Ocio", "expense", "Salida a cenar con amigos")
    transac7 = Transaction(1, "Pago de servicios", "2024-06-18", 150000, "Hogar", "expense", "Pago mensual de servicios")


    day1 = Day(1,"2024-06-15")
    day2 = Day(2,"2024-06-16")
    day3 = Day(3,"2024-06-17")
    day4 = Day(4,"2024-06-18")

    week1 = Week(1,"Semana 1", "2024-06-10", "2024-06-16")
    week2 = Week(2,"Semana 2", "2024-06-17", "2024-06-23")

    mounth1 = Month(1, "Junio", "2024-06-01")
    



    day1.add_transaction(transac)
    day1.add_transaction(transac2)
    day2.add_transaction(transac3)
    day3.add_transaction(transac4)
    day3.add_transaction(transac5)
    day4.add_transaction(transac6)
    day4.add_transaction(transac7)  

    week1.add_day(day1)
    week1.add_day(day2)
    week2.add_day(day3)
    week2.add_day(day4)

    mounth1.add_week(week1)
    mounth1.add_week(week2)

    ListCard = [
        GeneralCard(day1),
        GeneralCard(day2),
        TransactionCard(transac),
        TransactionCard(transac2),
        TransactionCard(transac3),
        TransactionCard(transac4),
        TransactionCard(transac5),
        TransactionCard(transac6),
        TransactionCard(transac7),
        GeneralCard(week1),
        GeneralCard(week2),
        GeneralCard(mounth1)
    ]

    

    async def route_change(e=None):
        page.views.clear()

        if page.route == "/add_transaccion":
                    
            page.views.append(AddTransaccionView(page))  # Aquí puedes pasar el día que quieras mostrar
        
        elif page.route == "/add_transaccion":
            
            await page.push_route("/")

            
        else:
            await page.push_route("/add_transaccion")  # Aquí puedes pasar el día que quieras mostrar
        page.update()

    async def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            await page.push_route(top_view.route)
            page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    await route_change()

    # Añadimos las tarjetas

ft.run(main)