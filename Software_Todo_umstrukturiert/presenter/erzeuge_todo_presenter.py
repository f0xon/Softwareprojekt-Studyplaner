# from pydantic.v1.errors import NoneIsAllowedError
# from dataclasses import asdict
from typing import Any, Literal

from model.ToDoListe_model import ToDoListModel, ToDoModel
from model.todo_model import Category, Priority, PRIORITAETEN_DICT, KATEGORIEN_DICT, KEINE_P
from model.todo_model import Studium, Haushalt, Freizeit
from repo import TodoRepo
from datetime import date


# class ErzeugeTodoPresenter:
class TodoDetailPresenter:
    _modus: Literal["create", "edit"]
    _model: ToDoListModel

    def __init__(self, model: ToDoListModel, repo: TodoRepo):
        self._model = model
        self.repo = repo
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

    def set_modus(self, modus: Literal["create", "edit"]):
        self._modus = modus

    def map_priority(self, value: str) -> Priority | None:  # ?eigentlich nur keine_p, niedrig, mittel, hoch
        # return prioritäten_dict[value]
        return PRIORITAETEN_DICT.get(value, KEINE_P)

    def map_category(self, value: str) -> Category|None:
        return KATEGORIEN_DICT.get(value,KEINE)

    def build_extra(
        self, category: str, data: dict[str, Any]
    ) -> Studium | Haushalt | Freizeit | None:
        if not data:
            return None
        mapping: dict[str, type[Studium] | type[Haushalt] | type[Freizeit]] = {
            "Studium": Studium,
            "Haushalt": Haushalt,
            "Freizeit": Freizeit,
        }
        cls: type[Studium] | type[Haushalt] | type[Freizeit] | None = mapping.get(
            category
        )
        if cls:
            return cls(**data)  # return zB für Studium "Studium"=Studium?
        else:
            return None

    # LOAD (Edit-Modus)
    def lade_todo(self, todo_id: int) -> None:
        todo = self.repo.finde_todo_mit_id(todo_id)
        self._current_todo = todo

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
            todo.calendar = self.von_str_zu_bool(calendar)  # ist Variablenwert von Model da in view str und im model bool
            # todo.priority = self.map_priority(priority)
            todo.priority = Priority.from_str(priority)
            todo.category = self.map_category(category)
            todo.extra = self.build_extra(category, extra)
        else:  # CREATE
            todo = ToDoModel(
                _id=self.repo.naechste_id(),
                titel=titel,
                notiz=notiz,
                deadline=deadline,
                calendar=self.von_str_zu_bool(calendar),
                priority=self.map_priority(priority),
                category=self.map_category(category),
                extra=self.build_extra(category, extra),
            )
            self.repo.speichere(todo)

    def von_str_zu_bool(self, string: str) -> bool:
        if string == "false":
            return False
        elif string == "true":
            return True
        raise ValueError(f"Ungültiger Bool-String: {string}")

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
