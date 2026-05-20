# pyright: reportUnknownMemberType=false
import flet as ft
from .TodoView import TodoView
from .addingTodoView import addingTodoView

class Navigator:
    page: ft.Page

    def __init__(self, page: ft.Page):
        self.page = page
        page.on_route_change = self.on_route_change
        page.go("/Todo")

    def on_route_change(self):
        self.page.clean()
        if self.page.route == "/Todo":
            self.page.add(TodoView())
        elif self.page.route == "/addingTodo":
            self.page.add(addingTodoView())

#Beispeil für Viewchange:

    # def on_button_click(self, e: ft.Event[ft.Button]):
    #     if isinstance(self.page, ft.Page):
    #         self.page.go("/kevin")