from erzeuge_todo_view import ErzeugeTodoView
import datetime

class ErzeugeTodoView_Studuium(ErzeugeTodoView):
    def __init__(self, router):
        super().__init__(router)
        self.category.value="Studium"
        self.fach: str = ""
        self.dozent: str = ""
        self.raum: str = ""
        self.abgebedatum: datetime.date

        self.control=ft.Column(