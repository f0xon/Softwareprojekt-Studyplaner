# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.todo_presenter import TodoPresenter

class TodoView(ft.Column):

    def __init__(self):
        super().__init__()
        self.presenter = TodoPresenter()

    def build_ui(self)
        for todo in self.presenter.todos:
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
                                    tooltip="Erledigt",
                                    # on_click=self.on_button_clicked_done
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.INFO_OUTLINE,
                                    tooltip="Details",
                                    # on_click=self.on_button_clicked_details
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    tooltip="Löschen",
                                    data=todo
                                    on_click=self.on_button_clicked_delete
                                )
                            ],
                        ),
                    )
                )
            )
    
    def on_button_clicked_delete(self,e):
        todo = e.control.data
        self.presenter.loesche_todo(todo)
        self.controls.clear()
        self.build_ui()
        self.update()