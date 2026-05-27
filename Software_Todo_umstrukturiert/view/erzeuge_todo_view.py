# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.erzeuge_todo_presenter import ErzeugeTodoPresenter

class ErzeugeTodoView(ft.Column):
    def __init__(self,router):
        super().__init__()
        self.router=router
        self.presenter = ErzeugeTodoPresenter(router)

        self.title = ft.TextField(label="Titel")
        self.deadline = ft.TextField(label="Fälligkeit")
        self.category = ft.TextField(label="Kategorie")

        self.controls.append(
        ft.Card(
            bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
            shadow_color=ft.Colors.ON_SURFACE_VARIANT,
            content=ft.Container(
                width=450,
                padding=10,
                content=ft.Column([
                    ft.Row([
                            ft.Text("Titel:"),
                            ft.Container(expand=True),  # füllt den Platz
                            self.title
                        ]),
                    ft.Row([
                            ft.Text("Fälligkeit:"),
                            ft.Container(expand=True),
                            self.deadline
                    ]),
                    ft.Row([
                        ft.Text("Kalender"),
                        ft.Container(expand=True), 
                        ft.RadioGroup(content=ft.Row([   #ja nein --> Radiobutton nur eins ankreuzen!!
                            ft.Radio(value="ja", label="Ja"),
                            ft.Radio(value="nein", label="Nein"),
                        ])),
                        ft.Container(expand=True) 
                    ]),
                    ft.Row([
                            ft.Text("Kategorie:"),
                            ft.Container(expand=True),
                            self.category
                            ]),
                    ft.Row([ft.ElevatedButton(content=ft.Text("Speichern"),on_click=self.save)])
                    ])
                ),
            ),
        )

    def save(self, e):
        self.presenter.save_todo(self.title.value, self.deadline.value, self.category.value)  
