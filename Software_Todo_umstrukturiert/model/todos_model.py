# pyright: reportUnknownMemberType=false
from model.erzeuge_todo_model import ErzeugeTodoModel

class TodosModel:
    def __init__(self):
        self._todos:list[ErzeugeTodoModel]=[]
    
    def add_todo(self,todo:ErzeugeTodoModel):
        self._todos.append(todo)

    def get_todos(self)->list[ErzeugeTodoModel]:
        return self._todos
    
    def filter_todos(self, status:str, kategorie:str, datum:str)->list[ErzeugeTodoModel]: #anfang der Logik zum Filtern der Todos basierend auf den Kriterien
        filtered_todos:list[ErzeugeTodoModel] = []
        
        for todo in filtered_todos:
            if status != "alle":
                continue
            elif status == "offen":
                if self.todo._done == False:
                    filtered_todos.append(todo)


            filtered_todos = [todo for todo in filtered_todos if todo.status == status]
        
            filtered_todos = [todo for todo in filtered_todos if todo.status == "offen"]
        elif status == "erledigt":
            filtered_todos = [todo for todo in filtered_todos if todo.status == "erledigt"]
        
        if kategorie != "keine":
            filtered_todos = [todo for todo in filtered_todos if todo.kategorie == kategorie]
        
        # Datum-Filterlogik könnte hier hinzugefügt werden
        
        return filtered_todos
    
    # def get_todos(self)->list[str]: 
        #return ["TD1", "TD2", "TD3"]