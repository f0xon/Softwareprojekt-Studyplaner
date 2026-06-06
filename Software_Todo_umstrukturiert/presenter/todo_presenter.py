# pyright: reportUnknownMemberType=false
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