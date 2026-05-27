# pyright: reportUnknownMemberType=false
from model.erzeuge_todo_model import ErzeugeTodoModel
class TodosModel:
    def __init__(self):
        self._todos:list[ErzeugeTodoModel]=[]
    
    def add_todo(self,todo):
        self._todos.append(todo)

    def get_todos(self)->list[ErzeugeTodoModel]:
        return self._todos
    
    # def get_todos(self)->list[str]: 
        #return ["TD1", "TD2", "TD3"]