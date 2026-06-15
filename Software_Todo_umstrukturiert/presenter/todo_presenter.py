# pyright: reportUnknownMemberType=false
# #from model.todo_model import TodoModel
from model.ToDoListe_model import ToDoListModel,ToDoModel
from repo import TodoRepo

#class ToDoPresenter:

 #   def __init__(self):
  #      self.model=ToDoModel()


class TodoListePresenter:

    _model: list[ToDoModel]
    #_repo: TodoRepo

    def __init__(self, model: ToDoListModel,repo:TodoRepo):
        #self._repo = repo
        #self._model = self.repo.get_all_todos()
        self.model = model
        self.repo=repo

    def get_todos(self):
        return self.repo.lade_alle()
    

    def erledige_todo(self, id: int)->None:
        for todo in self.repo.lade_alle():
            if todo.id == id:
                todo.erledige_todo()


    def loesche_todo(self,id: int)->None:
        for todo in self.repo.lade_alle():
            if todo.id == id:
                self.repo.loesche_todo(todo.id)


    def lade_todo(self, id: int)->ToDoModel | None:
        for todo in self.repo.lade_alle():
            if todo.id == id:
                return todo
        return None

    # def filter_todos(self, kat: str, prio: str, status: str)->list[ToDoModel]:
