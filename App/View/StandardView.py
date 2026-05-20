# pyright: reportUnknownMemberType=false
import flet as ft

#Für elemente die überalle in der App verwendet werden können, z.B. die AppBar, BottomAppBar, etc.

class Standard(ft.Column):
    def __init__(self):
        super().__init__(spacing=16, horizontal_alignment=ft.CrossAxisAlignment.START)
        self.controls =[]
        
    #     ft.Pagelet(
    #     navigation_bar=ft.CupertinoNavigationBar(
    #         bgcolor=ft.Colors.BLUE_100,
    #         inactive_color=ft.Colors.BLUE_GREY_600,
    #         active_color=ft.Colors.BLACK,
    #         on_change=lambda e: self.selected_index(e.control.selected_index),
    #         destinations=[
    #             ft.NavigationBarDestination(icon=ft.Icons.CHECKLIST_RTL, label="ToDos",),               #index 0
    #             ft.NavigationBarDestination(icon=ft.Icons.EDIT_NOTE_ROUNDED, label="Mein Studium",),    #index 1
    #             ft.NavigationBarDestination(
    #                 icon=ft.Icons.SETTINGS_OUTLINED,
    #                 selected_icon=ft.Icons.SETTINGS,
    #                 label="Settings",
    #             ),  #index 2
    #         ],
    #     ),
    #     content=ft.Container(),
    #     height=200,
    #     )

    # def selected_index(self, index: int):
    #     if index == 0:
    #         if isinstance(self.page, ft.Page):
    #             self.page.go("/Todo")
    #     elif index == 1:
    #         ft.Text("Selected index: Mein Studium ist ncoh nicht implementiert")
    #     elif index == 2:
    #         ft.Text("Selected index: Settings ist ncoh nicht implementiert")




    