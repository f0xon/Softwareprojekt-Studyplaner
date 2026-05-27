#from model.erzeuge_todo_model import ErzeugeTodoModel
from model.erzeuge_todo_model import ErzeugeTodoModel
#from model.todos_model import TodosModel

class ErzeugeTodoPresenter:
    def __init__(self,router):
        self.router=router
        self.model=router.todos_model # Globale Liste über Router aufgerufen
        #self.model = TodosModel() #schlecht --> jeder presenter hat eigene liste --> todo sonst nach speichern weg

    def save_todo(self, title: str, deadline: str, category: str):
        todo=ErzeugeTodoModel(title, deadline, category)
        self.model.add_todo(todo)
        self.router.go_to_todos()

    # def erzeuge_todo(self):
    #     self.router.go_to_erzeuge_todo()