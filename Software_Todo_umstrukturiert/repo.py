from typing import Protocol
from model.general_model import Todo,hoch,mittel,niedrig,freizeit,studium,keine_p,haushalt,mittel, Studium,keine,Freizeit,Haushalt
from datetime import date

class TodoRepo(Protocol):
    def speichere(self,todo:Todo):
        ...
<<<<<<< Updated upstream
    def lade_alle(self):
=======
    def erledige_todo(self,todo_id:str)->None:
>>>>>>> Stashed changes
        ...
    def lade_todo(self,name:str):
        ...

class MongoPersonTodoRepo(TodoRepo):
    def __init__(self, db: Database[Any]) -> None:
        self.db = db

    def speichere(self, todo: Todo):
        self.db.todos.insert_one(asdict(todo))
    
    def lade_alle(self) -> list[Todo]:
        todos: list[Todo] = []
        for todo in self.db.todos.find(projection={"_id": False}):
            todo_obj = Todo(**todo)
            todos.append(todo_obj)
        return todos

class InMemoryTodoRepo(TodoRepo):
    _todos:list[Todo]
    def __init__(self):
        self._todos=[
            Todo(
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
            ),
            Todo(
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
            ),
            Todo(
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
            ),
            Todo(
                titel="Wäsche waschen",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 12),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=True
                ),
            ),
            Todo(
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
            ),
            Todo(
                titel="Staubsaugen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 14),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=True
                ),
            ),
            Todo(
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
            ),
            Todo(
                titel="Einkaufen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 16),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=False
                ),
            ),
            Todo(
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
            ),
            Todo(
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
            ),
            Todo(
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
            ),
            Todo(
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
            ),
            Todo(
                titel="Auto waschen",
                notiz="",
                priority=niedrig,
                deadline=date(2026, 6, 21),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=False
                ),
            ),
            Todo(
                titel="Gartenarbeit",
                notiz="",
                priority=mittel,
                deadline=date(2026, 6, 22),
                calendar=False,
                category=haushalt,
                extra=Haushalt(
                    wiederkehrend=True
                ),
            ),
            Todo(
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
            ),
            Todo(
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
            ),
        ]
    def speichere(self,todo:Todo)->None:
        self._todos.append(todo)

<<<<<<< Updated upstream
    def lade_alle(self)->list[Todo]:
        return self._todos
=======
    def erledige_todo(self, id: int)->None:
        _todos: list[ToDoModel] = []
        for todo in _todos:
            if todo.id == id:
                if todo.erledigt == False:
                    todo.erledigt = True
                elif todo.erledigt == True:
                    todo.erledigt = False
                        

    def lade_alle(self)->ToDoListModel:
        return ToDoListModel(todos=self._todos)
>>>>>>> Stashed changes
