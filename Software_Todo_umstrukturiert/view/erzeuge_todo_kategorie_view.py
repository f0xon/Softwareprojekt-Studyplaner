# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.erzeuge_todo_kategorie_presenter import ErzeugeTodoKategoriePresenter

class ErzeugeTodoKategorieView(ft.Column):
    def __init__(self):
        super().__init__()
        self.presenter=ErzeugeTodoKategoriePresenter()

        # Dropdown Kategorie
        self.category = ft.Dropdown(
            value="keine",
            options=[
                ft.dropdown.Option("keine"),
                ft.dropdown.Option("Studium"),
                ft.dropdown.Option("Arbeit"),
                ft.dropdown.Option("Freizeit"),
            ],
            on_text_change=self.set_dropdownvalue,
        )

        # UI 
        self.controls.append(
            ft.Card(
                bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                content=ft.Container(
                    width=450,
                    padding=10,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("Kategorie:"),
                                    ft.Container(expand=True),
                                    self.category,
                                ]
                            ),
                        ]
                    ),
                ),
            )
        )

    def set_dropdownvalue(self,e: ft.ControlEvent):
        value=e.control.value
        presenter.erzeuge_todo_view(self,kategorie=value)

        