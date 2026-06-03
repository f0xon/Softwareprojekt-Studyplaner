# pyright: reportAttributeAccessIssue=false
import flet as ft

class NavigationBarView:
    def __init__(self, router):
        self.router = router

    def build(self):
        return ft.CupertinoNavigationBar(
            selected_index=0,
            on_change=self.router.on_nav_change,
            bgcolor=ft.Colors.BLUE_100,
            inactive_color=ft.Colors.BLUE_GREY_600,
            active_color=ft.Colors.BLACK,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.ADD, label="ADD"),
                ft.NavigationBarDestination(icon=ft.Icons.CHECKLIST_RTL, label="ToDos"),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS_OUTLINED, label="Settings"),
            ],
        )