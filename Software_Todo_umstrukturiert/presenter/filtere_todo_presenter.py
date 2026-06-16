from model.ToDoListe_model import ToDoListModel, ToDoModel
from repo import TodoRepo

class FiltereTodoPresenter:
    def __init__(self,model:ToDoListModel,repo:TodoRepo):
        self.model=model
        self.repo=repo
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
        result: list[ToDoModel]= self.repo.filtere_todos(self.kat,self.prio,self.status)
        print("Debug", result)
        print("")
        return result
