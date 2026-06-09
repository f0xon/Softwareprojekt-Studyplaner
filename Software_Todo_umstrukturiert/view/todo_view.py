# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.todo_presenter import TodoPresenter
from view.filtere_todo_view import FiltereTodoView


class TodoView(ft.Column):

<<<<<<< HEAD
    def __init__(self, presenter: TodoPresenter):
        super().__init__(
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        self.presenter = presenter
        self.build_ui()

    def build_ui(self):
        self.controls.clear()

        for todo in self.presenter.alle_todos():
=======
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
>>>>>>> origin/test-spaltung-for-Datenbanken
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
                                    data=todo.nummer,
                                    on_click=self.on_button_clicked_done
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.INFO_OUTLINE,
                                    tooltip="Details",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    tooltip="Löschen",
                                    data=todo.nummer,
                                    on_click=self.on_button_clicked_delete
                                )
                            ],
                        ),
                    )
                )
            )
<<<<<<< HEAD

    def on_button_clicked_done(self, e):
        nummer = e.control.data
        self.presenter.erledige_todo(nummer)
        self.build_ui()
        self.update()

    def on_button_clicked_delete(self, e):
        nummer = e.control.data
        self.presenter.loesche_todo(nummer)
        self.build_ui()
        self.update()
        
        #             content=ft.Container(
        #                 width=450,
        #                 padding=10,
        #                 content=ft.Row(
        #                         controls=[
        #                             ft.IconButton(ft.Icons.DONE), #,on_click=self.on_button_clicked_done noch nicht implementiert
        #                             ft.Text("Name"),
        #                             ft.Text(todo.titel),
        #                             ft.IconButton(ft.Icons.INFO), #noch nicht implementiert
        #                             ft.Text("Notiz"),
        #                             ft.Text(todo.notiz)
        #                         ]
        #                     )
        #                 )
        #             )
        #         )
            
            


            # self.controls.append(ft.Column([
            #     ft.ListTile(
            #         title=todo.titel,#titel
            #         subtitle=todo.notiz,#categorie
            #         trailing=ft.Text(""),#datum
            #         bgcolor=ft.Colors.SURFACE_CONTAINER_LOW
            #     )
            # ]))

    # def on_button_clicked_add(self):
    #     self.presenter.erzeuge_todo()
    
    # def on_button_clicked_filter(self):
    #     self.presenter.filtere_todo()
    

    # def did_mount(self):
    #     self.presenter.load_todos()

    # def show_todos(self, todos:list[str]):
    #     self.todo_list.controls.clear()

    #     for todo in todos:
    #         self.todo_list.controls.append(ft.Text(todo))

    #     self.update()

=======
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
>>>>>>> origin/test-spaltung-for-Datenbanken
