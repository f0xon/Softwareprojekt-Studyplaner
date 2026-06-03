# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.todos_presenter import TodosPresenter

class TodosView(ft.Column):

    def __init__(self,router):
        super().__init__()

        self.router=router
        self.presenter = TodosPresenter(self, router)

        self.todo_list = ft.Column()
        self.controls.extend([
            ft.Row([
                ft.Text("ToDos", style=ft.TextStyle(weight=ft.FontWeight.BOLD, decoration=ft.TextDecoration.UNDERLINE)),
                #ft.IconButton(icon=ft.Icons.ADD , icon_color=ft.Colors.PRIMARY, on_click=self.on_button_clicked_add),#beim klicken des plus-Button wird page.go("/erzeugeTodo") und springt in ErzeugeTodoView()
                ft.IconButton(icon=ft.Icons.FILTER_ALT , icon_color=ft.Colors.PRIMARY, on_click=self.on_button_clicked_filter),
            ]),
            self.todo_list
        ])

        # Design von Ferdinand(funktioniert noch nicht)
        # self.controls.append(ft.Column([
        #     ft.Row([
        #         ft.Button("+", on_click=self.on_button_clicked), #beim klicken des plus-Button auf todosView wird page.go("/erzeugeTodo") und springt in ErzeugeTodoView()
        #     ]),
        #     for todo in todos: #noch nicht fertig. Wie Liste Models ausgeben? Es gehen keine Forschleifen in Listen wie lösen?
        #         ft.ListTile(
        #             leading=ft.Checkbox(),
        #             title="",#titel
        #             subtitle="",#categorie
        #             trailing=ft.Text(""),#datum
        #             bgcolor=ft.Colors.SURFACE_CONTAINER_LOW
        #         )
        # ]))


    def on_button_clicked_add(self):
        self.presenter.erzeuge_todo()
    
    def on_button_clicked_filter(self):
        self.presenter.filtere_todo()
    

    def did_mount(self):
        self.presenter.load_todos()

    def show_todos(self, todos:list[str]):
        self.todo_list.controls.clear()

        for todo in todos:
            self.todo_list.controls.append(ft.Text(todo))

        self.update()

