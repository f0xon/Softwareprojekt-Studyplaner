# pyright: reportUnknownMemberType=false
from model.todo_model import TodoModel

class FiltereTodoPresenter:
    def __init__(self, model: TodoModel):
        self._model = model