# pyright: ignore
# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportOptionalMemberAccess=false
from dataclasses import asdict
from datetime import date
from typing import Any
from model.todo_model import (
    FREIZEIT,
    HAUSHALT,
    KATEGORIEN_DICT,
    PRIORITAETEN_DICT,
    STUDIUM,
    Category,
    Freizeit,
    Haushalt,
    Priority,
    Studium,
    ToDo,
)
from repo.todo_repo import TodoRepo

# Datenbank: soen_vorlesung
# Collection: todos -> wird lazy erstellt
# Dokumente: Todoobjekt in json artigen dict


class MongoTodoRepo(TodoRepo):
    def __init__(self, db) -> None:  # type: ignore
        self.db = db

    def speichere(self, todo: ToDo) -> None:
        self.db.todos.insert_one(self.list_to_doc(todo))

    def update_todo(self, todo: ToDo) -> None:
        self.db.todos.update_one(
            {"_todo_id": todo.todo_id}, {"$set": self.list_to_doc(todo)}
        )

    def lade_alle(self) -> list[ToDo]:
        todos: list[ToDo] = []
        alle_eintraege = self.db.todos.find(
            projection={"_id": False}, sort=[("_todo_id", -1)]
        )
        for eintrag in alle_eintraege:
            todos.append(self.doc_to_list(eintrag))
        return todos

    def finde_todo_mit_id(self, todo_id: int) -> ToDo | None:
        todo = self.db.todos.find_one({"_todo_id": todo_id}, projection={"_id": False})  # type: ignore
        if todo is None:
            return None
            # raise ValueError(f"ToDo mit der Id: {todo_id} existiert nicht")
        return self.doc_to_list(todo)  # type: ignore

    def erledige_todo(self, todo_id: int) -> None:
        todo = self.finde_todo_mit_id(todo_id)
        neuer_status = not todo.erledigt
        self.db.todos.update_one(
            {"_todo_id": todo_id}, {"$set": {"_erledigt": neuer_status}}
        )

    def loesche_todo(self, todo: ToDo) -> None:
        self.db.todos.delete_one({"_todo_id": todo.todo_id})

    def filtere_todos(self, kat: str, prio: str, status: str) -> list[ToDo]:
        query: dict[str, Any] = {}
        # Kategorie
        if kat != "alle":
            query["category"] = KATEGORIEN_DICT[kat].name
        # Priorität
        if prio != "alle":
            query["priority"] = PRIORITAETEN_DICT[prio].name
        # Status
        if status == "offen":
            query["_erledigt"] = False
        elif status == "erledigt":
            query["_erledigt"] = True
        todos: list[ToDo] = []
        for doc in self.db.todos.find(
            query, projection={"_id": False}, sort=[("_todo_id", -1)]
        ):  # type: ignore
            todos.append(self.doc_to_list(doc))  # type: ignore
        return todos

    def naechste_id(self) -> int:
        letztes_todo = self.db.todos.find_one(
            sort=[("_todo_id", -1)]
        )  # sortiert  absteigend #Betz warum ist das hier rot? Können wir es ignorieren?
        if letztes_todo is None:
            return 1
        return letztes_todo["_todo_id"] + 1

    # Übersetzung von Liste in Mongo Dict:
    def list_to_doc(self, todo: ToDo) -> dict[str, Any]:
        todo_doc = asdict(todo)
        # Value Object → string
        todo_doc["priority"] = todo.priority.name if todo.priority else None
        todo_doc["category"] = todo.category.name if todo.category else None
        # Date → ISO String
        todo_doc["deadline"] = todo.deadline.isoformat()
        # Extra (nested dataclass → dict)
        todo_doc["extra"] = asdict(todo.extra) if todo.extra is not None else None
        return todo_doc

    def doc_to_list(self, todo_doc: dict[str, Any]) -> ToDo:
        todo_doc["priority"] = Priority.from_str(
            todo_doc["priority"]
        )  # "hoch"-> Priority(name="hoch", symbol="!!!")
        todo_doc["category"] = Category.from_str(todo_doc["category"])
        todo_doc["deadline"] = date.fromisoformat(todo_doc["deadline"])
        if todo_doc["extra"] is not None:
            if todo_doc["category"] == STUDIUM:
                todo_doc["extra"] = Studium(**todo_doc["extra"])
            elif todo_doc["category"] == HAUSHALT:
                todo_doc["extra"] = Haushalt(**todo_doc["extra"])
            elif todo_doc["category"] == FREIZEIT:
                todo_doc["extra"] = Freizeit(**todo_doc["extra"])
        return ToDo(**todo_doc)
