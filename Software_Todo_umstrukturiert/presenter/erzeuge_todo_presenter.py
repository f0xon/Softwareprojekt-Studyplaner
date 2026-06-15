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
    
    def detail_todo(self,todo:ToDoModel)->dict[str,Any]:
        #in erzeuge_view springen
        #...
        #Daten für die view vorbereiten
        
        title=todo.titel
        notiz=todo.notiz
        deadline=todo.deadline
        calendar=todo.calendar
        erledigt=todo.erledigt
        priority=self.map_priority(todo.priority.name)
        category=self.map_category(todo.category.name)
        data_for_ui:dict[str,Any]={
            "Titel":title,
            "Notiz":notiz,
            "Deadline":deadline,
            "Kalender":calendar,
            "Priorität":priority,
            "Kategorie":category,
            "Erledigt":erledigt
        }
        return data_for_ui

    # @property
    # def übergebe_params_erzeugetodo(self)->dict[str, Any]:
    #     self.detail_todo(todo)

    def save_todo(
        self,
        title: str,
        notiz: str,
        deadline:date,
        calendar: bool,
        priority: str,
        category: str,
        extra: dict[str,Any],
    )->None:
        todo = ToDoModel(
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