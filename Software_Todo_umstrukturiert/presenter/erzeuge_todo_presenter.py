from typing import Any, Literal

from model.ToDoListe_model import ToDoListModel,ToDoModel
from model.ToDoListe_model import prioritäten_dict
from model.ToDoListe_model import Studium,Haushalt, Freizeit, kategorien_dict
from repo import TodoRepo
from datetime import date

#class ErzeugeTodoPresenter:
class TodoDetailPresenter:

    _modus: Literal["create", "edit"]
    _model: ToDoModel

    def __init__(self, model: ToDoListModel,repo:TodoRepo):
        self.model = model
        self.repo=repo
        self._current_todo: ToDoModel | None = None

    @property
    def is_create_mode(self) -> bool:
        return self._modus == "create"

    @property
    def is_edit_mode(self) -> bool:
        return self._modus == "edit"
    
    def map_priority(self, value:str)->Any:#?eigentlich nur keine_p, niedrig, mittel, hoch
        return prioritäten_dict.get(value)

    def map_category(self, value:str)->Any:
        return kategorien_dict.get(value)

    def build_extra(self, category: str, data: dict[str,Any]):
        if not data:
            return {}
        mapping:dict[str,type[Studium]|type[Haushalt]|type[Freizeit]] = {
            "Studium": Studium,
            "Haushalt": Haushalt,
            "Freizeit": Freizeit,
        }
        cls:type[Studium]|type[Haushalt]|type[Freizeit]=mapping.get(category)
        return cls(**data)
    
    # def detail_todo(self,todo_id:int)->dict[str,Any]:
    #     #in erzeuge_view springen
    #     #...
    #     #Daten für die view vorbereiten
    #     todo=self.repo.finde_todo_mit_id(todo_id)
    #     title=todo.titel
    #     notiz=todo.notiz
    #     deadline=todo.deadline
    #     calendar=todo.calendar
    #     erledigt=todo.erledigt
    #     priority=self.map_priority(todo.priority.name)
    #     category=self.map_category(todo.category.name)
    #     data_for_ui:dict[str,Any]={
    #         "Titel":title,
    #         "Notiz":notiz,
    #         "Deadline":deadline,
    #         "Kalender":calendar,
    #         "Priorität":priority,
    #         "Kategorie":category,
    #         "Erledigt":erledigt
    #     }
    #     return data_for_ui

    # def get_current_todo_data(self) -> dict[str, Any] | None:
    #     return self._current_todo
    
    # LOAD (Edit-Modus)
    def lade_todo(self, todo_id: int) -> dict[str, Any]:
        todo = self.repo.finde_todo_mit_id(todo_id)
        self._current_todo = todo

        if not todo:
            return {}
        
        print(f"""Titel {todo.titel}
            "Notiz" {todo.notiz},
            "Deadline": {todo.deadline},
            "Kalender": {todo.calendar},
            "Priorität": {todo.priority.name},
            "Kategorie": {todo.category.name}""")

        return {
            "Titel": todo.titel,
            "Notiz": todo.notiz,
            "Deadline": todo.deadline,
            "Kalender": todo.calendar,
            "Priorität": todo.priority.name,
            "Kategorie": todo.category.name,
            "Extra":
        }

    def save_todo(
        self,
        # id:int,
        titel: str,
        notiz: str,
        deadline:date,
        calendar: bool,
        priority: str,
        category: str,
        extra: dict[str,Any],
    ) -> None:

        if self._current_todo:   # EDIT
            todo = self._current_todo
            todo.titel = titel
            todo.notiz = notiz
            todo.deadline = deadline
            todo.calendar = calendar
            todo.priority = priority
            todo.category = category
            todo.extra = extra
        else:               # CREATE
            todo = ToDoModel(
                _id=self.repo.naechste_id(),
                titel=titel,
                notiz=notiz,
                deadline=deadline,
                calendar=calendar,
                priority=self.map_priority(priority),
                category=self.map_category(category),
                extra=self.build_extra(category, extra),
            )
            self.repo.speichere(todo)


    # def save_todo(
    #     self,
    #     # id:int,
    #     title: str,
    #     notiz: str,
    #     deadline:date,
    #     calendar: bool,
    #     priority: str,
    #     category: str,
    #     extra: dict[str,Any],
    # )->None:
    #     todo = ToDoModel(
    #         _id=self.repo.naechste_id(),
    #         titel=title,
    #         notiz=notiz,
    #         deadline=deadline,
    #         calendar=calendar,
    #         priority=self.map_priority(priority),  
    #         category=self.map_category(category),
    #         extra=self.build_extra(category, extra),
    #     )

    #     # self.model.add_todo(todo)
    #     self.repo.speichere(todo)

    #     print("DEBUG: Todo gespeichert",todo)