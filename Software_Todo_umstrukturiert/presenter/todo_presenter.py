# pyright: reportUnknownMemberType=false
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