# pyright: ignore[reportArgumentType]
from typing import Callable

import flet as ft

from view.erzeuge_todo_view import ErzeugeTodoView
from view.todos_view import TodosView
from view.filtere_todo_view import FiltereTodoView
from view.navigationBar_view import NavigationBarView
from view.erzeuge_todo_freizeit_view import ErzeugeTodoFreizeitView
from view.erzeuge_todo_privat_view import ErzeugeTodoPrivatView
from view.erzeuge_todo_studium_view import ErzeugeTodoStudiumView

from model.todos_model import TodosModel

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.todos_model=TodosModel() #für model erzeuge todo model
        self.todo:str="/Todo"
        self.erzeuge_todo:str="/erzeugeTodo"
        self.filtere_todo:str="/filtereTodo"

        page.on_route_change = self.on_route_change

        self.page.navigation_bar = NavigationBarView(self).build()

        self.routes:dict[str,Callable[[], ft.Column]]={ #richtiges Typing?
            self.todo: lambda:TodosView(self), #lamda definiert Minifunktionen
            self.erzeuge_todo: lambda: ErzeugeTodoView(self),
            self.filtere_todo: lambda: FiltereTodoView(),
            self.todo_freizeit: lambda: ErzeugeTodoFreizeitView(),
            self.todo_privat: lambda: ErzeugeTodoPrivatView(),
            self.todo_studium: lambda: ErzeugeTodoStudiumView()
            #self.filtered_todos: lambda: TodosView() #noch nicht implementiert
        }

        self.navigation:dict[int, str]={
            0:self.erzeuge_todo,
            1:self.todo,
            2:self.filtere_todo
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
            if isinstance(self.page, ft.Page): # pyright: ignore[reportUnnecessaryIsInstance]
                self.page.go(route)

    # def go_to_erzeuge_todo(self):
    #     self.page.go (self.erzeuge_todo)

    def go_to_todos(self):
        self.page.go (self.todo) #mit Index machen?

    # def go_to_filtere_todo(self):
    #     self.page.go (self.filtere_todo)

    def go_to_Filterted_todos(self):
        self.page.go (self.filtere_todo)

    def go_to_erzeuge_todo_view(self,kategorie:str):
        self.page.go (kategorie)