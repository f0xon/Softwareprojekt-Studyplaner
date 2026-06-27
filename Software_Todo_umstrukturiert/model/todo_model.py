from __future__ import annotations
from dataclasses import dataclass
from datetime import date


# --- Domain Core ---
@dataclass(frozen=True)
class Priority:
    name: str
    symbol: str

    @classmethod
    def from_str(cls, as_str: str) -> Priority | None:
        if as_str in PRIORITAETEN_DICT:
            return PRIORITAETEN_DICT[as_str]
        else:
            return KEINE_P


KEINE_P = Priority("keine", "X")
NIEDRIG = Priority("niedrig", "!")
MITTEL = Priority("mittel", "!!")
HOCH = Priority("hoch", "!!!")

PRIORITAETEN_DICT: dict[str, Priority] = {
    "keine": KEINE_P,
    "niedrig": NIEDRIG,
    "mittel": MITTEL,
    "hoch": HOCH,
}


@dataclass(frozen=True)
class Category:
    name: str
    farbe: str

    @classmethod
    def from_str(cls, as_str: str) -> Category | None:
        if as_str in KATEGORIEN_DICT:
            return KATEGORIEN_DICT[as_str]
        else:
            return KEINE


KEINE = Category("keine", "GREY_300")
STUDIUM = Category("Studium", "BLUE_100")
HAUSHALT = Category("Haushalt", "DEEP_PURPLE_100")
FREIZEIT = Category("Freizeit", "TEAL_100")

KATEGORIEN_DICT = {
    "keine": KEINE,
    "Studium": STUDIUM,
    "Haushalt": HAUSHALT,
    "Freizeit": FREIZEIT,
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


@dataclass
class ToDo:
    _todo_id: int
    titel: str
    notiz: str
    priority: Priority
    deadline: date
    calendar: bool
    category: Category
    extra: Studium | Haushalt | Freizeit | None = None  # hat optionalen Zusatzdaten
    _erledigt: bool = False

    @property
    def todo_id(self) -> int:
        return self._todo_id

    @property
    def erledigt(self) -> bool:
        return self._erledigt

    def toggle_erledigt_todo(self) -> None:
        self._erledigt = not self._erledigt
