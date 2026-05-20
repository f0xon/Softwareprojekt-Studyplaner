# pyright: reportUnknownMemberType=false
import flet as ft

#Für elemente die überalle in der App verwendet werden können, z.B. die AppBar, BottomAppBar, etc.

class Standard(ft.Column):
    def __init__(self):
        super().__init__(spacing=16, horizontal_alignment=ft.CrossAxisAlignment.START)
        self.controls =[]
