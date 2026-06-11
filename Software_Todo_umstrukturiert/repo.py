from typing import Protocol, Any
from model.todo_model import ToDoModel, hoch, mittel, niedrig, keine_p, studium, keine, haushalt, freizeit, kategorien_dict, prioritäten_dict, Category, Studium, Haushalt, Freizeit
from model.ToDoListe_model import ToDoListModel
from datetime import date

class TodoRepo(Protocol):
    def speichere(self,todo:ToDoModel)->None:
        ...
    def erledige_todo(self,todo:ToDoModel)->None:
        ...
    def lade_alle(self)->ToDoListModel:
        ...
    # def lade_todo(self,name:str):
    #     ...

class MongoTodoRepo(TodoRepo):
    def __init__(self, db: Database[Any]) -> None:
        self.db = db

    def speichere(self, todo: ToDoModel):
        self.db.todos.insert_one(asdict(todo))
    
    def lade_todo(self, todo_id: int) -> ToDoModel | None:
        todo = self.db.todos.find_one(
            {"_id": todo_id},
            projection={"_id": False}
        )
        if todo is None:
            return None
        return ToDoModel(**todo)


    def erledige_todo(self, todo_id: int) -> None:
        todo = self.db.todos.find_one({"_id": todo_id})
        neuer_status = not todo["erledigt"]
        todo.update_one(
            {"_id": todo_id},
            {"$set": {"erledigt": neuer_status}}
        )

    def lade_alle(self) -> ToDoListModel:
        _todos: list[ToDoModel] = []
        for todo in self.db.todos.find(projection={"_id": False}):
            todo_obj = ToDoModel(**todo)
            _todos.append(todo_obj)
        return ToDoListModel(todos=_todos)

class InMemoryTodoRepo(TodoRepo):
    _todos:list[ToDoModel]
    def __init__(self):
        self._todos=[
            ToDoModel(_id=1,
                titel="Mathe lernen",
                notiz="Kapitel 3 üben",
                priority=hoch,
                deadline=date(2026, 6, 10),
                calendar=False,
                category=studium,
                extra=Studium(
                    modul="Mathe 2",
                    gruppenarbeit=True
                ),
                erledigt=False,
            ),
            ToDoModel(_id=2,
                titel="Hund bürsten",
                notiz="Hundebürste",
                priority=keine_p,
                deadline=date(2026, 6, 10),
                calendar=False,
                category=freizeit,
                extra=Freizeit(
                    hobby="Hundepflege",
                    ort="Zuhause"
                ),
                erledigt=False,
            ),
            ToDoModel(_id=3,
                titel="Mathe",
                notiz="MaMo",
                priority=mittel,
                deadline=date(2026, 6, 11),
                calendar=False,
                category=studium,
                extra=Studium(
                    modul="Mathematik",
                    gruppenarbeit=False
                ),
                erledigt=False,
            ),
            ToDoModel(_id=4,
                titel="Wäsche waschen",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 12),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=True
                ),
                erledigt=False,
            ),
            ToDoModel(_id=5,
                titel="Oma anrufen",
                notiz="gut",
                priority=hoch,
                deadline=date(2026, 6, 13),
                calendar=False,
                category=freizeit,
                extra=Freizeit(
                    hobby="Familie",
                    ort="Telefon"
                ),
                erledigt=False,
            ),
        ToDoModel(_id=6,
                titel="Staubsaugen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 14),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=True
                ),
                erledigt=False,
            ),
            ToDoModel(_id=7,
                titel="Softwareprojekt-Studyplaner",
                notiz="",
                priority=hoch,
                deadline=date(2026, 6, 15),
                calendar=False,
                category=studium,
                extra=Studium(
                    modul="Software Engineering",
                    gruppenarbeit=True
                ),
                erledigt=False,
            ),
            ToDoModel(_id=8,
                titel="Einkaufen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 16),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=False
                ),
                erledigt=False,
            ),
            ToDoModel(_id=9,
                titel="Freunde treffen",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 17),
                calendar=False,
                category=freizeit,
                extra=Freizeit(
                    hobby="Treffen",
                    ort="Stadt"
                ),
                erledigt=False,
            ),
            ToDoModel(_id=10,
                titel="Buch lesen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 18),
                calendar=False,
                category=freizeit,
                extra=Freizeit(
                    hobby="Lesen",
                    ort="Wohnzimmer"
                ),
                erledigt=False,
            ),
            ToDoModel(_id=11,
                titel="Sport machen",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 19),
                calendar=False,
                category=freizeit,
                extra=Freizeit(
                    hobby="Fitness",
                    ort="Fitnessstudio"
                ),
                erledigt=False,
            ),
            ToDoModel(_id=12,
                titel="Projektarbeit",
                notiz="",
                priority=hoch,
                deadline=date(2026, 6, 20),
                calendar=False,
                category=studium,
                extra=Studium(
                    modul="Projektmanagement",
                    gruppenarbeit=True
                ),
                erledigt=False,
            ),
            ToDoModel(_id=13,
                titel="Auto waschen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 21),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=False
                ),
                erledigt=False,
            ),
            ToDoModel(_id=14,
                titel="Gartenarbeit",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 22),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=True
                ),
                erledigt=False,
            ),
            ToDoModel(_id=15,
                titel="Kino besuchen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 23),
                calendar=False,
                category=freizeit,
                extra=Freizeit(
                    hobby="Filme",
                    ort="Kino"
                ),
                erledigt=False,
            ),
            ToDoModel(_id=16,
                titel="Hausaufgaben",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 24),
                calendar=False,
                category=studium,
                extra=Studium(
                    modul="Informatik",
                    gruppenarbeit=False
                ),
                erledigt=False,
            ),
        ]
    
    def speichere(self,todo:ToDoModel)->None:
        self._todos.append(todo)

    def erledige_todo(self, id: int)->None:
        _todos: list[ToDoModel] = []
        for todo in _todos:
            if todo.id == id:
                if todo.erledigt == False:
                    todo.erledigt = True
                elif todo.erledigt == True:
                    todo.erledigt = False
                        

    def lade_alle(self)->ToDoListModel:
        return ToDoListModel(todos=_todos)