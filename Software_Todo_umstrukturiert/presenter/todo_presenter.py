# pyright: reportUnknownMemberType=false
# #from model.todo_model import TodoModel
from model.todo_model import ToDo
from repo.todo_repo import TodoRepo


class TodoListePresenter:
    _repo: TodoRepo

    def __init__(self, repo: TodoRepo):
        self._repo: TodoRepo = repo

    def get_todos(self) -> list[ToDo]:
        return self._repo.lade_alle()

    def erledige_todo(self, id: int) -> None:
        todo: ToDo = self.todo_None(todo=self._repo.finde_todo_mit_id(todo_id=id))
        todo.toggle_erledigt_todo()
        self._repo.update_todo(todo)


    def loesche_todo(self, id: int) -> None:
        todo: ToDo = self.todo_None(todo=self._repo.finde_todo_mit_id(todo_id=id))
        self._repo.loesche_todo(todo)


    def lade_todo(self, id: int) -> ToDo | None:  # None passt hier
        for todo in self._repo.lade_alle():
            if todo.todo_id == id:
                return todo
        return None 

    def todo_None(self, todo: ToDo | None) -> ToDo:
        if todo is None:
            raise ValueError("Todo nicht gefunden")
        return todo
    
    def ist_liste_leer(self) -> bool:
        return len(self._repo.lade_alle()) == 0
