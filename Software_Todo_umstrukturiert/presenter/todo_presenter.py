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
        todo = self._repo.finde_todo_mit_id(id)
        if todo is None:
            #TODO fix: behandle Fehler
            ...
            return
        todo.toggle_erledigt_todo()
        self._repo.speichere(todo)

    def loesche_todo(self,id: int)->None:
        todo = self._repo.finde_todo_mit_id(id)
        # if todo is None:
        #     #TODO fix: behandle Fehler
        #     ...
        #     return
        # self._repo.loesche_todo() repo umbauen sodass todo haben will und nicht die todo id
        for todo in self._repo.lade_alle():
            if todo.id == id:
                self._repo.loesche_todo(todo.id)


    def lade_todo(self, id: int)->ToDoModel | None:
        for todo in self._repo.lade_alle():
            if todo.id == id:
                return todo
        return None

