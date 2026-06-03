# pyright: reportAttributeAccessIssue=false
import datetime
import flet as ft
from presenter.erzeuge_todo_presenter import ErzeugeTodoPresenter


class ErzeugeTodoView(ft.Column):
    def __init__(self, router):
        super().__init__()

        self.router = router
        self.presenter = ErzeugeTodoPresenter(router)
        self.selected_date=datetime.datetime.now()


        # Eingabefelder
        self.title = ft.TextField(label="Titel")

        self.deadline=ft.Button(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: e.control.page.show_dialog(
                ft.DatePicker(
                    first_date=datetime.datetime(2023, 10, 1),
                    last_date=datetime.datetime(2026, 12, 1),
                    value=self.selected_date,
                    on_change=self.date_changed,
                )
            )
        )

        # self.deadline = ft.DatePicker(
        #     first_date=datetime.datetime(2023, 10, 1),
        #     last_date=datetime.datetime(2026, 12, 1),
        #     value=self.selected_date,
        #     on_change=self.date_changed,
        #             )

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
                                    ft.Text(self.selected_date),
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Kalender (noch zu implementieren)"),
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
    def date_changed(self, e):
        self.selected_date=e.control.value

    def save(self, e)->None:
        self.presenter.save_todo(self.title.value, self.selected_date, self.category.value)  
