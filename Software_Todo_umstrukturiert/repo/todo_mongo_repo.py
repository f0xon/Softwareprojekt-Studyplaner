# pyright: ignore
# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportOptionalMemberAccess=false
from dataclasses import asdict
from model.todo_model import ToDo
from repo.todo_repo import TodoRepo

class MongoTodoRepo(TodoRepo):
    def __init__(self, db) -> None: 
        self.db = db 

    def speichere(self, todo: ToDo) ->None:
        self.db.todos.insert_one(self.to_doc(todo))

    def update_todo(self, todo: ToDo)->None:
        self.db.todos.update_one(
            {"_id": todo.id},
            {"$set": asdict(todo)}
        )
        # self._todos.remove(todo)
        # self._todos.append(todo)

    def lade_alle(self) -> list[ToDo]:
        todos: list[ToDo] = []
        for todo in self.db.todos.find(projection={"_id": False}):
            todos.append(ToDo(**todo))
        return todos

    def finde_todo_mit_id(self, todo_id: int) -> ToDo: 
        todo = self.db.todos.find_one({"_id": todo_id}, projection={"_id": False})
        if todo is None:
            raise ValueError(f"ToDo mit der Id-{todo_id} existiert nicht")
        return ToDo(**todo)

    def erledige_todo(self, todo_id: int) -> None:
        todo = self.finde_todo_mit_id(todo_id)
        neuer_status = not todo.erledigt
        self.db.todos.update_one(
            {"_id": todo_id},
            {"$set": {"_erledigt": neuer_status}}
        )

    def loesche_todo(self, todo:ToDo) -> None:
        self.db.todos.delete_one({"_id": todo.id})
    
    def filtere_todos(self, kat: str, prio: str, status: str) -> list[ToDo]:#ki lösung muss noch angepasst werden
        result:list[ToDo]=self.lade_alle()
         if kat != "alle":
            todos = [
                t for t in todos
                if t.category and t.category.name == kat
            ]
        if prio != "alle":
            todos = [
                t for t in todos
                if t.priority and t.priority.name == prio
            ]
        if status == "offen":
            todos = [t for t in todos if not t.erledigt]
        elif status == "erledigt":
            todos = [t for t in todos if t.erledigt]

        return todos
    
    def naechste_id(self) -> int:...

