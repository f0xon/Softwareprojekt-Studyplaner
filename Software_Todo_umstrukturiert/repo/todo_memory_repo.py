from model.todo_model import (
    ToDo,
    HOCH,
    MITTEL,
    NIEDRIG,
    KEINE_P,
    STUDIUM,
    KEINE,
    HAUSHALT,
    FREIZEIT,
    KATEGORIEN_DICT,
    PRIORITAETEN_DICT,
    Studium,
    Haushalt,
    Freizeit,
)
from datetime import date
from repo.todo_repo import TodoRepo


class InMemoryTodoRepo(TodoRepo):
    _todos: list[ToDo]

    def __init__(self):
        self._todos: list[ToDo] = [
            ToDo(
                _todo_id=1,
                titel="Mathe lernen",
                notiz="Kapitel 3 üben",
                priority=HOCH,
                deadline=date(2026, 6, 10),
                calendar=False,
                category=STUDIUM,
                extra=Studium(modul="Mathe 2", gruppenarbeit=True),
            ),
            ToDo(
                _todo_id=2,
                titel="Hund bürsten",
                notiz="Hundebürste",
                priority=KEINE_P,
                deadline=date(2026, 6, 10),
                calendar=False,
                category=FREIZEIT,
                extra=Freizeit(hobby="Hundepflege", ort="Zuhause"),
            ),
            ToDo(
                _todo_id=3,
                titel="Mathe",
                notiz="MaMo",
                priority=MITTEL,
                deadline=date(2026, 6, 11),
                calendar=False,
                category=STUDIUM,
                extra=Studium(modul="Mathematik", gruppenarbeit=False),
            ),
            ToDo(
                _todo_id=4,
                titel="Wäsche waschen",
                notiz="",
                priority=MITTEL,
                deadline=date(2026, 6, 12),
                calendar=False,
                category=KEINE,
            ),
            ToDo(
                _todo_id=5,
                titel="Oma anrufen",
                notiz="gut",
                priority=HOCH,
                deadline=date(2026, 6, 13),
                calendar=False,
                category=FREIZEIT,
                extra=Freizeit(hobby="Familie", ort="Telefon"),
            ),
            ToDo(
                _todo_id=6,
                titel="Staubsaugen",
                notiz="",
                priority=NIEDRIG,
                deadline=date(2026, 6, 14),
                calendar=False,
                category=HAUSHALT,
                extra=Haushalt(wiederkehrend=True),
            ),
            ToDo(
                _todo_id=7,
                titel="Softwareprojekt-Studyplaner",
                notiz="",
                priority=HOCH,
                deadline=date(2026, 6, 15),
                calendar=False,
                category=STUDIUM,
                extra=Studium(modul="Software Engineering", gruppenarbeit=True),
            ),
            ToDo(
                _todo_id=8,
                titel="Einkaufen",
                notiz="",
                priority=NIEDRIG,
                deadline=date(2026, 6, 16),
                calendar=False,
                category=HAUSHALT,
                extra=Haushalt(wiederkehrend=False),
            ),
            ToDo(
                _todo_id=9,
                titel="Freunde treffen",
                notiz="",
                priority=MITTEL,
                deadline=date(2026, 6, 17),
                calendar=False,
                category=FREIZEIT,
                extra=Freizeit(hobby="Treffen", ort="Stadt"),
            ),
            ToDo(
                _todo_id=10,
                titel="Buch lesen",
                notiz="",
                priority=NIEDRIG,
                deadline=date(2026, 6, 18),
                calendar=False,
                category=FREIZEIT,
                extra=Freizeit(hobby="Lesen", ort="Wohnzimmer"),
            ),
            ToDo(
                _todo_id=11,
                titel="Sport machen",
                notiz="",
                priority=MITTEL,
                deadline=date(2026, 6, 19),
                calendar=False,
                category=FREIZEIT,
                extra=Freizeit(hobby="Fitness", ort="Fitnessstudio"),
            ),
            ToDo(
                _todo_id=12,
                titel="Projektarbeit",
                notiz="",
                priority=HOCH,
                deadline=date(2026, 6, 20),
                calendar=False,
                category=STUDIUM,
                extra=Studium(modul="Projektmanagement", gruppenarbeit=True),
            ),
            ToDo(
                _todo_id=13,
                titel="Auto waschen",
                notiz="",
                priority=NIEDRIG,
                deadline=date(2026, 6, 21),
                calendar=False,
                category=HAUSHALT,
                extra=Haushalt(wiederkehrend=False),
            ),
            ToDo(
                _todo_id=14,
                titel="Gartenarbeit",
                notiz="",
                priority=MITTEL,
                deadline=date(2026, 6, 22),
                calendar=False,
                category=HAUSHALT,
                extra=Haushalt(wiederkehrend=True),
            ),
            ToDo(
                _todo_id=15,
                titel="Kino besuchen",
                notiz="",
                priority=NIEDRIG,
                deadline=date(2026, 6, 23),
                calendar=False,
                category=FREIZEIT,
                extra=Freizeit(hobby="Filme", ort="Kino"),
            ),
            ToDo(
                _todo_id=16,
                titel="Hausaufgaben",
                notiz="",
                priority=MITTEL,
                deadline=date(2026, 6, 24),
                calendar=False,
                category=STUDIUM,
                extra=Studium(modul="Informatik", gruppenarbeit=False),
            ),
        ]

    def speichere(self, todo: ToDo) -> None:
        self._todos.append(todo)

    def update_todo(self, todo: ToDo) -> None:
        self._todos.remove(todo)
        self._todos.append(todo)

    def lade_alle(self) -> list[ToDo]:  # unstimmigkeit ?? nur ein model?
        return self._todos

    def finde_todo_mit_id(self, todo_id: int) -> ToDo | None:
        for todo in self._todos:
            if todo.todo_id == todo_id:
                return todo
        return None

    def erledige_todo(self, todo_id: int) -> None:
        todo = self.finde_todo_mit_id(todo_id)
        if todo is not None:
            todo.toggle_erledigt_todo()

    def loesche_todo(self, todo: ToDo) -> None:
        self._todos.remove(todo)

    def filtere_todos(self, kat: str, prio: str, status: str) -> list[ToDo]:
        result: list[ToDo] = self._todos.copy()
        if kat != "alle":
            gefiltert_nach_kategorie: list[ToDo] = []
            for todo in result:
                if todo.category == KATEGORIEN_DICT[kat]:
                    gefiltert_nach_kategorie.append(todo)
            result: list[ToDo] = gefiltert_nach_kategorie
        # Priorität
        if prio != "alle":
            gefiltert_nach_priority: list[ToDo] = []
            for todo in result:
                if todo.priority == PRIORITAETEN_DICT[prio]:
                    gefiltert_nach_priority.append(todo)

            result: list[ToDo] = gefiltert_nach_priority
        # Status
        if status == "offen":
            gefiltert_nach_status: list[ToDo] = []
            for todo in result:
                if todo.erledigt is False:
                    gefiltert_nach_status.append(todo)
            result: list[ToDo] = gefiltert_nach_status
        elif status == "erledigt":
            gefiltert_nach_status: list[ToDo] = []
            for todo in result:
                if todo.erledigt is True:
                    gefiltert_nach_status.append(todo)
            result: list[ToDo] = gefiltert_nach_status
        return result

    def naechste_id(self) -> int:
        return max(todo.todo_id for todo in self._todos) + 1
