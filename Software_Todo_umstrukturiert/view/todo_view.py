# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.todo_presenter import TodoPresenter

class TodoView(ft.Column):

    def __init__(self):
        super().__init__()
        self.presenter = TodoPresenter()

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
                                ft.IconButton(
                                    icon=ft.Icons.DONE,
                                    tooltip="Erledigt",
                                    # on_click=self.on_done
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.INFO_OUTLINE,
                                    tooltip="Details",
                                ),
                            ],
                        ),
                    )
                )
            )
        # for todo in self.presenter.todos:
        #     self.controls.append(
        #         ft.Card(
        #             bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        #             shadow_color=ft.Colors.ON_SURFACE_VARIANT,
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

