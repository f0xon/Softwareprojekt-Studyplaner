from model.ToDoListe_model import ToDoListModel, ToDoModel

class FiltereTodoPresenter:
    def __init__(self):
        self.model=ToDoListModel()
        self.kat:str="alle"
        self.prio:str="alle"
        self.status:str="alle"
    
    def set_kategorie(self, value:str):
        self.kat = value

    def set_priority(self, value:str):
        self.prio = value

    def set_status(self, value:str):
        self.status = value

    def get_filtered_todos(self)->list[ToDoModel]:
        return self.model.filter_todos(
            self.kat,
            self.prio,
            self.status
        )
