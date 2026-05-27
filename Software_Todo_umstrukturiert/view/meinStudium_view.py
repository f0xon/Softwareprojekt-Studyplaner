# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import flet as ft

class MeinStudiumView(ft.Column):

    def __init__(self):
        super().__init__()
        self.controls.append(ft.Text("Mein Studium"))