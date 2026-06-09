# pyright: reportUnknownMemberType=false
<<<<<<< HEAD
from dataclasses import dataclass
from model.todo_model import TodoModel


@dataclass(frozen=True)
class TodoViewModel:
    nummer:int 
    titel:str
    notiz:str
    priority:str
    category:str
    erledigt:bool


class TodoPresenter:
    def __init__(self, model: TodoModel):
        self._model=model

    def alle_todos(self)->list[TodoViewModel]:
        todos_fuer_view: list[TodoViewModel] = []
        for todo in self._model.todos:
            todos_fuer_view.append(
                TodoViewModel(
                    todo.nummer, 
                    todo.titel, 
                    todo.notiz, 
                    todo.priority, 
                    todo.category, 
                    todo.erledigt))
        return todos_fuer_view
    
    def erledige_todo(self, nummer:int):
        for todo in self._model.todos:
            if todo.nummer == nummer:
                todo.markiere_als_erledigt()

    def loesche_todo(self, nummer:int):
        for todo in self._model.todos:
            if todo.nummer == nummer:
                self._model.todos.remove(todo)

"""class TodoPresenter:
    def __init__(self):
        self.model_todo=Todo()
        self.todo=self.model_todo
        self.notiz=self.model_todo.notiz
        self.priority=self.model_todo.priority
        self.category=self.model_todo.category
    
    def markiere_als_erledigt(self, todo: Todo, Aufgabe: ft.Card): #ist Flet dabei erlaubt, als Parameter ? 
        self.model_todo.markiere_als_erledigt(todo)
        self.controls.remove(Aufgabe)"""
    



    # def __init__(self, view,router):
    #     self.view = view
    #     self.router=router
    #     self.model = router.todos_model

    # def load_todos(self):
    #     todos = self.model.get_todos()
    #     ui_data=[ # für model übersetzen --> view sonst direkten zugriff auf model objekt
    #         f"{t.title}"
    #         for t in todos
    #         ]
    #     self.view.show_todos(ui_data)

    # def erzeuge_todo(self):
    #     self.router.go_to_erzeuge_todo()
    
    # def filtere_todo(self):
    #     self.router.go_to_filtere_todo()
=======
# #from model.todo_model import TodoModel
from model.general_model import GeneralModel,Todo

class TodoPresenter:
    def __init__(self):
        self.model=GeneralModel()
    
    def get_todo(self):
        return list(self.model.dummydaten)

    def erledige_todo(self,todo_e:Todo)->None:
        todo_e.erledigt=True
    
    def loesche_todo(self,todo_d:Todo)->None:
        if todo_d in self.model.todos:
            self.model.todos.remove(todo_d)

    def filter_todos(self, kat: str, prio: str, status: str)->list[Todo]:
        result=self.model.result
        if kat != "alle":
            gefiltert_nach_kategorie:list[Todo] = []
            for todo in result:
                if todo.category == kategorien_dict[kat]:
                    gefiltert_nach_kategorie.append(todo)
            result = gefiltert_nach_kategorie
        # Priorität
        if prio != "alle":
            gefiltert_nach_priority:list[Todo] = []
            for todo in result:
                if todo.priority == prioritäten_dict[prio]:
                    gefiltert_nach_priority.append(todo)

            result = gefiltert_nach_priority
        # Status
        if status == "offen":
            gefiltert_nach_status:list[Todo] = []
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
>>>>>>> origin/test-spaltung-for-Datenbanken
