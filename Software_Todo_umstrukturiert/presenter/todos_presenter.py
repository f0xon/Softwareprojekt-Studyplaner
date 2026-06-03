# pyright: reportUnknownMemberType=false
from model.todos_model import TodosModel


class TodosPresenter:

    def __init__(self, view,router):
        self.view = view
        self.router=router
        self.model = router.todos_model

    def load_todos(self):
        todos = self.model.get_todos()
        ui_data=[ # für model übersetzen --> view sonst direkten zugriff auf model objekt
            f"{t.title}"
            for t in todos
            ]
        self.view.show_todos(ui_data)

    def erzeuge_todo(self):
        self.router.go_to_erzeuge_todo()
    
    def filtere_todo(self):
        self.router.go_to_filtere_todo()