from typing import Protocol, Any
from model.todo_model import (
    ToDoModel,
    hoch,
    mittel,
    niedrig,
    keine_p,
    studium,
    keine,
    haushalt,
    freizeit,
    kategorien_dict,
    prioritäten_dict,
    Studium,
    Haushalt,
    Freizeit,
)
from model.ToDoListe_model import ToDoListModel
from datetime import date
from pymongo.database import Database
from dataclasses import asdict


class TodoRepo(Protocol):
    def speichere(self, todo: ToDoModel) -> None: ...
    def update_todo(self, todo: ToDoModel): ...
    def lade_alle(self) -> ToDoListModel: ...
    def finde_todo_mit_id(self, todo_id: int) -> ToDoModel | None: ...
    def erledige_todo(self, todo_id: int) -> None: ...
    def loesche_todo(self, todo: ToDoModel) -> None: ...
    def filtere_todos(self, kat: str, prio: str, status: str) -> list[ToDoModel]: ...
    def naechste_id(self) -> int:...

class MongoTodoRepo(TodoRepo):
    def __init__(self, db: Database[Any]) -> None:
        self.db = db

    def speichere(self, todo: ToDoModel):
        self.db.todos.insert_one(asdict(todo))

    # def update_todo(self, todo_id: int):
    #     todo=self.db.todos.find_one({"_id": todo_id}, projection={"_id": False})
    #     # self._todos.remove(todo)
    #     # self._todos.append(todo)

    def lade_alle(self) -> ToDoListModel:
        _todos: ToDoListModel = ToDoListModel()
        for todo in self.db.todos.find(projection={"_id": False}):
            todo_obj = ToDoModel(**todo)
            _todos.append(todo_obj)
        return ToDoListModel(todos=_todos)

    def finde_todo_mit_id(self, todo_id: int) -> ToDoModel: 
        todo = self.db.todos.find_one({"_id": todo_id}, projection={"_id": False})
        if todo is None:
            raise ValueError(f"ToDo mit der Id-{todo_id} existiert nicht")
        return ToDoModel(**todo)

    def erledige_todo(self, todo_id: int) -> None:
        todo = self.finde_todo_mit_id(todo_id)
        #if todo is not None:
        neuer_status = not todo["_erledigt"]
        todo.update_one({"_id": todo_id}, {"$set": {"_erledigt": neuer_status}})

    def loesche_todo(self, todo_id: int) -> None:
        todo= self.finde_todo_mit_id(todo_id)
        todo.delete_one({"_id": todo.id})
    
    def filtere_todos(self, kat: str, prio: str, status: str) -> list[ToDoModel]:
        
    def naechste_id(self) -> int:...

class InMemoryTodoRepo(TodoRepo):
    _todos: list[ToDoModel]

    def __init__(self):
        self._todos = [
            ToDoModel(
                _id=1,
                titel="Mathe lernen",
                notiz="Kapitel 3 üben",
                priority=hoch,
                deadline=date(2026, 6, 10),
                calendar=False,
                category=studium,
                extra=Studium(modul="Mathe 2", gruppenarbeit=True),
            ),
            ToDoModel(
                _id=2,
                titel="Hund bürsten",
                notiz="Hundebürste",
                priority=keine_p,
                deadline=date(2026, 6, 10),
                calendar=False,
                category=freizeit,
                extra=Freizeit(hobby="Hundepflege", ort="Zuhause"),
            ),
            ToDoModel(
                _id=3,
                titel="Mathe",
                notiz="MaMo",
                priority=mittel,
                deadline=date(2026, 6, 11),
                calendar=False,
                category=studium,
                extra=Studium(modul="Mathematik", gruppenarbeit=False),
            ),
            ToDoModel(
                _id=4,
                titel="Wäsche waschen",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 12),
                calendar=False,
                category=keine,
            ),
            ToDoModel(
                _id=5,
                titel="Oma anrufen",
                notiz="gut",
                priority=hoch,
                deadline=date(2026, 6, 13),
                calendar=False,
                category=freizeit,
                extra=Freizeit(hobby="Familie", ort="Telefon"),
            ),
            ToDoModel(
                _id=6,
                titel="Staubsaugen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 14),
                calendar=False,
                category=haushalt,
                extra=Haushalt(wiederkehrend=True),
            ),
            ToDoModel(
                _id=7,
                titel="Softwareprojekt-Studyplaner",
                notiz="",
                priority=hoch,
                deadline=date(2026, 6, 15),
                calendar=False,
                category=studium,
                extra=Studium(modul="Software Engineering", gruppenarbeit=True),
            ),
            ToDoModel(
                _id=8,
                titel="Einkaufen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 16),
                calendar=False,
                category=haushalt,
                extra=Haushalt(wiederkehrend=False),
            ),
            ToDoModel(
                _id=9,
                titel="Freunde treffen",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 17),
                calendar=False,
                category=freizeit,
                extra=Freizeit(hobby="Treffen", ort="Stadt"),
            ),
            ToDoModel(
                _id=10,
                titel="Buch lesen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 18),
                calendar=False,
                category=freizeit,
                extra=Freizeit(hobby="Lesen", ort="Wohnzimmer"),
            ),
            ToDoModel(
                _id=11,
                titel="Sport machen",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 19),
                calendar=False,
                category=freizeit,
                extra=Freizeit(hobby="Fitness", ort="Fitnessstudio"),
            ),
            ToDoModel(
                _id=12,
                titel="Projektarbeit",
                notiz="",
                priority=hoch,
                deadline=date(2026, 6, 20),
                calendar=False,
                category=studium,
                extra=Studium(modul="Projektmanagement", gruppenarbeit=True),
            ),
            ToDoModel(
                _id=13,
                titel="Auto waschen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 21),
                calendar=False,
                category=haushalt,
                extra=Haushalt(wiederkehrend=False),
            ),
            ToDoModel(
                _id=14,
                titel="Gartenarbeit",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 22),
                calendar=False,
                category=haushalt,
                extra=Haushalt(wiederkehrend=True),
            ),
            ToDoModel(
                _id=15,
                titel="Kino besuchen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 23),
                calendar=False,
                category=freizeit,
                extra=Freizeit(hobby="Filme", ort="Kino"),
            ),
            ToDoModel(
                _id=16,
                titel="Hausaufgaben",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 24),
                calendar=False,
                category=studium,
                extra=Studium(modul="Informatik", gruppenarbeit=False),
            ),
        ]

    def speichere(self, todo: ToDoModel) -> None:
        self._todos.append(todo)

    def update_todo(self, todo: ToDoModel):
        self._todos.remove(todo)
        self._todos.append(todo)

    def lade_alle(self) -> ToDoListModel:  # unstimmigkeit ?? nur ein model?
        todoliste: ToDoListModel = ToDoListModel()
        todoliste.todos = self._todos
        return todoliste

    def finde_todo_mit_id(self, todo_id: int) -> ToDoModel | None:
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def erledige_todo(self, todo_id: int) -> None:
        todo = self.finde_todo_mit_id(todo_id)
        if todo is not None:
            todo.toggle_erledigt_todo()

    def loesche_todo(self, todo: ToDoModel) -> None:
        self._todos.remove(todo)

    def filtere_todos(self, kat: str, prio: str, status: str) -> list[ToDoModel]:
        result: list[ToDoModel] = self._todos.copy()
        if kat != "alle":
            gefiltert_nach_kategorie: list[ToDoModel] = []
            for todo in result:
                if todo.category == kategorien_dict[kat]:
                    gefiltert_nach_kategorie.append(todo)
            result = gefiltert_nach_kategorie
        # Priorität
        if prio != "alle":
            gefiltert_nach_priority: list[ToDoModel] = []
            for todo in result:
                if todo.priority == prioritäten_dict[prio]:
                    gefiltert_nach_priority.append(todo)

            result = gefiltert_nach_priority
        # Status
        if status == "offen":
            gefiltert_nach_status: list[ToDoModel] = []
            for todo in result:
                if todo.erledigt is False:
                    gefiltert_nach_status.append(todo)
            result = gefiltert_nach_status
        elif status == "erledigt":
            gefiltert_nach_status = []
            for todo in result:
                if todo.erledigt is True:
                    gefiltert_nach_status.append(todo)
            result = gefiltert_nach_status
        return result

    def naechste_id(self) -> int:
        return max(todo.id for todo in self._todos) + 1
