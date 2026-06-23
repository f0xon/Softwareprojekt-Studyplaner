from typing import Any
from model.todo_model import ToDo
from repo.todo_repo import TodoRepo

class MongoTodoRepo(TodoRepo):
    def __init__(self, db: Database[Any]) -> None:
        self.db = db

    def speichere(self, todo: ToDo) ->None:
        ...
        #todo = self.finde_todo_mit_id(todo_id)

    # def update_todo(self, todo_id: int):
    #     todo=self.db.todos.find_one({"_id": todo_id}, projection={"_id": False})
    #     # self._todos.remove(todo)
    #     # self._todos.append(todo)

    def lade_alle(self) -> list[ToDo]:
        _todos: ToDoListModel = ToDoListModel()
        for todo in self.db.todos.find(projection={"_id": False}):
            todo_obj = ToDo(**todo)
            _todos.append(todo_obj)
        return ToDoListModel(todos=_todos)

    def finde_todo_mit_id(self, todo_id: int) -> ToDo: 
        todo = self.db.todos.find_one({"_id": todo_id}, projection={"_id": False})
        if todo is None:
            raise ValueError(f"ToDo mit der Id-{todo_id} existiert nicht")
        return ToDo(**todo)

    def erledige_todo(self, todo_id: int) -> None:
        todo = self.finde_todo_mit_id(todo_id)
        #if todo is not None:
        neuer_status = not todo["_erledigt"]
        todo.update_one({"_id": todo_id}, {"$set": {"_erledigt": neuer_status}})

    def loesche_todo(self, todo_id: int) -> None:
        todo= self.finde_todo_mit_id(todo_id)
        todo.delete_one({"_id": todo.id})
    
    def filtere_todos(self, kat: str, prio: str, status: str) -> list[ToDo]:
        result:ToDoListModel=self.lade_alle()

        
    def naechste_id(self) -> int:...