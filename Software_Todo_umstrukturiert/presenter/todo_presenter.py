# pyright: reportUnknownMemberType=false
# #from model.todo_model import TodoModel
from model.ToDoListe_model import ToDoListModel,ToDoModel

#class ToDoPresenter:

 #   def __init__(self):
  #      self.model=ToDoModel()


class TodoListePresenter:
    def __init__(self, model: ToDoListModel):
        self.model = model

    def get_todos(self):
        return list(self.model.dummydaten)
    

    def erledige_todo(self, id: int)->None:
        for todo in self.model.dummydaten:
            if todo.id == id:
                todo.erledige_todo()


    def loesche_todo(self,id: int)->None:
        for todo in self.model.dummydaten:
            if todo.id == id:
                self.model.loesche_todo(todo)

    # def filter_todos(self, kat: str, prio: str, status: str)->list[ToDoModel]:
