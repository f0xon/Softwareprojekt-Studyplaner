
from model.todo_model import ToDoModel #warum funktioniert das nicht ?


class ToDoListModel:
    def __init__(self):
        self.todos: list[ToDoModel]=[]

    @property
    def anzahl_offene_todos(self):
        return len(self.todos)