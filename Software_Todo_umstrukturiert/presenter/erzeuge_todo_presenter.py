from typing import Any, Literal

from model.ToDoListe_model import ToDoListModel,ToDoModel
from model.ToDoListe_model import keine_p, niedrig, mittel, hoch, prioritäten_dict
from model.ToDoListe_model import keine, studium, haushalt, freizeit, kategorien_dict
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
            return None
        cls= self.map_category(category)
        if cls is None:
            return None
        return cls(**data)

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