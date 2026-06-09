# pyright: reportUnknownMemberType=false
# #from model.todo_model import TodoModel
from model.ToDoListe_model import ToDoListModel,ToDoModel

#class ToDoPresenter:

 #   def __init__(self):
  #      self.model=ToDoModel()


class TodoListePresenter:
    def __init__(self, model: ToDoListModel):
        self.model = model

    def get_todos(self):
        return list(self.model.dummydaten)
    

    def erledige_todo(self, id: int)->None:
        for todo in self.model.dummydaten:
            if todo.id == id:
                todo.erledige_todo()


    def loesche_todo(self,id: int)->None:
        for todo in self.model.dummydaten:
            if todo.id == id:
                self.model.loesche_todo(todo)

    def filter_todos(self, kat: str, prio: str, status: str)->list[ToDoModel]:
        result=self.model.result
        if kat != "alle":
            gefiltert_nach_kategorie:list[ToDoModel] = []
            for todo in result:
                if todo.category == kategorien_dict[kat]:
                    gefiltert_nach_kategorie.append(todo)
            result = gefiltert_nach_kategorie
        # Priorität
        if prio != "alle":
            gefiltert_nach_priority:list[ToDoModel] = []
            for todo in result:
                if todo.priority == prioritäten_dict[prio]:
                    gefiltert_nach_priority.append(todo)

            result = gefiltert_nach_priority
        # Status
        if status == "offen":
            gefiltert_nach_status:list[ToDoModel] = []
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
