# from pydantic.v1.errors import NoneIsAllowedError
# from dataclasses import asdict
from typing import Any, Literal
from model.todo_model import (
    KATEGORIEN_DICT,
    KEINE,
    KEINE_P,
    PRIORITAETEN_DICT,
    Category,
    Freizeit,
    Haushalt,
    Priority,
    Studium,
    ToDo,
)
from repo.todo_repo import TodoRepo
from datetime import date

#Betz wir haben keine ViewModels ist das trotzdem ok?
class TodoDetailPresenter:
    _modus: Literal["create", "edit"]

    def __init__(self, repo: TodoRepo):
        self.repo: TodoRepo = repo
        self._modus: Literal["create", "edit"] = "create"
        self._current_todo: ToDo | None = None

    @property
    def current_todo(self) -> ToDo | None:
        if self._current_todo:
            return self._current_todo
        return None

    def set_modus(self, modus: Literal["create", "edit"]):
        self._modus: Literal["create", "edit"] = modus

    @property
    def is_create_mode(self) -> bool:
        return self._modus == "create"

    @property
    def is_edit_mode(self) -> bool:
        return self._modus == "edit"

    def map_priority(self, value: str) -> Priority | None:
        return PRIORITAETEN_DICT.get(value)

    def map_category(self, value: str) -> Category | None:
        return KATEGORIEN_DICT.get(value)

    def build_extra(
        self, category: str, data: dict[str, Any]
    ) -> Studium | Haushalt | Freizeit | dict[str, Any] | None:
        if not data:
            return {}
        
        #Umwandlung von View=str zu Model=bool
        if category == "Studium":
            data["gruppenarbeit"] = self.von_str_zu_bool(data["gruppenarbeit"])
        elif category == "Haushalt":
            data["wiederkehrend"] = self.von_str_zu_bool(data["wiederkehrend"])
        
        mapping: dict[str, type[Studium] | type[Haushalt] | type[Freizeit]] = {
            "Studium": Studium,
            "Haushalt": Haushalt,
            "Freizeit": Freizeit,
        }
        cls: type[Studium] | type[Haushalt] | type[Freizeit] | None = mapping.get(
            category
        )
        if cls:
            return cls(**data)  # return Haushalt(wiederkehrend=False)
        raise TypeError(f"Ungültige Kategorie: {category}")

    # LOAD (Edit-Modus)
    def lade_todo(self, todo_id: int) -> dict[str, Any]:
        todo = self.repo.finde_todo_mit_id(todo_id)
        self._current_todo = todo
        if todo is None:
            return {}
        return {
            "Titel": todo.titel,
            "Notiz": todo.notiz,
            "Deadline": todo.deadline,
            "Kalender": todo.calendar,
            "Priorität": todo.priority.name if todo.priority else "keine",
            "Kategorie": todo.category.name if todo.category else "keine",
        }

    def save_todo(
        # hat Variablenwerte der View
        self,
        titel: str,
        notiz: str,
        deadline: date,
        calendar: str,
        priority: str,
        category: str,
        extra: dict[str, Any],
    ) -> None:

        if self._current_todo:  # EDIT
            todo = self._current_todo
            todo.titel = titel
            todo.notiz = notiz
            todo.deadline = deadline
            todo.calendar = self.von_str_zu_bool(
                calendar
            )  # ist Variablenwert von Model da in view str und im model bool
            todo.priority = Priority.from_str(priority) #TODO: Was ist hier das Problem?
            todo.category = Category.from_str(category)
            todo.extra = self.build_extra(category, extra)
            self.repo.update_todo(todo) 
        else:  # CREATE
            todo = ToDo(
                _todo_id=self.repo.naechste_id(),
                titel=titel,
                notiz=notiz,
                deadline=deadline,
                calendar=self.von_str_zu_bool(calendar),
                # priority=self.map_priority(priority),
                priority=Priority.from_str(priority),
                category=Category.from_str(category),
                extra=self.build_extra(category, extra),
            )
            self.repo.speichere(todo)

    def von_str_zu_bool(self, string: str | bool) -> bool:
        if isinstance(string, bool):
            return string
        if isinstance(string, str):
            lower_value = string.lower()
            if lower_value == "false":
                return False
            elif lower_value == "true":
                return True
        raise ValueError(f"Ungültiger Bool-String: {string}")
    
    def von_bool_zu_str(self, wert_b: bool) -> str:
        if wert_b:
            return "true"
        elif wert_b is False:
            return "false"
        raise ValueError(f"Ungültiger Wert: {wert_b}")
