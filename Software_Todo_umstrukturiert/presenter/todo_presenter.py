# pyright: reportUnknownMemberType=false
from model.todo_model import TodoModel

class TodoPresenter:
    def __init__(self):
        self.model=TodoModel()
        self.todos=self.model.todos
    
    def loesche_todo(self,todo_d):
