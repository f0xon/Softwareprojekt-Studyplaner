<<<<<<< HEAD
# pyright: reportUnknownMemberType=false
from model.todo_model import TodoModel

class FiltereTodoPresenter:
    def __init__(self, model: TodoModel):
        self._model = model
=======
from model.general_model import GeneralModel, Todo

class FiltereTodoPresenter:
    def __init__(self):
        self.model=GeneralModel()
        self.kat:str="alle"
        self.prio:str="alle"
        self.status:str="alle"
    
    def set_kategorie(self, value:str):
        self.kat = value

    def set_priority(self, value:str):
        self.prio = value

    def set_status(self, value:str):
        self.status = value

    def get_filtered_todos(self)->list[Todo]:
        return self.model.filter_todos(
            self.kat,
            self.prio,
            self.status
        )
>>>>>>> origin/test-spaltung-for-Datenbanken
