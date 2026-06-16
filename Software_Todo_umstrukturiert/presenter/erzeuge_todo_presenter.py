from dataclasses import asdict
from typing import Any, Literal

from model.ToDoListe_model import ToDoListModel,ToDoModel
from model.todo_model import prioritäten_dict, kategorien_dict
from model.todo_model import Studium,Haushalt, Freizeit, kategorien_dict
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
    
    @property
    def current_todo(self) -> ToDoModel | None:
        if self._current_todo:
            return self._current_todo
        return None
    
    def map_priority(self, value:str)->Any:#?eigentlich nur keine_p, niedrig, mittel, hoch
        return prioritäten_dict.get(value)

    def map_category(self, value:str)->Any:
        return kategorien_dict.get(value)

    def build_extra(self, category: str, data: dict[str,Any])->Studium|Haushalt|Freizeit|None:
        if not data:
            return None
        mapping:dict[str,type[Studium]|type[Haushalt]|type[Freizeit] | None] = {
            "Studium": Studium,
            "Haushalt": Haushalt,
            "Freizeit": Freizeit,
        }
        cls:type[Studium]|type[Haushalt]|type[Freizeit]=mapping.get(category, None)
        return cls(**data)
    
    # LOAD (Edit-Modus)
    def lade_todo(self, todo_id: int) -> None: # None
        todo = self.repo.finde_todo_mit_id(todo_id)
        self._current_todo = todo

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