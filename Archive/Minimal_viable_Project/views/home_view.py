import flet as ft
from .base_view import BaseView


class HomeView(BaseView):
    def build(self):
        return ft.Column([ft.Text("Home View — Platzhalter")], spacing=10)
