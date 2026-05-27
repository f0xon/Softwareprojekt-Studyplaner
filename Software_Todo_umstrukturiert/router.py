# pyright: ignore[reportArgumentType]
import flet as ft

from view.einstellungen_view import EinstellungenView
from view.erzeuge_todo_view import ErzeugeTodoView
from view.meinStudium_view import MeinStudiumView
from view.todos_view import TodosView
from view.filtere_todo_view import FiltereTodoView
from model.todos_model import TodosModel

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        page.on_route_change = self.on_route_change
        self.todos_model=TodosModel()

        page.navigation_bar = ft.CupertinoNavigationBar(
            selected_index=0,
            on_change=self.on_nav_change, 
            bgcolor=ft.Colors.BLUE_100,
            inactive_color=ft.Colors.BLUE_GREY_600,
            active_color=ft.Colors.BLACK,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.CHECKLIST_RTL,
                    label="ToDos",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.EDIT_NOTE_ROUNDED,
                    label="Mein Studium",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icons.SETTINGS,
                    label="Settings",
                ),
            ],
        )

    def on_route_change(self, e: ft.RouteChangeEvent):
        self.page.clean()
        if self.page.route == "/meinStudium":
            self.page.add(MeinStudiumView())
        elif self.page.route == "/Todo":
            self.page.add(TodosView(self))
        elif self.page.route == "/Einstellungen":
            self.page.add(EinstellungenView())
        elif self.page.route == "/erzeugeTodo":
            self.page.add(ErzeugeTodoView(self)) 
        elif self.page.route == "/filtereTodo":
            self.page.add(FiltereTodoView()) 


    def on_nav_change(self, e:ft.ControlEvent):
        index = e.control.selected_index

        if index == 0:
            if isinstance(self.page, ft.Page):
                self.page.go("/Todo")

        elif index == 1:
            if isinstance(self.page, ft.Page):
                self.page.go("/meinStudium")
        
        elif index == 2:
            if isinstance(self.page, ft.Page):
                self.page.go("/Einstellungen")

        self.page.update()

    def go_to_erzeuge_todo(self):
        self.page.go ("/erzeugeTodo")

    def go_to_todos(self):
        self.page.go ("/Todo") #mit Index machen?

    def go_to_filtere_todo(self):
        self.page.go ("/filtereTodo")
