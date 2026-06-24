# pyright: ignore[reportArgumentType]
# from typing import Any

import flet as ft

# from model.todo_model import ToDoModel, Priority, hoch, mittel, niedrig, keine_p, Category, studium, haushalt, freizeit
from model.todo_model import ToDo
from view.todo_view import TodoView
from view.filtere_todo_view import FiltereTodoView
from view.navigationBar_view import NavigationBarView
from view.erzeuge_todo_view import ErzeugeTodoView
from presenter.todo_presenter import TodoListePresenter
from presenter.erzeuge_todo_presenter import TodoDetailPresenter
from presenter.filtere_todo_presenter import FiltereTodoPresenter
from repo.todo_memory_repo import InMemoryTodoRepo
# from repo.todo_mongo_repo import MongoTodoRepo
# from repo.todo_repo import TodoRepo
# from pymongo import MongoClient
# from pymongo.database import Database

DB_URL = "mongodb+srv://cluster0.9w2gjme.mongodb.net"
DB_USER = "soen_labor"
DB_PASSWORD = "6HQgiBWd7IDAXa6g"
DB_NAME = "soen_vorlesung"


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.todo: str = "/Todo"
        self.erzeuge_todo: str = "/erzeugeTodo"
        self.filtere_todo: str = "/filtereTodo"
        self.page.navigation_bar = NavigationBarView(self).build()

        page.on_route_change = self.on_route_change

        # Repo erzeugen und an Presenter übergeben
        # db: Database[Any] = MongoClient(                               #TODO Fragen wegen Type # type: ignore
        #     DB_URL, username=DB_USER, password=DB_PASSWORD
        # ).get_database(DB_NAME)
        # self.repo_mongo = MongoTodoRepo(db)
        self.repo_memory = InMemoryTodoRepo()
        # wähle hier dein gewünschtes Repo aus:
        self.ausgewaehltes_repo = self.repo_memory

        # Presenter hier erzeugen
        self.presenter_todo = TodoListePresenter(self.ausgewaehltes_repo)
        self.presenter_detail = TodoDetailPresenter(self.ausgewaehltes_repo)
        self.presenter_filtern = FiltereTodoPresenter(self.ausgewaehltes_repo)

        self.navigation: dict[int, str] = {
            0: self.erzeuge_todo,
            1: self.todo,
            2: self.filtere_todo,
        }

        self.page.on_route_change = self.on_route_change

        self.page.navigation_bar = NavigationBarView(self).build()

    def on_route_change(self):

        self.page.clean()
        if self.page.route == self.todo:
            self.page.add(
                TodoView(
                    self.presenter_todo, self.presenter_filtern, self.presenter_detail
                )
            )

        elif self.page.route.startswith(self.erzeuge_todo):
            if "?" in self.page.route:
                self.lade_todo_aus_route()
            else:
                self.presenter_detail.set_modus("create")
            self.page.add(ErzeugeTodoView(self.presenter_detail))

        elif self.page.route == self.filtere_todo:
            self.page.add(FiltereTodoView(self.presenter_filtern))

        else:
            self.page.go(self.todo)

        self.page.update()

    def lade_todo_aus_route(self) -> None:
        self.presenter_detail.set_modus("edit")
        query = self.page.route.split("?")[1]
        items = query.split("&")
        values: dict[str, str] = {}
        for item in items:
            key, value = item.split("=")
            values[key] = value
        if "id" in values:
            todo_id = int(values["id"])
            self.presenter_detail.lade_todo(todo_id)

    def on_nav_change(self, e: ft.ControlEvent):
        index: int = e.control.selected_index
        route = self.navigation.get(index)
        if route:
            if isinstance(self.page, ft.Page):  # pyright: ignore[reportUnnecessaryIsInstance]
                self.page.go(route)

    def go_to_todos(self):
        self.page.go(self.todo)
