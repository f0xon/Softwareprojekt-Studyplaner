

class ErzeugeTodoKategoriePresenter:
    def __init__(self, router):
        self.router=router

    def erzeuge_todo_view(self,kategorie:str):
         self.router.go_to_erzeuge_todo_view(kategorie)