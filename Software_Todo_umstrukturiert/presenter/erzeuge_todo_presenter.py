from typing import Any, Literal

from model.general_model import GeneralModel,Todo, Studium, Haushalt, Freizeit
from model.general_model import keine,niedrig, mittel, hoch
from model.general_model import studium, haushalt,freizeit
from datetime import date

#class ErzeugeTodoPresenter:
class TodoDetailPresenter:

    _modus: Literal["create", "edit"]
    _model: Todo

    def __init__(self):
        self.model = GeneralModel()
        # self.model
    
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

    def build_extra(self, category: str, data: dict[str,Any]):
        if not data:
            return None
        mapping = {
            "Studium": Studium,
            "Haushalt": Haushalt,
            "Freizeit": Freizeit,
        }
        cls:Studium|Haushalt|Freizeit = mapping.get(category)
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