
import flet as ft

class FletNavigator:
    page: ft.Page

    def __init__(self, page: ft.Page):
        self.page = page
        page.on_route_change = self.on_route_change
        page.go("/bob")

    def on_route_change(self):
        self.page.clean()
        if self.page.route == "/bob":
            self.page.add(BobView())
        elif self.page.route == "/kevin":
            self.page.add(KevinView())

#Beispeil für Viewchange:

    # def on_button_click(self, e: ft.Event[ft.Button]):
    #     if isinstance(self.page, ft.Page):
    #         self.page.go("/kevin")