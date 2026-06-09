from dataclasses import dataclass
from datetime import date

# --- Domain Core ---
@dataclass(frozen=True)
class Priority:
    name: str
    ausrufezeichen: str
keine_p = Priority("keine", "X")
niedrig = Priority("niedrig", "!")
mittel = Priority("mittel", "!!")
hoch = Priority("hoch", "!!!")
prioritäten_dict={    
    "keine": keine_p,
    "niedrig": niedrig,
    "mittel": mittel,
    "hoch": hoch,}

@dataclass(frozen=True)
class Category:
    name: str
keine= Category("keine")
studium = Category("Studium")
haushalt = Category("Haushalt")
freizeit = Category("Freizeit")
kategorien_dict={
    "keine":keine,
    "Studium":studium,
    "Haushalt":haushalt,
    "Freizeit":freizeit
}

# --- Category Data Models ---
@dataclass
class Studium:
    modul: str
    gruppenarbeit: bool
@dataclass
class Haushalt:
    wiederkehrend: bool
@dataclass
class Freizeit:
    hobby: str
    ort: str

# --- MAIN TODO ---
#Todo hat eine Kategorie Todo hat optionale Zusatzdaten
@dataclass
class Todo:
    titel: str
    notiz: str
    priority: Priority
    deadline: date
    calendar:bool
    category: Category
    extra: Studium | Haushalt | Freizeit | None
    erledigt: bool = False

class GeneralModel:
    def __init__(self):
        self.todos:list[Todo]=[]
        self.dummydaten:list[Todo]=[
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
        self.result = self.dummydaten.copy()
    
    def add_todo(self,todo:Todo)->None:
        self.todos.append(todo)

   
    
    # def filter_todos(self, kat: str, prio: str, status: str)->list[Todo]:
    #     if kat != "alle":
    #         gefiltert_nach_kategorie:list[Todo] = []
    #         for todo in result:
    #             if todo.category == kategorien_dict[kat]:
    #                 gefiltert_nach_kategorie.append(todo)
    #         result = gefiltert_nach_kategorie
    #     # Priorität
    #     if prio != "alle":
    #         gefiltert_nach_priority:list[Todo] = []
    #         for todo in result:
    #             if todo.priority == prioritäten_dict[prio]:
    #                 gefiltert_nach_priority.append(todo)

    #         result = gefiltert_nach_priority
    #     # Status
    #     if status == "offen":
    #         gefiltert_nach_status:list[Todo] = []
    #         for todo in result:
    #             if todo.erledigt is False:
    #                 gefiltert_nach_status.append(todo)
    #         result = gefiltert_nach_status
    #     elif status == "erledigt":
    #         gefiltert_nach_status = []
    #         for todo in result:
    #             if todo.erledigt is True:
    #                 gefiltert_nach_status.append(todo)
    #         result = gefiltert_nach_status
    #     return result