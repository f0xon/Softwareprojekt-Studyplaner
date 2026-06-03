# pyright: ignore[reportArgumentType]
from typing import Callable

import flet as ft

from view.einstellungen_view import EinstellungenView
from view.erzeuge_todo_view import ErzeugeTodoView
from view.meinStudium_view import MeinStudiumView
from view.todos_view import TodosView
from view.filtere_todo_view import FiltereTodoView
from view.navigationBar_view import NavigationBarView

from model.todos_model import TodosModel

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.todos_model=TodosModel() #für model erzeuge todo model
        self.todo:str="/Todo"
        self.studium:str="/meinStudium"
        self.einstellungen:str="/Einstellungen"
        self.erzeuge_todo:str="/erzeugeTodo"
        self.filtere_todo:str="/filtereTodo"

        page.on_route_change = self.on_route_change

        self.page.navigation_bar = NavigationBarView(self).build()

        self.routes:dict[str,Callable[[], ft.Column]]={ #richtiges Typing?
            self.todo: lambda:TodosView(self), #lamda definiert Minifunktionen
            self.studium: lambda: MeinStudiumView(), #auch möglich MeinStudiumView()
            self.einstellungen: lambda:EinstellungenView(),
            self.erzeuge_todo: lambda: ErzeugeTodoView(self),
            self.filtere_todo: lambda: FiltereTodoView(),
            self.filtered_todos: lambda: TodosView() #noch nicht implementiert
        }

        self.navigation:dict[int, str]={
            0:self.todo,
            1:self.studium,
            2:self.einstellungen
        }

    def on_route_change(self, e: ft.RouteChangeEvent):
        self.page.clean()
        erzeuge_view=self.routes.get(self.page.route)
        if erzeuge_view: #nur wenn eintrag im dict vorhanden ist
            self.page.add(erzeuge_view())
        self.page.update()
    
    def on_nav_change(self, e:ft.ControlEvent):
        index:int = e.control.selected_index
        route=self.navigation.get(index)
        if route:
            if isinstance(self.page, ft.Page):
                self.page.go(route)

    def go_to_erzeuge_todo(self):
        self.page.go (self.erzeuge_todo)

    def go_to_todos(self):
        self.page.go (self.todo) #mit Index machen?

    def go_to_filtere_todo(self):
        self.page.go (self.filtere_todo)

    def go_to_Filterted_todos(self):
        self.page.go (self.filtere_todo)

    # page.navigation_bar = ft.CupertinoNavigationBar(
    #     selected_index=0,
    #     on_change=self.on_nav_change, 
    #     bgcolor=ft.Colors.BLUE_100,
    #     inactive_color=ft.Colors.BLUE_GREY_600,
    #     active_color=ft.Colors.BLACK,
    #     destinations=[
    #         ft.NavigationBarDestination(
    #             icon=ft.Icons.CHECKLIST_RTL,
    #             label="ToDos",
    #         ),
    #         ft.NavigationBarDestination(
    #             icon=ft.Icons.EDIT_NOTE_ROUNDED,
    #             label="Mein Studium",
    #         ),
    #         ft.NavigationBarDestination(
    #             icon=ft.Icons.SETTINGS_OUTLINED,
    #             selected_icon=ft.Icons.SETTINGS,
    #             label="Settings",
    #         ),
    #     ],
    # )

    #def on_route_change (self, e: ft.RouteChangeEvent):
        # if self.page.route == "/meinStudium":
        #     self.page.add(MeinStudiumView())
        # elif self.page.route == "/Todo":
        #     self.page.add(TodosView(self))
        # elif self.page.route == "/Einstellungen":
        #     self.page.add(EinstellungenView())
        # elif self.page.route == "/erzeugeTodo":
        #     self.page.add(ErzeugeTodoView(self)) 
        # elif self.page.route == "/filtereTodo":
        #     self.page.add(FiltereTodoView()) 
    # def on_nav_change(self, e:ft.ControlEvent):
        # index:int = e.control.selected_index
        # if index == 0:
        #     if isinstance(self.page, ft.Page):
        #         self.page.go("/Todo")

        # elif index == 1:
        #     if isinstance(self.page, ft.Page):
        #         self.page.go("/meinStudium")
        
        # elif index == 2:
        #     if isinstance(self.page, ft.Page):
        #         self.page.go("/Einstellungen")

        # self.page.update()
