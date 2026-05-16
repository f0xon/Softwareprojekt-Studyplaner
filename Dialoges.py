# pyright: reportUnknownMemberType=false

import flet as ft


class Standard(ft.Column):
    def __init__(self):
        super().__init__(spacing=16, horizontal_alignment=ft.CrossAxisAlignment.START)
        self.controls.extend([
            ft.Text("Dashboard", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Welcome to the dashboard. Add widgets here to display your content."),
            ft.ElevatedButton("new ToDo", on_click=self.on_new_todo),
            ft.ElevatedButton("ToDo01", on_click=self.on_ToDo),
            ft.ElevatedButton("ToDo02", on_click=self.on_ToDo),
            ft.ElevatedButton("ToDo03", on_click=self.on_ToDo),
            ft.ElevatedButton("Refresh", on_click=self.on_refresh),
        ])

    def on_refresh(self, event: ft.Event[ft.Button]):
        event.page.update()

    def on_new_todo(self, event: ft.Event[ft.Button]):
         event.page.update()
    def on_ToDo(self, event: ft.Event[ft.Button]):
         event.page.update()



class todolist(Standard):
    def __init__(self):
        super().__init__()
        ft.SafeArea(
            expand=True,
            content=ft.GridView(
                expand=True,
                runs_count=5,
                max_extent=150,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
                controls=[
                    ft.Image(
                        src=f"https://picsum.photos/150/150?{i}",
                        fit=ft.BoxFit.NONE,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                        border_radius=ft.BorderRadius.all(10),
                    )
                    for i in range(0, 60)
                ],
            ),
        )
        


def main(page: ft.Page):
    page.title = "Todos"
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.MENU),
        title=ft.Text("Dashboard"),
        actions=[
            ft.IconButton(ft.Icons.SEARCH),
            ft.IconButton(ft.Icons.MORE_VERT),
        ],
    )
    page.add(todolist())


ft.app(target=main)
