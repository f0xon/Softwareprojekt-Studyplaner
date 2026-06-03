import flet as ft


class BaseView:
    """Simple base view class. Subviews should inherit this and implement `build()`.

    Keeps a reference to the `page` so subviews can access it later.
    """

    def __init__(self, page: ft.Page):
        self.page = page

    def build(self) -> ft.Control:
        return ft.Column([ft.Text("Base View")])
