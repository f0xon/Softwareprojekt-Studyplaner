# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
from model.todo_model import ToDo
import flet as ft
from presenter.todo_presenter import TodoListePresenter
from presenter.filtere_todo_presenter import FiltereTodoPresenter


class TodoView(ft.Column):
    def __init__(
        self,
        presenter_todo: TodoListePresenter,
        presenter_filtere: FiltereTodoPresenter,
    ):
        super().__init__()
        self.presenter_todo: TodoListePresenter = presenter_todo
        self.presenter_filtere: FiltereTodoPresenter = presenter_filtere
        self.build_ui()

    def build_ui(self):
        self.controls.clear()
        alle_todos: list[ToDo] = self.presenter_filtere.get_filtered_todos()

        if self.presenter_todo.ist_liste_leer():
            self.controls.append(
                ft.Card(
                    bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                    shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                    content=ft.Container(
                        width=450,
                        padding=10,
                        content=ft.Column(
                            controls=[
                                ft.Row(controls=[ft.Icon(ft.Icons.INFO_OUTLINE_ROUNDED, size=50)]),
                                ft.Row(controls=[ft.Text(
                                    "Keine Todos verfügbar",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                )]),
                            ]
                        ),
                    ),
                )
            )
        elif (
            alle_todos == []
        ):  
            self.controls.append(
                ft.Card(
                    bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                    shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                    content=ft.Container(
                        width=450,
                        padding=10,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.INFO_OUTLINE_ROUNDED, size=50),
                                        ft.Container(expand=True),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            "Keine Todos mit ausgewählten Filtern vorhanden",
                                            size=20,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Container(expand=True),
                                    ]
                                ),
                            ]
                        ),
                    ),
                )
            )
        else:
            for todo in alle_todos:
                self.controls.append(
                    ft.Card(
                        bgcolor=getattr(
                            ft.Colors, todo.category.farbe, ft.Colors.GREY_500
                        ),
                        elevation=2,
                        content=ft.ListTile(
                            title=ft.Text(todo.titel, weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text(
                                todo.notiz if todo.notiz else "Keine Notiz"
                            ),
                            trailing=ft.Row(
                                tight=True,
                                controls=[
                                    ft.Button(
                                        todo.priority.symbol,
                                        tooltip="Priorität: " + todo.priority.name,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.RED_ACCENT_700,
                                            bgcolor=ft.Colors.TRANSPARENT,
                                        ),
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DONE,
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.WHITE,
                                        ),
                                        tooltip="Erledigt"
                                        if todo.erledigt
                                        else "Unerledigt",
                                        icon_color=ft.Colors.BLUE
                                        if todo.erledigt
                                        else ft.Colors.GREY,
                                        data=todo.todo_id,
                                        on_click=self.on_button_clicked_done,
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.INFO_OUTLINE,
                                        tooltip="Details",
                                        data=todo.todo_id,
                                        on_click=self.on_button_clicked_detail,
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE_OUTLINE,
                                        tooltip="Löschen",
                                        data=todo.todo_id,
                                        on_click=self.on_button_clicked_delete,
                                    ),
                                ],
                            ),
                        ),
                    )
                )

    def rebuild(self):
        self.controls.clear()
        self.build_ui()
        self.update()

    def on_button_clicked_done(self, e: ft.Event[ft.IconButton]):
        todo_id: int = e.control.data
        self.presenter_todo.erledige_todo(todo_id)
        self.rebuild()

    def on_button_clicked_delete(self, e: ft.Event[ft.IconButton]):
        todo_id: int = e.control.data
        self.presenter_todo.loesche_todo(todo_id)
        self.rebuild()

    def on_button_clicked_detail(self, e: ft.Event[ft.IconButton]):
        todo_id: int = e.control.data
        if isinstance(
            self.page, ft.Page
        ):  # für den TypeChecker, eigentlich immer der Fall
            self.page.go("/erzeugeTodo?id=" + str(todo_id))
        self.rebuild()
