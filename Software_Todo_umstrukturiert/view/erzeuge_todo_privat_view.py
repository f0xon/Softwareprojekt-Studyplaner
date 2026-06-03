import flet as ft

class ErzeugeTodoPrivatView(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls.append(ft.Text("Hallo"))