# pyright: reportUnknownMemberType=false

from dataclasses import dataclass

import flet as ft


@dataclass
class Date():
    ...


# @dataclass
# class Todo():
#     ...

class Standard(ft.Column):
    def __init__(self):
        super().__init__(spacing=16, horizontal_alignment=ft.CrossAxisAlignment.START)
        self.controls =[]

    

    # def on_refresh(self, event: ft.Event[ft.Button]):
    #     event.page.update()


class adding_todo_UI(Standard):
    Titel: str = ""
    Fälligkeit: Date= 
    Kalender: str = ""
    Erinnerung: str = ""
    Bemerkung: str = ""
    Kategorie: str = ""



    def __init__(self):
        super().__init__()

    def did_mount(self):
         #pop up fesnster
        self.controls.append(
            ft.Column([
                ft.Row([
                        ft.Text("Titel:"),
                        ft.TextField(
                            label="",
                            value=self.Titel,
                        ),
                        ]),
                ft.Row([
                        ft.Text("Fälligkeit:"),
                        ft.TextField(
                            label="",
                            value=self.Fälligkeit,
                        ),
                        ]),

                ft.Row([
                    ft.Text("Kalender")
                    #ja nein check boxen
                ])

                ft.Row([
                        ft.Text("Erinnerung:"),
                        ft.TextField(
                            label="",
                            value=self.Erinnerung,
                        ),
                        ]),
                ft.Row([
                        ft.Text("Bemerkung:"),
                        ft.TextField(
                            label="",
                            value=self.Bemerkung,
                        ),
                        ]),
                ft.Row([
                        ft.Text("Kategorie:"),
                        ft.TextField(
                            label="",
                            value=self.Kategorie,
                        ),
                        ]),
            ])
        )
        ...
        
        




class todolist_UI(Standard):
    
    # list_todos: list[any]= [ft.Checkbox(label="todo1"), #
    #             ft.Checkbox(label="todo2"),
    #             ft.Checkbox(label="todo3")] # type: ignore
    
    def __init__(self):
        super().__init__()
        
    
    def did_mount(self): 
        self.page.title = "Todos"
        self.controls.append(
            ft.AppBar(
                leading=ft.Icon(ft.Icons.MENU),
                title=ft.Text("ToDo-Liste"),
                actions=[
                    ft.IconButton(ft.Icons.SEARCH),
                    ft.IconButton(ft.Icons.MORE_VERT),
                ],
            ) 
        )
        self.controls.append(
            ft.Column(
            [
                ft.Row([
                    #ft.Button(content= ft.Container(ft.Text("Sortieren"), ft.Icons.KEYBOARD_ARROW_DOWN_ROUNDED)),
                    ft.IconButton(icon=ft.Icons.ADD , icon_color=ft.Colors.PRIMARY),
                    ]),
                # ft.Row([
                #     ft.Checkbox(label="todo1"), ft.Text("Fällig: 20.05. 18Uhr")
                # ]),
                ft.ListTile(
                    width=500,
                    leading=ft.Checkbox(),
                    title="Todo1",
                    subtitle="Categorie",
                    trailing=ft.Text("Do date"),
                    bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                ),
                ft.ListTile(
                    width=500,
                    leading=ft.Checkbox(),
                    title="Todo2",
                    subtitle="Categorie",
                    trailing=ft.Text("Do date"),
                    bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                )
            ]
            )
        )



def main(page: ft.Page):
    page.add(todolist_UI())


ft.app(target=main)