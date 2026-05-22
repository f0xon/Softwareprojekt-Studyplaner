# pyright: reportUnknownMemberType=false
import flet as ft
from .StandardView import Standard

class addingTodoView(Standard):

# Standard Werte für Eingabefelder für die Eingabe eines neuen Todos
    Titel: str = ""
    Fälligkeit: str = "18.05.2026"
    Kalender: str = ""
    Erinnerung: str = ""
    Bemerkung: str = ""
    Kategorie: str = ""



    def __init__(self):
        super().__init__()

    def did_mount(self):
        
         #pop up Fenster implementieren
        self.controls.append(
            ft.Card(
                bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                content=ft.Container(
                    width=450,
                    padding=10,
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Titel:"),
                                    ft.Container(expand=True),  # füllt den Platz
                                    ft.TextField(
                                        value=self.Titel,
                                    ),
                                ]
                            ),
                            ft.Row([
                                    ft.Text("Fälligkeit:"),
                                    ft.Container(expand=True),  # füllt den Platz
                                    ft.TextField(
                                        value=self.Fälligkeit,
                                    ),
                            ]),

                            ft.Row([
                                ft.Text("Kalender"),
                                ft.Container(expand=True),  # füllt den Platz
                                ft.Checkbox(label="Ja"),
                                ft.Checkbox(label="Nein"),  #ja nein check boxen
                                ft.Container(expand=True)  # füllt den Platz
                            ]),

                            ft.Row([
                                    ft.Text("Erinnerung:"),
                                    ft.Container(expand=True),  # füllt den Platz
                                    ft.TextField(
                                        value=self.Erinnerung,

                                    ),
                                    ]),
                            ft.Row([
                                    ft.Text("Bemerkung:"),
                                    ft.Container(expand=True),  # füllt den Platz
                                    ft.TextField(
                                        value=self.Bemerkung,
                                    ),
                                    ]),
                            ft.Row([
                                    ft.Text("Kategorie:"),
                                    ft.Container(expand=True),  # füllt den Platz
                                    ft.TextField(
                                        value=self.Kategorie,
                                    ),
                                    ]),
                        ]
                    )
                    ),
                ),
            )