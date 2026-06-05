from dataclasses import dataclass

@dataclass
class KeineKategorie:
    titel:str
    notiz:str
    priority:str
    deadline:datetime.date
    category:str

@dataclass
class StudiumKategorie(KeineKategorie):
    modul:str
    gruppenarbeit:bool

@dataclass
class Haushalt(KeineKategorie):
    wiederkehrend: bool

@dataclass
class Freizeit(KeineKategorie):
    hobby:str
    ort:str
 
class ErzeugeTodoModel:
