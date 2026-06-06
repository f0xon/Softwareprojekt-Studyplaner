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
    titel:str
    notiz:str
    priority:Priority
    #deadline:datetime.date
    category:Category
    #calender: str
    erledigt: bool=False


class TodoModel:
        def __init__(self):
              self.todos=[
                    Todo("Hund bürsten","Hundebürste",keine,freizeit),
                    Todo("Mathe","MaMo",mittel,studium),
                    Todo("Wäsche waschen","",mittel, haushalt),
                    Todo("Oma anrufen","gut",hoch,freizeit),
                    Todo("Staubsaugen","",niedrig,haushalt),
                    Todo("Softwareprojekt-Studyplaner","", hoch, studium),
                    Todo("Einkaufen","",niedrig,haushalt),
                    Todo("Freunde treffen","",mittel,freizeit),
                    Todo("Buch lesen","",niedrig,freizeit),
                    Todo("Sport machen","",mittel,freizeit),
                    Todo("Projektarbeit","",hoch,studium),
                    Todo("Auto waschen","",niedrig, haushalt),
                    Todo("Gartenarbeit","",mittel,haushalt),
                    Todo("Kino besuchen","",niedrig,freizeit),
                    Todo("Hausaufgaben","",mittel,studium),
                    Todo("Rechnung bezahlen","",hoch,haushalt),
                    Todo("Spazieren gehen","",niedrig,freizeit),
                    Todo("Prüfungsvorbereitung","",hoch,studium),
                    Todo("Kochen","",mittel,haushalt),
                    Todo("Musik hören","",niedrig,freizeit),
                    Todo("Freizeitpark besuchen","",mittel,freizeit),
                    Todo("Gitarre spielen","",niedrig,freizeit),
                    Todo("Büro aufräumen","",mittel,haushalt),
                    Todo("Vorlesung besuchen","",hoch,studium),
                    Todo("Freunde anrufen","",niedrig,freizeit),
                    Todo("Fenster putzen","",mittel,haushalt),
                    Todo("Kunstprojekt","",hoch,studium),
                    Todo("Fahrrad reparieren","",mittel,haushalt)
                ]



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