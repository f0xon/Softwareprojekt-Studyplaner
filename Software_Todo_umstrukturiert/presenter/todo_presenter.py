# pyright: reportUnknownMemberType=false
# #from model.todo_model import TodoModel
from model.ToDoListe_model import ToDoListModel,ToDoModel
from repo import TodoRepo

class TodoListePresenter:

    _model: ToDoListModel
    _repo: TodoRepo

    def __init__(self, model: ToDoListModel,repo:TodoRepo):
        #self._repo = repo
        #self._model = self.repo.get_all_todos() #Repo wo auswählen Presenter/Router ? 
        self._model = model
        self._repo=repo

    def get_todos(self):
        return self._repo.lade_alle()
    

    def erledige_todo(self, id: int)->None:
        todo = self.todo_None(self._repo.finde_todo_mit_id(id))
        todo.toggle_erledigt_todo()
        self._repo.speichere(todo)

    def loesche_todo(self,id: int)->None:
        todo = self.todo_None(self._repo.finde_todo_mit_id(id))
        self._repo.loesche_todo(todo)


    def lade_todo(self, id: int)->ToDoModel | None:
        for todo in self._repo.lade_alle():
            if todo.id == id:
                return todo
        return None
    
    def todo_None(self, todo:ToDoModel|None)->ToDoModel:
        if todo is None:
            raise ValueError("Todo nicht gefunden")
        return todo


