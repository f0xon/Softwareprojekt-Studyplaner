import flet as ft
from .base_view import BaseView


class SettingsView(BaseView):
    def build(self):
        return ft.Column([ft.Text("Settings — Platzhalter")], spacing=8)
