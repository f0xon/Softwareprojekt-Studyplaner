# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.todo_presenter import TodoPresenter
from view.filtere_todo_view import FiltereTodoView


class TodoView(ft.Column):

    def __init__(self):
        super().__init__()
        self.presenter = TodoPresenter()
        self.filter_view=FiltereTodoView()
        self.build_ui()

    def build_ui(self):
        category = self.filter_view.category.value
        prio = self.filter_view.priority.value
        status = self.filter_view.status.value
        todos = self.presenter.filter_todos(category, prio, status)
        for todo in todos:
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
                                    on_click=self.on_button_clicked_done
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.INFO_OUTLINE,
                                    tooltip="Details",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    tooltip="Löschen",
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
        self.presenter.erledige_todo(todo)
        self.rebuild()

    def on_button_clicked_delete(self,e):
        todo = e.control.data
        self.presenter.loesche_todo(todo)
        self.rebuild()
