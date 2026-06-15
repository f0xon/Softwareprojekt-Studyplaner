# pyright: reportAttributeAccessIssue=false
from datetime import datetime
from datetime import date
from zoneinfo import ZoneInfo
from typing import Any, Protocol
import flet as ft
from presenter.erzeuge_todo_presenter import TodoDetailPresenter
from view.todo_view import TodoView

class Kategorie(Protocol):
    def build_ui(self) -> list[ft.Row]:
        ...
    def extract(self) -> dict[str,Any]:
        ...

class StudiumKategorie:
    def __init__(self):
        self.modul=ft.TextField(label="Modul")
        self.gruppenarbeit=ft.RadioGroup(
            value=False,
            content=ft.Row(
                controls=[
                    ft.Radio(value=True, label="Ja"),
                    ft.Radio(value=False, label="Nein"),
                ]
            )
        )

    def build_ui(self)->list[ft.Row]:
        return [
            ft.Row(
                controls=[
                    ft.Text("Modul:"),
                    ft.Container(expand=True),
                    self.modul,
                ]
            ),
            ft.Row(
                controls=[
                    ft.Text("Gruppenarbeit:"),
                    ft.Container(expand=True),
                    self.gruppenarbeit
                ]
            )
        ]
    def extract(self) -> dict[str,Any]:
        return {
            "modul": self.modul.value,
            "gruppenarbeit": self.gruppenarbeit.value
        }

class HaushaltKategorie:
    def __init__(self):
        self.wiederkehrend=ft.RadioGroup(
            value=False,
            content=ft.Row(
                controls=[
                    ft.Radio(value=True, label="Ja"),
                    ft.Radio(value=False, label="Nein"),
                ]
            )
        )

    def build_ui(self)->list[ft.Row]:
        return [
            ft.Row(
                controls=[
                    ft.Text("wiederkehrende Aufgabe:"),
                    ft.Container(expand=True),
                    self.wiederkehrend
                ]
            )
        ]

    def extract(self) -> dict[str,Any]:
        return {
            "wiederkehrend":self.wiederkehrend.value
        }
    
class FreizeitKategorie:
    def __init__(self):
        self.hobby=ft.TextField(label="Hobby")
        self.ort=ft.TextField(label="Ort")

    def build_ui(self)->list[ft.Row]:
        return [
            ft.Row(
                controls=[
                    ft.Text("Hobby:"),
                    ft.Container(expand=True),
                    self.hobby
                ]
            ),
            ft.Row(
                controls=[
                    ft.Text("Ort:"),
                    ft.Container(expand=True),
                    self.ort,
                ]
            ),
        ]
    def extract(self) -> dict[str,Any]:
        return {
            "hobby":self.hobby.value,
            "ort":self.ort.value
        }

#wenn todo dann zeige todo mit lade_detail_todo wenn nicht erstelle neues todo
class ErzeugeTodoView(ft.Column):
    def __init__(self, presenter:TodoDetailPresenter):
        super().__init__()
        self.presenter = presenter
        #self.on_save=on_save
        self.selected_date = date.today()

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
                    first_date=date(2026, 1, 1),
                    last_date=date(2028, 12, 1),
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
            content=ft.Row([
                    ft.Radio(value=True, label="Ja"),
                    ft.Radio(value=False, label="Nein"),
                ])
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
        self.lade_ui()
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
        value = e.control.value

        if isinstance(value, datetime):
            value = value.astimezone(ZoneInfo("Europe/Berlin")).date()
        elif isinstance(value, dt.date):
            value = value 
        
        self.deadline = value 
        self.deadline_text.value = self.deadline.strftime("%d.%m.%Y")

        self. update()
        #return self.selected_date 

    def category_changed(self,e)->None:
        self.category_fields.controls.clear()
        kat = self.kategorien.get(self.category.value)
        if kat:
            self.category_fields.controls.extend(kat.build_ui())
        self.update()

    # ---------------- LOAD INTO VIEW ----------------
    def lade_ui(self, todo_id: int | None = None):
        data = self.presenter.lade_todo(todo_id) if todo_id else {}

        self.title.value = data.get("Titel", "")
        self.notiz.value = data.get("Notiz", "")
        self.selected_date = data.get("Deadline", self.selected_date)
        self.calendar.value = data.get("Kalender", False)
        self.prio.value = data.get("Priorität", "keine")
        self.category.value = data.get("Kategorie", "keine")
        #Kategorienspezifische Extrafelder fehlen noch

    # ---------------- SAVE ----------------
    def save(self, e):
        kat:str|None=self.category.value
        aktuelle_kat = self.kategorien.get(kat,"")
        if aktuelle_kat:
            extra:dict[str,Any] = aktuelle_kat.extract()
        else:
            extra = {}
        self.presenter.save_todo(
            titel=self.title.value,
            notiz=self.notiz.value,
            deadline=self.selected_date,
            calendar=self.calendar.value,
            priority=self.prio.value,
            category=kat,
            extra=extra,
        )

        #if self.on_save:
        #   self.on_save()

    # def zeige_detail_todo(self):
    #     dict_todo:dict[str,Any]|None=self.presenter.get_current_todo_data()
    #     self.title.value = dict_todo.get("Titel")
    #     self.notiz.value = dict_todo.get("Notiz")
    #     self.selected_date= dict_todo.get("Deadline")
    #     self.calendar.value = dict_todo.get("Kalender")
    #     self.prio.value = dict_todo.get("Priorität")
    #     self.category.value = dict_todo.get("Kategorie")
    #     category:str=dict_todo.get("Kategorie")
    #     #Kategorien-spezifische Felder
    #     if category == "Studium":
    #         self.modul=...
    #         self.gruppenarbeit=...
    #     elif category == "Haushalt":
    #         self.wiederkehrend=...
    #     elif category == "Freizeit":
    #         self.hobby=...
    #         self.ort=...

    # def save(self, e) -> None:
    #     kat=self.category.value
    #     aktuelle_kat = self.kategorien.get(kat)
    #     if aktuelle_kat:
    #         extra:dict[str,Any] = aktuelle_kat.extract()
    #     else:
    #         extra = {}
    #     self.presenter.save_todo(
    #         title=self.title.value,
    #         notiz=self.notiz.value,
    #         deadline=self.selected_date,
    #         calendar=self.calendar.value,
    #         priority=self.prio.value,
    #         category=kat,
    #         extra=extra,
    #     )
