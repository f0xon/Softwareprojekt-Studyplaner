# pyright: reportUnknownMemberType=false
from dataclasses import dataclass

@dataclass (frozen=True)
class Priority:
    name:str
    #schriftdicke
    #filternhilfe
keine=Priority("keine")
niedrig=Priority("niedrig")
mittel=Priority("mittel")
hoch=Priority("hoch")

@dataclass (frozen=True)
class Category:
    name:str
    #schriftdicke
    #filternhilfe  
studium=Category("Studium")
haushalt=Category("Haushalt")
freizeit=Category ("Freizeit")

@dataclass
class Todo:
    titel:str
    notiz:str
    priority:Priority
    #deadline:datetime.date
    category:Category
    #calender: str
    _erledigt: bool=False

    @property
    def erledigt(self)->bool:
        return self._erledigt

class TodoModel:
        def __init__(self):
              self.todos=[
                    Todo("Hund bürsten","Hundebürste",keine,freizeit),
                    Todo("Mathe","MaMo",mittel,studium),
                    Todo("Wäsche waschen","",mittel, haushalt),
                    Todo("Oma anrufen","gut",hoch,freizeit)
              ]



# class TodosModel:
#     def __init__(self):
#         self._todos:list[ErzeugeTodoModel]=[]
    
#     def add_todo(self,todo:ErzeugeTodoModel):
#         self._todos.append(todo)

#     def get_todos(self)->list[ErzeugeTodoModel]:
#         return self._todos
    
#     def filter_todos(self, status:str, kategorie:str, datum:str)->list[ErzeugeTodoModel]: #anfang der Logik zum Filtern der Todos basierend auf den Kriterien
#         filtered_todos:list[ErzeugeTodoModel] = []
        
        # for todo in self._todos: #alle solt fuktionieren
        #     if status != "alle":
        #         filtered_todos.append(todo)
        #     elif status == "offen":
        #         if self.todo._done == False:
        #             filtered_todos.append(todo)
        #     elif status == "erledigt":
        #     filtered_todos = [todo for todo in filtered_todos if todo.status == "erledigt"]
        
        # if kategorie != "keine":
        #     filtered_todos = [todo for todo in filtered_todos if todo.kategorie == kategorie]
        
        # Datum-Filterlogik könnte hier hinzugefügt werden
        
        #return filtered_todos
    
    # def get_todos(self)->list[str]: 
        #return ["TD1", "TD2", "TD3"]