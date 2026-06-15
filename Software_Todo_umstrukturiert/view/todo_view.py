# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.todo_presenter import TodoListePresenter
from presenter.filtere_todo_presenter import FiltereTodoPresenter
from presenter.erzeuge_todo_presenter import TodoDetailPresenter



class TodoView(ft.Column):

    def __init__(self, presenter_todo: TodoListePresenter,presenter_filtere:FiltereTodoPresenter,presenter_detail:TodoDetailPresenter):
        super().__init__()
        self.presenter_todo = presenter_todo
        self.presenter_filtere=presenter_filtere
        self.presenter_detail= presenter_detail
        self.build_ui()

    def build_ui(self):
        self.controls.clear()
        alle_todos=self.presenter_filtere.get_filtered_todos()
        for todo in alle_todos:
            self.controls.append(
                ft.Card(
                    bgcolor= getattr(ft.Colors, todo.category.farbe, ft.Colors.GREY_500),
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
                                    tooltip="Priorität: "+ todo.priority.name,
                                    style=ft.ButtonStyle(
                                        color=ft.Colors.RED_ACCENT_700,
                                        bgcolor=ft.Colors.TRANSPARENT,
                                    )
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DONE,
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.WHITE,
                                        ),
                                    tooltip="Erledigt" if todo.erledigt else "Unerledigt",
                                    icon_color=ft.Colors.BLUE if todo.erledigt else ft.Colors.GREY,
                                    data=todo.id,
                                    on_click=self.on_button_clicked_done
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.INFO_OUTLINE,
                                    tooltip="Details",
                                    data=todo.id,
                                    on_click=self.on_button_clicked_detail
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    tooltip="Löschen",
                                    data=todo.id,
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
        todo_id: int = e.control.data
        self.presenter_todo.erledige_todo(todo_id)
        self.rebuild()

    def on_button_clicked_delete(self,e):
        todo_id: int = e.control.data
        print("View löscht Todo mit ID:", todo_id,type(todo_id))
        self.presenter_todo.loesche_todo(todo_id)
        print("View hat Todo gelöscht")
        self.rebuild()

    def on_button_clicked_detail(self,e):
        todo_id: int = e.control.data
        self.presenter_detail.lade_todo(todo_id)
        self.rebuild()
