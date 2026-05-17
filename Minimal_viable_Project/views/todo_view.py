import flet as ft
from .base_view import BaseView


class TodoView(BaseView):
    def build(self):
        return ft.Column(
            [
                ft.Text("Todo-Liste"),
                ft.Checkbox(label="todo1"),
                ft.Checkbox(label="todo2"),
                ft.Checkbox(label="todo3"),
            ],
            spacing=8,
            alignment=ft.MainAxisAlignment.START,
        )
