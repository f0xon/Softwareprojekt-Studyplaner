# pyright: reportAttributeAccessIssue=false
import flet as ft

class FiltereTodoView(ft.Column):
    def __init__(self):
        super().__init__()

        self.status_value = "offen"
        self.kategorie_value = "keine"
        self.datum_value = "nach Deadline neueste zuerst"

        self.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Fälligkeit"),
                    ft.Dropdown(
                        value=self.status_value,
                        options=[
                            ft.DropdownOption("alle"),
                            ft.DropdownOption("offen"),
                            ft.DropdownOption("erledigt"),
                        ],
                    ),

                    ft.Text("Kategorie"),
                    ft.Dropdown(
                        value=self.kategorie_value,
                        options=[
                            ft.DropdownOption("keine"),
                            ft.DropdownOption("Studium"),
                            ft.DropdownOption("Arbeit"),
                            ft.DropdownOption("Freizeit"),
                        ],
                    ),

                    ft.Text("Datum"),
                    ft.Dropdown(
                        value=self.datum_value,
                        options=[
                            ft.DropdownOption("nach Deadline neueste zuerst"),
                            ft.DropdownOption("älteste zuerst"),
                            ft.DropdownOption("nach Erstellungsdatum"),
                        ],
                    ),

                    ft.Button("Filtern") #Button noch nicht anklickbar
                ]
            )
        )