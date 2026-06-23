# pyright: reportUnknownMemberType=false
# #from model.todo_model import TodoModel
from model.todo_model import ToDo
from repo.todo_repo import TodoRepo

class TodoListePresenter:
    _model: ToDo
    _repo: TodoRepo

    def __init__(self, model: ToDo, repo: TodoRepo):
        self._repo = repo
        self._model = model
        self._repo = repo

    def get_todos(self) -> list[ToDo]:
        return self._repo.lade_alle()

    def erledige_todo(self, id: int) -> None:
        try:  # wenn erledigt angehakt ist doppelt
            todo = self.todo_None(self._repo.finde_todo_mit_id(id))
            todo.toggle_erledigt_todo()
            self._repo.update_todo(todo)
        except ValueError as e:
            print(f"Fehler:{e}")

    def loesche_todo(self, id: int) -> None:
        try:
            todo = self.todo_None(self._repo.finde_todo_mit_id(id))
            self._repo.loesche_todo(todo)
        except ValueError as e:
            print(f"Fehler:{e}")

    def lade_todo(self, id: int) -> ToDo | None:  # None passt hier
        for todo in self._repo.lade_alle().todos:
            if todo.id == id:
                return todo
        return None

    def todo_None(self, todo: ToDo | None) -> ToDo:
        if todo is None:
            raise ValueError("Todo nicht gefunden")
        return todo
