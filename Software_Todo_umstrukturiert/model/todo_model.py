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
    farbe:str
keine= Category("keine","GREY_300")
studium = Category("Studium","BLUE_100")
haushalt = Category("Haushalt","DEEP_PURPLE_100")
freizeit = Category("Freizeit","TEAL_100")
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
class ToDoModel:
    _id: int
    titel: str = ""
    notiz: str = ""
    priority: Priority = keine_p
    deadline: date = date(2024, 1, 1)
    calendar:bool   = False
    category: Category  = keine
    extra: Studium | Haushalt | Freizeit |None=None
    _erledigt: bool = False

    @property
    def id(self)->int:
        return self._id

    @property
    def erledigt(self)->bool:
        return self._erledigt

    def erledige_todo(self)->None:
        if self._erledigt == False:
            self._erledigt = True
        elif self._erledigt == True:
            self._erledigt = False
