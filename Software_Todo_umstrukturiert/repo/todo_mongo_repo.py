# pyright: ignore
# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportOptionalMemberAccess=false
from dataclasses import asdict
from datetime import date
from sqlite3 import Cursor
from typing import Any
from model.todo_model import KATEGORIEN_DICT, PRIORITAETEN_DICT, Category, Priority, ToDo
from repo.todo_repo import TodoRepo

#Datenbank: soen_vorlesung
#Collection: todos -> wird lazy erstellt
#Dokumente: Todoobjekt in json 

class MongoTodoRepo(TodoRepo):
    def __init__(self, db) -> None: 
        self.db = db 

    def speichere(self, todo: ToDo) ->None:
        self.db.todos.insert_one(self.list_to_doc(todo)) #TODO todo_id mit erzeugen

    def update_todo(self, todo: ToDo)->None:
        self.db.todos.update_one(
            {"_id": todo.todo_id},
            {"$set": self.list_to_doc(todo)}
        )
        # self._todos.remove(todo)
        # self._todos.append(todo)

    def lade_alle(self) -> list[ToDo]:
        todos: list[ToDo] = []
        alle_eintraege=self.db.todos.find(projection={"_id": False})
        for eintrag in alle_eintraege:
            todos.append(self.doc_to_list(eintrag))
        return todos

    def finde_todo_mit_id(self, todo_id: int) -> ToDo: 
        todo = self.db.todos.find_one({"_id": todo_id}, projection={"_id": False})
        if todo is None:
            raise ValueError(f"ToDo mit der Id-{todo_id} existiert nicht")
        return self.doc_to_list(todo)

    def erledige_todo(self, todo_id: int) -> None:
        todo = self.finde_todo_mit_id(todo_id)
        neuer_status = not todo.erledigt
        self.db.todos.update_one(
            {"_id": todo_id},
            {"$set": {"erledigt": neuer_status}}
        )

    def loesche_todo(self, todo:ToDo) -> None:
        self.db.todos.delete_one({"_id": todo.todo_id})
    
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
            query["erledigt"] = False
        elif status == "erledigt":
            query["erledigt"] = True
        todos: list[ToDo] = []
        for doc in self.db.todos.find(query):
            todos.append(self.doc_to_list(doc))
        return todos
    
    def naechste_id(self) -> int:...

    #Übersetzung von Liste in Mongo Dict:
    def list_to_doc(self, todo: ToDo) -> dict[str,Any]:
        todo_doc = asdict(todo)
        #Value Object → string
        todo_doc["priority"] = todo.priority.name if todo.priority else None
        todo_doc["category"] = todo.category.name if todo.category else None
        # Date → ISO String
        todo_doc["deadline"] = todo.deadline.isoformat()
        # Extra (nested dataclass → dict)
        todo_doc["extra"] = asdict(todo.extra) if todo.extra else None
        return todo_doc
    
    #Betz: Model mit im repo ok?
    def doc_to_list(self, todo_doc:dict[str,Any])->ToDo:
        todo_doc["priority"] = Priority.from_str(todo_doc["priority"]) #vorher "hoch"-> Priority(name="hoch", ausrufezeichen="!!!")
        todo_doc["category"] = Category.from_str(todo_doc["category"])
        todo_doc["deadline"] = date.fromisoformat(todo_doc["deadline"])
        todo_doc["extra"] = todo_doc["extra"]
        return ToDo(**todo_doc)

