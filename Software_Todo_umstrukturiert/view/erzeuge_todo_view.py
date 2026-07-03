# pyright: reportAttributeAccessIssue=false
from datetime import datetime
from datetime import date
from zoneinfo import ZoneInfo
from typing import Any, Protocol
import flet as ft
from model.todo_model import (
    Freizeit,
    Haushalt,
    Studium,
)  
from presenter.erzeuge_todo_presenter import TodoDetailPresenter

#Betz: Müssen die Klassen Kategorie, StudiumKategorie, Haushaltkategorie und PrivatKategorie in eine eigene Datei?
class KategorieView(Protocol):
    def build_ui(self) -> list[ft.Row]: ...
    def extract(self) -> dict[str, Any]: ...


class StudiumKategorieView(KategorieView):
    def __init__(self):
        self.modul = ft.TextField(label="Modul")
        self.gruppenarbeit = ft.RadioGroup(
            value="false",  
            content=ft.Row(
                controls=[
                    ft.Radio(value="true", label="Ja"),
                    ft.Radio(value="false", label="Nein"),
                ]
            ),
        )

    def build_ui(self) -> list[ft.Row]:
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
                    self.gruppenarbeit,
                ]
            ),
        ]

    def extract(self) -> dict[str, Any]:
        return {"modul": self.modul.value, "gruppenarbeit": self.gruppenarbeit.value}


class HaushaltKategorieView(KategorieView):
    def __init__(self):
        self.wiederkehrend = ft.RadioGroup(
            value="false",
            content=ft.Row(
                controls=[
                    ft.Radio(value="true", label="Ja"),
                    ft.Radio(value="false", label="Nein"),
                ]
            ),
        )

    def build_ui(self) -> list[ft.Row]:
        return [
            ft.Row(
                controls=[
                    ft.Text("wiederkehrende Aufgabe:"),
                    ft.Container(expand=True),
                    self.wiederkehrend,
                ]
            )
        ]

    def extract(self) -> dict[str, Any]:
        return {"wiederkehrend": self.wiederkehrend.value}


class FreizeitKategorieView(KategorieView):
    def __init__(self):
        self.hobby = ft.TextField(label="Hobby")
        self.ort = ft.TextField(label="Ort")

    def build_ui(self) -> list[ft.Row]:
        return [
            ft.Row(controls=[ft.Text("Hobby:"), ft.Container(expand=True), self.hobby]),
            ft.Row(
                controls=[
                    ft.Text("Ort:"),
                    ft.Container(expand=True),
                    self.ort,
                ]
            ),
        ]

    def extract(self) -> dict[str, Any]:
        return {"hobby": self.hobby.value, "ort": self.ort.value}


# wenn todo dann zeige todo mit lade_detail_todo wenn nicht erstelle neues todo
class ErzeugeTodoView(ft.Column):
    def __init__(self, presenter: TodoDetailPresenter):
        super().__init__()
        self.presenter: TodoDetailPresenter = presenter
        self.selected_date: date = date.today()

        self.category_fields = ft.Column()
        self.kategorien: dict[str, KategorieView] = {
            "Studium": StudiumKategorieView(),
            "Haushalt": HaushaltKategorieView(),
            "Freizeit": FreizeitKategorieView(),
        }

        # Eingabefelder
        self.title = ft.TextField(label="Titel")

        self.notiz = ft.TextField(label="Notiz")

        self.deadline_text = ft.Text(str(self.selected_date))
        self.deadline = ft.Button(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=self.show_datepicker,
        )

        self.category = ft.RadioGroup(
            value="keine",
            content=ft.Row(
                [
                    ft.Radio(value="keine", label="Keine"),
                    ft.Radio(value="Studium", label="Studium"),
                    ft.Radio(value="Haushalt", label="Haushalt"),
                    ft.Radio(value="Freizeit", label="Freizeit"),
                ]
            ),
            on_change=self.category_changed,
        )

        self.calendar = ft.RadioGroup(
            value="false",
            content=ft.Row(
                [
                    ft.Radio(value="true", label="Ja"),
                    ft.Radio(value="false", label="Nein"),
                ]
            ),
        )

        self.prio = ft.Dropdown(
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
                                controls=[ft.Button("Speichern", on_click=self.save)]
                            ),
                        ]
                    ),
                ),
            )
        )
    
    def show_datepicker(self, e: ft.Event[ft.Button]) -> None:
        if isinstance(e.control.page, ft.Page):
            e.control.page.show_dialog(
                ft.DatePicker(
                    first_date=date(2026, 1, 1),
                    last_date=date(2028, 12, 1),
                    value=self.selected_date,
                    on_change=self.date_changed,
                )
            )

    def date_changed(self, e: ft.Event[ft.DatePicker]) -> None:
        value = e.control.value
        print(f"Selected date: {value} ({type(value)})")

        if isinstance(value, datetime):
            tzone = ZoneInfo("Europe/Berlin")
            value = value.astimezone(tzone).date()
        elif isinstance(value, date):
            value = value

        self.deadline = value
        if self.deadline is not None:
            self.deadline_text.value = self.deadline.isoformat()
        self.update()

    def category_changed(self, e: ft.Event[ft.RadioGroup]) -> None:
        self.category_fields.controls.clear()
        if self.category.value is not None:
            kat = self.kategorien.get(self.category.value)
            if kat:
                self.category_fields.controls.extend(kat.build_ui())
            self.update()

    def lade_ui(self) -> None:
        if self.presenter.is_edit_mode:
            # data = self.presenter.lade_todo(todo_id) if todo_id else {}
            data = self.presenter.current_todo
            if data is not None:
                self.title.value = data.titel
                self.notiz.value = data.notiz
                self.selected_date = data.deadline
                self.calendar.value = "true" if data.calendar else "false"
                self.prio.value = data.priority.name if data.priority else "keine"
                self.category.value = data.category.name if data.category else "keine"
                category = data.category.name if data.category else "keine"
                if category == "Studium":
                    kat = self.kategorien["Studium"]
                    if isinstance(kat, StudiumKategorieView) and isinstance(
                        data.extra, Studium
                    ):
                        kat.modul.value = data.extra.modul
                        kat.gruppenarbeit.value = self.presenter.von_bool_zu_str(
                            data.extra.gruppenarbeit
                        )
                    self.category_fields.controls.extend(kat.build_ui())
                elif category == "Haushalt":
                    kat = self.kategorien["Haushalt"]
                    self.category_fields.controls.extend(kat.build_ui())
                    if isinstance(kat, HaushaltKategorieView) and isinstance(
                        data.extra, Haushalt
                    ):
                        kat.wiederkehrend.value = self.presenter.von_bool_zu_str(
                            data.extra.wiederkehrend
                        )
                elif category == "Freizeit":
                    kat = self.kategorien["Freizeit"]
                    self.category_fields.controls.extend(kat.build_ui())
                    if isinstance(kat, FreizeitKategorieView) and isinstance(
                        data.extra, Freizeit #Betz: View kennt Model? braucht um typechecker zufriedenzustellen
                    ):  # für pyrigth klasse definiert
                        kat.hobby.value = data.extra.hobby
                        kat.ort.value = data.extra.ort

    # ---------------- SAVE ----------------
    def save(self) -> None:
        kat: str | None = (
            self.category.value
        )  # Selbst wenn ein Default gesetzt ist, kann Flet intern den Zustand überschreiben oder nicht initialisieren.
        aktuelle_kat: KategorieView | None = self.kategorien.get(kat) if kat else None
        if aktuelle_kat:
            extra: dict[str, Any] = (
                aktuelle_kat.extract()
            )  # Any ist StudiumKategorie()|HausHaltkategorie()|Freizeikategorie()
        else:
            extra = {}
        self.presenter.save_todo(
            titel=self.title.value,
            notiz=self.notiz.value,
            deadline=self.selected_date,
            calendar=self.calendar.value or "false",
            priority=self.prio.value or "keine",
            category=kat or "keine",
            extra=extra,
        )

        if isinstance(
            self.page, ft.Page
        ):  # für den TypeChecker, eigentlich immer der Fall
            self.page.go(route="/todos")
