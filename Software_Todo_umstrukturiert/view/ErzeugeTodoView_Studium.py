# pyright: reportAttributeAccessIssue=false
from erzeuge_todo_view import ErzeugeTodoView
import datetime
import flet as ft

class ErzeugeTodoView_Studuium(ErzeugeTodoView):
    def __init__(self, router):
        super().__init__(router)
        self.category.value = "Studium"
        self.fach = ft.TextField()
        self.dozent = ft.TextField()
        self.raum = ft.TextField()
        self.abgebedatum = ft.DatePicker()


        self.selected_date = datetime.date.today()
        self.controls.append(
            ft.Column(
                controls = [
                    ft.Row(
                        controls=[
                            ft.Text("Fach:"),
                            ft.Container(expand=True),
                            self.fach,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("dozent:"),
                            ft.Container(expand=True),
                            self.dozent,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Raum:"),
                            ft.Container(expand=True),
                            self.raum,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Abgabedatum:"),
                            ft.Container(expand=True),
                            self.deadline,
                            ft.Text(str(self.selected_date)),
                        ]
                    )
                ]
            )
        )

    def date_changed(self, e):
        # value from DatePicker event is a date
        self.selected_date = e.control.value

    def save(self, e)->None:
        self.presenter.save_todo(self.title.value, self.selected_date, self.category.value, self.fach, self.dozent, self.raum, self.abgebedatum)  
