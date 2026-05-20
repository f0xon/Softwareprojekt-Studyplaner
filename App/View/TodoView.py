# pyright: reportUnknownMemberType=false
import flet as ft
from .StandardView import Standard


class TodoView(Standard):
    
    # list_todos: list[any]= [ft.Checkbox(label="todo1"), #
    #             ft.Checkbox(label="todo2"),
    #             ft.Checkbox(label="todo3")] # type: ignore
    
    def __init__(self):
        super().__init__()
        
    
    def did_mount(self): 
        self.page.title = "Todos"
        # self.controls.append(
        #     ft.BottomAppBar(
        #         bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        #         content=ft.Row(
        #             alignment=ft.MainAxisAlignment.SPACE_AROUND,
        #             controls=[
        #                 ft.IconButton(ft.Icons.MENU),
        #                 ft.IconButton(ft.Icons.SEARCH),
        #                 ft.IconButton(ft.Icons.SETTINGS),
        #             ],
        #         ),
        #     )
        # )
        self.controls.append(
            ft.Column(
            [
                ft.Row([
                    #ft.Button(content= ft.Container(ft.Text("Sortieren"), ft.Icons.KEYBOARD_ARROW_DOWN_ROUNDED)),
                    
                    #warum sprigt es ohne den knopf zu drücken immer in in die ander view?
                    ft.IconButton(icon=ft.Icons.ADD , icon_color=ft.Colors.PRIMARY, on_click=self.on_button_click_addingTodoView()),
                    ]),
                # ft.Row([
                #     ft.Checkbox(label="todo1"), ft.Text("Fällig: 20.05. 18Uhr")
                # ]),
                ft.ListTile(
                    leading=ft.Checkbox(),
                    title="Todo1",
                    subtitle="Categorie",
                    trailing=ft.Text("Do date"),
                    bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                ),
                ft.ListTile(
                    leading=ft.Checkbox(),
                    title="Todo2",
                    subtitle="Categorie",
                    trailing=ft.Text("Do date"),
                    bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                )
            ]
            )
        )

    def on_button_click_addingTodoView(self):
        if isinstance(self.page, ft.Page):
            self.page.go("/addingTodo")