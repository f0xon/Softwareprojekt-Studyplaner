# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.todo_presenter import TodoListePresenter
from presenter.filtere_todo_presenter import FiltereTodoPresenter



class TodoView(ft.Column):

    def __init__(self, presenter_todo: TodoListePresenter,presenter_filtere:FiltereTodoPresenter):
        super().__init__()
        self.presenter_todo = presenter_todo
        self.presenter_filtere=presenter_filtere
        self.build_ui()

    def build_ui(self):
        self.controls.clear()
        alle_todos=self.presenter_filtere.get_filtered_todos()
        for todo in alle_todos:
            self.controls.append(
                ft.Card(
                    elevation=2,
                    content=ft.ListTile(
                        title=ft.Text(
                            todo.titel,
                            weight=ft.FontWeight.BOLD
                        ),
                        subtitle=ft.Text(
                            todo.notiz if todo.notiz else "Keine Notiz"
                        ),
                        trailing=ft.Row(
                            tight=True,
                            controls=[
                                ft.Button(
                                    todo.priority.ausrufezeichen,
                                    tooltip="Priorität"
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DONE,
                                    tooltip="Erledigt" if todo.erledigt else "Unerledigt",
                                    icon_color=ft.Colors.BLUE if todo.erledigt else ft.Colors.GREY,
                                    data=todo._id,
                                    on_click=self.on_button_clicked_done
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.INFO_OUTLINE,
                                    tooltip="Details",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    tooltip="Löschen",
                                    data=todo._id,
                                    on_click=self.on_button_clicked_delete
                                )
                            ],
                        ),
                    )
                )
            )

    def rebuild(self):
        self.controls.clear()
        self.build_ui()
        self.update()

    def on_button_clicked_done(self,e):
        todo= e.control.data
        self.presenter_todo.erledige_todo(todo)
        self.rebuild()

    def on_button_clicked_delete(self,e):
        todo = e.control.data
        self.presenter_todo.loesche_todo(todo)
        self.rebuild()
