'''

# pyright: reportUnknownMemberType=false
from dataclasses import dataclass

@dataclass (frozen=True)
class Priority:
    name:str
    ausrufezeichen:str
    #schriftdicke
    #filternhilfe
keine=Priority("keine","X")
niedrig=Priority("niedrig","!")
mittel=Priority("mittel","!!")
hoch=Priority("hoch","!!!")

@dataclass (frozen=True)
class Category:
    name:str
    #schriftdicke
    #filternhilfe  
studium=Category("Studium")
haushalt=Category("Haushalt")
freizeit=Category ("Freizeit")

@dataclass
class Todo:
    nummer:int 
    titel:str
    notiz:str
    priority:Priority
    #deadline:datetime.date
    category:Category
    #calender: str
    _erledigt: bool=False

    @property
    def erledigt(self)->bool:
        return self._erledigt
    
    @property
    def offen(self)->bool:
        return not self._erledigt
    
    def markiere_als_erledigt(self):
        self._erledigt=True

    def gehoert_zu_kategorie(self, kategorie: Category)->bool:
        return self.category == kategorie

@dataclass
class ErstelleTodo:
    titel:str
    notiz:str
    priority_name:str
    #deadline:datetime.date
    category_name:str
@dataclass 
class TodoModel:
    todos: list[Todo] 

    def __init__(self):
              self.todos=[
                    Todo(1,"Hund bürsten","Hundebürste",keine,freizeit),
                    Todo(2,"Mathe","MaMo",mittel,studium),
                    Todo(3,"Wäsche waschen","",mittel, haushalt),
                    Todo(4,"Oma anrufen","gut",hoch,freizeit),
                    Todo(5,"Staubsaugen","",niedrig,haushalt),
                    Todo(6,"Softwareprojekt-Studyplaner","", hoch, studium),
                    Todo(7,"Einkaufen","",niedrig,haushalt),
                    Todo(8,"Freunde treffen","",mittel,freizeit),
                    Todo(9,"Buch lesen","",niedrig,freizeit),
                    Todo(10,"Sport machen","",mittel,freizeit),
                    Todo(11,"Projektarbeit","",hoch,studium),
                    Todo(12,"Auto waschen","",niedrig, haushalt),
                    Todo(13,"Gartenarbeit","",mittel,haushalt),
                    Todo(14,"Kino besuchen","",niedrig,freizeit),
                    Todo(15,"Hausaufgaben","",mittel,studium),
                    Todo(16,"Rechnung bezahlen","",hoch,haushalt),
                    Todo(17,"Spazieren gehen","",niedrig,freizeit),
                    Todo(18,"Prüfungsvorbereitung","",hoch,studium),
                    Todo(19,"Kochen","",mittel,haushalt),
                    Todo(20,"Musik hören","",niedrig,freizeit),
                    Todo(21,"Freizeitpark besuchen","",mittel,freizeit),
                    Todo(22,"Gitarre spielen","",niedrig,freizeit),
                    Todo(23,"Büro aufräumen","",mittel,haushalt),
                    Todo(24,"Vorlesung besuchen","",hoch,studium),
                    Todo(25,"Freunde anrufen","",niedrig,freizeit),
                    Todo(26,"Fenster putzen","",mittel,haushalt),
                    Todo(27,"Kunstprojekt","",hoch,studium),
                    Todo(28,"Fahrrad reparieren","",mittel,haushalt)
                ]
        
    def fuege_todo_hinzu(self, neue_Daten: ErstelleTodo):
        todo = Todo(
            nummer=len(self.todos) + 1,
            titel=neue_Daten.titel,
            notiz=neue_Daten.notiz,
            priority= self._priority_aus_name(neue_Daten.priority_name),
            category=self._category_aus_name(neue_Daten.category_name)
        )
        self.todos.append(todo)

    def entferne_todo(self, todo: Todo):
        self.todos.remove(todo)

    def _priority_aus_name(self, name: str)->Priority:
        if name == "keine":
            return keine
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
        
    @property
    def offene_todos(self)->list[Todo]:
        offene_todos: list[Todo] = [] 
        for todo in self.todos:
            if todo.offen:
                offene_todos.append(todo)
        return offene_todos
    
    @property
    def erledigte_todos(self)->list[Todo]:
        erledigte_todos: list[Todo] = [] 
        for todo in self.todos:
            if todo.erledigt:
                erledigte_todos.append(todo)
        return erledigte_todos
'''




# class TodosModel:
#     def __init__(self):
#         self._todos:list[ErzeugeTodoModel]=[]
    
#     def add_todo(self,todo:ErzeugeTodoModel):
#         self._todos.append(todo)

#     def get_todos(self)->list[ErzeugeTodoModel]:
#         return self._todos
    
#     def filter_todos(self, status:str, kategorie:str, datum:str)->list[ErzeugeTodoModel]: #anfang der Logik zum Filtern der Todos basierend auf den Kriterien
#         filtered_todos:list[ErzeugeTodoModel] = []
        
        # for todo in self._todos: #alle solt fuktionieren
        #     if status != "alle":
        #         filtered_todos.append(todo)
        #     elif status == "offen":
        #         if self.todo._done == False:
        #             filtered_todos.append(todo)
        #     elif status == "erledigt":
        #     filtered_todos = [todo for todo in filtered_todos if todo.status == "erledigt"]
        
        # if kategorie != "keine":
        #     filtered_todos = [todo for todo in filtered_todos if todo.kategorie == kategorie]
        
        # Datum-Filterlogik könnte hier hinzugefügt werden
        
        #return filtered_todos
    
    # def get_todos(self)->list[str]: 
        #return ["TD1", "TD2", "TD3"]