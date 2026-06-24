from model.todo_model import ToDo
from repo.todo_repo import TodoRepo


class FiltereTodoPresenter:
    def __init__(self, repo: TodoRepo):
        self.repo: TodoRepo = repo
        self.kat: str = "alle"
        self.prio: str = "alle"
        self.status: str = "alle"

    def set_kategorie(self, value: str):
        self.kat: str = value

    def set_priority(self, value: str):
        self.prio: str = value

    def set_status(self, value: str):
        self.status: str = value

    def get_filtered_todos(self) -> list[ToDo]:
        result: list[ToDo] = self.repo.filtere_todos(self.kat, self.prio, self.status)
        print("Debug", result)
        print("")
        return result
