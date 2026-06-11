from typing import Any

<<<<<<< HEAD
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
=======
from model.general_model import GeneralModel,Todo, Studium, Haushalt, Freizeit
from model.general_model import keine,niedrig, mittel, hoch
from model.general_model import studium, haushalt,freizeit
from datetime import date

class ErzeugeTodoPresenter:
    def __init__(self):
        self.model = GeneralModel()
    
    def map_priority(self, value:str):
        dict_prio:dict[str,Any]={
            "keine":keine,
            "niedrig":niedrig,
            "mittel":mittel,
            "hoch":hoch
        }       
        return dict_prio.get(value)

    def map_category(self, value:str):
        dict_prio:dict[str,Any]={
            "keine":None,
            "Studium":studium,
            "Freizeit":freizeit,
            "Haushalt":haushalt
        }       
        return dict_prio.get(value)
>>>>>>> origin/test-spaltung-for-Datenbanken

    def build_extra(self, category: str, data: dict[str,Any])->dict[str,Any]|None:
        if not data:
            return None
        mapping:dict[str,Studium|Haushalt|Freizeit] = {
            "Studium": Studium,
            "Haushalt": Haushalt,
            "Freizeit": Freizeit,
        }
<<<<<<< Updated upstream
        cls:Studium|Haushalt|Freizeit = mapping.get(category)
        if cls is None:
            return None
=======
        cls:Studium|Haushalt|Freizeit=mapping.get(category)
>>>>>>> Stashed changes
        return cls(**data)

    def show_todo(self,todo:ToDoModel)->dict[str,Any]:
        title=todo.titel
        notiz=todo.notiz
        deadline=todo.deadline
        calendar=todo.calendar
        priority=self.map_priority(todo.priority.name)
        category=self.map_category(todo.category.name)
        data_for_ui:dict[str,Any]={
            "Titel":title,
            "Notiz":notiz,
            "Deadline":deadline,
            "Kalender":calendar,
            "Priorität":priority,
            "Kategorie":category
        }
        return data_for_ui

    def save_todo(
        self,
        title: str,
        notiz: str,
        deadline:date,
        calendar: bool,
        priority: str,
        category: str,
        extra: dict[str,Any],
    ):
        todo = Todo(
            titel=title,
            notiz=notiz,
            deadline=deadline,
            calendar=calendar,
            priority=self.map_priority(priority),  
            category=self.map_category(category),
            extra=self.build_extra(category, extra),
        )

        self.model.add_todo(todo)

        print("DEBUG: Todo gespeichert",todo)
    
    # def show_details(self,todo:ToDoModel)->None:
    #     self._modus="edit"
    #     #ErzeugeTodoView(todo)