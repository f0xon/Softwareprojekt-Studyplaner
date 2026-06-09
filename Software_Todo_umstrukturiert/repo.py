from typing import Protocol
from model.general_model import Todo

class TodoRepo(Protocol):
    def speichere(self,todo:Todo):
        ...
    def lade_alle(self):
        ...
    def lade_todo(self,name:str):
        ...