# pyright: reportAttributeAccessIssue=false
import datetime
from typing import Protocol
import flet as ft
from presenter.erzeuge_todo_presenter import ErzeugeTodoPresenter

class Kategorie(Protocol):
    def build_ui(self) -> list[ft.Row]:
        ...

class StudiumKategorie:
    def build_ui(self)->list[ft.Row]:
        return [
            ft.Row(
                controls=[
                    ft.Text("Modul:"),
                    ft.Container(expand=True),
                    ft.TextField(label="Modul"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Text("Gruppenarbeit:"),
                    ft.Container(expand=True),
                    ft.RadioGroup(
                        value="nein",
                        content=ft.Row(
                            controls=[
                                ft.Radio(value="ja", label="Ja"),
                                ft.Radio(value="nein", label="Nein"),
                            ]
                        )
                    )
                ]
            )
        ]

class HaushaltKategorie:
    def build_ui(self)->list[ft.Row]:
        return [
            ft.Row(
                controls=[
                    ft.Text("wiederkehrende Aufgabe:"),
                    ft.Container(expand=True),
                    ft.RadioGroup(
                        value="nein",
                        content=ft.Row(
                            controls=[
                                ft.Radio(value="ja", label="Ja"),
                                ft.Radio(value="nein", label="Nein"),
                            ]
                        )
                    )
                ]
            )
        ]
    
class FreizeitKategorie:
    def build_ui(self)->list[ft.Row]:
        return [
            ft.Row(
                controls=[
                    ft.Text("Hobby:"),
                    ft.Container(expand=True),
                    ft.TextField(label="Hobby"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Text("Ort:"),
                    ft.Container(expand=True),
                    ft.TextField(label="Ort"),
                ]
            ),
        ]


class ErzeugeTodoView(ft.Column):
    def __init__(self):
        super().__init__()
        self.presenter = ErzeugeTodoPresenter()
        # use date (no time) to match DatePicker value type
        self.selected_date = datetime.date.today()

        self.category_fields=ft.Column()
        self.kategorien:dict[str,Kategorie] = {
            "Studium": StudiumKategorie(),
            "Haushalt": HaushaltKategorie(),
            "Freizeit": FreizeitKategorie()
        }

        # Eingabefelder
        self.title = ft.TextField(label="Titel")

        self.notiz=ft.TextField(label="Notiz")

        self.deadline_text=ft.Text(str(self.selected_date))
        self.deadline=ft.Button(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: e.control.page.show_dialog(
                ft.DatePicker(
                    first_date=datetime.date(2026, 1, 1),
                    last_date=datetime.date(2028, 12, 1),
                    value=self.selected_date,
                    on_change=self.date_changed,
                )
            )
        )

        self.category = ft.RadioGroup(
            value="keine",
            content=ft.Row([
                ft.Radio(value="keine", label="Keine"),
                ft.Radio(value="Studium", label="Studium"),
                ft.Radio(value="Haushalt", label="Haushalt"),
                ft.Radio(value="Freizeit", label="Freizeit"),
            ]),
            on_change=self.category_changed
        )

        # RadioGroup Kalender
        self.calendar = ft.RadioGroup(
            value="nein",
            content=ft.Row(
                controls=[
                    ft.Radio(value="ja", label="Ja"),
                    ft.Radio(value="nein", label="Nein"),
                ]
            )
        )

        self.prio=ft.Dropdown(
            value="keine",
            options=[
                ft.dropdown.Option("keine"),
                ft.dropdown.Option("niedrig"),
                ft.dropdown.Option("mittel"),
                ft.dropdown.Option("hoch"),
            ],
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
                                    ft.Text("Notiz:"),
                                    ft.Container(expand=True),
                                    self.notiz,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Fälligkeitsdatum:"),
                                    ft.Container(expand=True),
                                    self.deadline,
                                    self.deadline_text,
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
                                    ft.Text("Priorität:"),
                                    ft.Container(expand=True),
                                    self.prio,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Kategorie:"),
                                    ft.Container(expand=True),
                                    self.category,
                                ]
                            ),
                            self.category_fields,
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
        # value from DatePicker event is a date
        self.selected_date = e.control.value.date()
        self.deadline_text.value=str(self.selected_date)
        self.update()
        #return self.selected_date 

    def category_changed(self,e)->None:
        self.category_fields.controls.clear()
        kat = self.kategorien.get(self.category.value)
        if kat:
            self.category_fields.controls.extend(kat.build_ui())
        self.update()


    # def save(self, e) -> None:
    #     self.presenter.save_todo(self.title.value, self.selected_date, self.calendar.value, self.prio.value, self.category.value)

    def save(self, e) -> None:
        kat = self.kategorien.get(self.category.value)

        if kat:
            extra = kat.extract(self) 
        else:
            extra = {}

        try:
            todo = self.presenter.save_todo(
                title=self.title.value,
                deadline=self.selected_date,
                calendar=self.calendar.value,
                priority=self.prio.value,
                category=self.category.value,
                extra=extra
            )

            print("Gespeichert:", todo)

        except ValueError as ex:
            print("Fehler:", ex)  

    # Dropdown Kategorie
    # self.category = ft.Dropdown(
    #     value="keine",
    #     options=[
    #         ft.dropdown.Option("keine",on_click=self.category_changed),
    #         ft.dropdown.Option("Studium",on_click=self.category_changed),
    #         ft.dropdown.Option("Haushalt",on_click=self.category_changed),
    #         ft.dropdown.Option("Freizeit",on_click=self.category_changed),
    #     ],
    #     #on_change=self.category_changed
    # )
    # self.category.on_change = self.category_changed