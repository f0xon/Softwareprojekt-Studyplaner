from typing import Protocol

class TodoRepo(Protocol):
    def speichere(todo:Todo)