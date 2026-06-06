from datetime import datetime

#from model.erzeuge_todo_model import ErzeugeTodoModel
#from model.todos_model import TodosModel
from model.todo_model import TodoModel, ErstelleTodo

class ErzeugeTodoPresenter:
    def __init__(self, model: TodoModel):
        self._model=model

    def erzeuge_todo(self, titel:str, notiz:str, priority_name:str, category_name:str):
        neue_Daten = ErstelleTodo(titel, notiz, priority_name, category_name)
        self._model.fuege_todo_hinzu(neue_Daten)
    
        #self.router=router
        #self.model=router.todos_model # Globale Liste über Router aufgerufen
        #self.model = TodosModel() #schlecht --> jeder presenter hat eigene liste --> todo sonst nach speichern weg

    #def save_todo(self, title: str, deadline: datetime.date, category: str):
    #    todo=ErzeugeTodoModel(title, deadline, category)
    #    print(todo)
    #    #self.model.add_todo(todo)
    #    #elf.router.go_to_todos()

    # def erzeuge_todo(self):
    #     self.router.go_to_erzeuge_todo()