# pyright: reportAttributeAccessIssue=false

import flet as ft
import datetime
from presenter.erzeuge_todo_presenter import ErzeugeTodoPresenter


class ErzeugeTodoView(ft.Column):
    def __init__(self, router):
        super().__init__()
        
        self.router = router
        self.presenter = ErzeugeTodoPresenter(router)

        # Eingabefelder
        self.title = ft.TextField(label="Titel")
        self.deadline = ft.TextField(label="Fälligkeit")

        # Dropdown Kategorie
        self.category = ft.Dropdown(
            value="keine",
            options=[
                ft.dropdown.Option("keine"),
                ft.dropdown.Option("Studium"),
                ft.dropdown.Option("Arbeit"),
                ft.dropdown.Option("Freizeit"),
            ],
        )

        # RadioGroup Kalender
        self.calendar = ft.RadioGroup(
            content=ft.Row(
                controls=[
                    ft.Radio(value="ja", label="Ja"),
                    ft.Radio(value="nein", label="Nein"),
                ]
            )
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
                                    ft.Text("Titel:"),
                                    ft.Container(expand=True),
                                    self.title,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Fälligkeit:"),
                                    ft.Container(expand=True),
                                    self.deadline,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Kalender"),
                                    ft.Container(expand=True),
                                    self.calendar,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Kategorie:"),
                                    ft.Container(expand=True),
                                    self.category,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Button("Speichern",on_click=self.save)
                                ]
                            ),
                        ]
                    ),
                ),
            )
        )

    def save(self, e):
        self.presenter.save_todo(self.title.value, self.deadline.value, self.category.value)  
