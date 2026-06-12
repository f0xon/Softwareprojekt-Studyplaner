from dataclasses import dataclass
from datetime import date
from model.todo_model import ToDoModel
from model.todo_model import Priority, hoch, mittel, niedrig, keine_p, prioritäten_dict
from model.todo_model import Category, Studium, Haushalt, Freizeit, keine, studium, haushalt, freizeit, kategorien_dict

class ToDoListModel:
    def __init__(self):
        self.todos:list[ToDoModel]=[]
        self.dummydaten:list[ToDoModel]=[
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
            ),
        ]
        self.result = self.dummydaten.copy()
    
    def add_todo(self,todo:ToDoModel)->None:
        self.dummydaten.append(todo)

    def loesche_todo(self, todo: ToDoModel):
        self.dummydaten.remove(todo)
        print(self.dummydaten)

    def _priority_aus_name(self, name: str)->Priority:
        if name == "keine":
            return keine_p
        elif name == "niedrig":
            return niedrig
        elif name == "mittel":
            return mittel
        elif name == "hoch":
            return hoch
        else:
            raise ValueError(f"Ungültiger Prioritätsname: {name}")
        
    def _category_aus_name(self, name: str)->Category:
        if name == "Studium":
            return studium
        elif name == "Haushalt":
            return haushalt
        elif name == "Freizeit":
            return freizeit
        else:
            raise ValueError(f"Ungültiger Kategoriename: {name}")




    def filter_todos(self, kat: str, prio: str, status: str)->list[ToDoModel]:
        result=self.dummydaten.copy()
        if kat != "alle":
            gefiltert_nach_kategorie:list[ToDoModel] = []
            for todo in result:
                if todo.category == kategorien_dict[kat]:
                    gefiltert_nach_kategorie.append(todo)
            result = gefiltert_nach_kategorie
        # Priorität
        if prio != "alle":
            gefiltert_nach_priority:list[ToDoModel] = []
            for todo in result:
                if todo.priority == prioritäten_dict[prio]:
                    gefiltert_nach_priority.append(todo)

            result = gefiltert_nach_priority
        # Status
        if status == "offen":
            gefiltert_nach_status:list[ToDoModel] = []
            for todo in result:
                if todo.erledigt is False:
                    gefiltert_nach_status.append(todo)
            result = gefiltert_nach_status
        elif status == "erledigt":
            gefiltert_nach_status = []
            for todo in result:
                if todo.erledigt is True:
                    gefiltert_nach_status.append(todo)
            result = gefiltert_nach_status
        return result
        # wenn liste leer keine todos mit diesen filtrn vorhanden