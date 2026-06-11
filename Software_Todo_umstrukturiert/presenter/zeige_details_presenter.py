from model.ToDoListe_model import ToDoListModel
from repo import TodoRepo

class ZeigeDetailsPresenter:
    def __init__(self,model: ToDoListModel,repo:TodoRepo):
        self.model=model
        self.repo=repo
    def show_details(self,todo):
        