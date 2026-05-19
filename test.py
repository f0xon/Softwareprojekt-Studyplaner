# pyright: reportUnknownMemberType=false


print('Hallo! ztzr')
print("test selina")
print("test selina2")
import flet as ft











def main( page: ft.Page):
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.add()
    page.controls.append(
    #    ft.dropdown(
    #         width = 400,
    #         value="Option 1",
    #         hint_text="Select an option",
    #         options=[
    #             ft.dropdown.Option("Option 1"),
    #             ft.dropdown.Option("Option 2"),
    #         ]
    #     )


        # Option A: Mit Spacer()
        ft.Row([
            ft.Text("Links"),
            ft.Container(expand=True),  # füllt den Platz
            ft.Text("Rechts")
        ])
        
    )

if __name__ == "__main__":
    ft.run(main)




# class adding_todo_UI(Standard):
#     def __init__(self):
#         super().__init__()

#     def did_mount(self):
#          #pop up fesnster
#         self.controls.append(
#             ft.Row([
#                     ft.Text("Titel:"),
#                     ft.IconButton(icon=ft.Icons.ADD , icon_color=ft.Colors.PRIMARY),
#                     ]),
#         )
#         ...
        
        




# class todolist_UI(Standard):
    
#     # list_todos: list[any]= [ft.Checkbox(label="todo1"), #
#     #             ft.Checkbox(label="todo2"),
#     #             ft.Checkbox(label="todo3")] # type: ignore
    
#     def __init__(self):
#         super().__init__()
        
    
#     def did_mount(self): 
#         self.page.title = "Todos"
#         self.controls.append(
#             ft.AppBar(
#                 leading=ft.Icon(ft.Icons.MENU),
#                 title=ft.Text("ToDo-Liste"),
#                 actions=[
#                     ft.IconButton(ft.Icons.SEARCH),
#                     ft.IconButton(ft.Icons.MORE_VERT),
#                 ],
#             ) 
#         )
#         self.controls.append(
#             ft.Column(
#             [
#                 ft.Row([
#                     ft.Button(content= ft.Container(ft.Text("Sortieren"), ft.Icons.KEYBOARD_ARROW_DOWN_ROUNDED)),
#                     ft.IconButton(icon=ft.Icons.ADD , icon_color=ft.Colors.PRIMARY),
#                     ]),
#                 # ft.Row([
#                 #     ft.Checkbox(label="todo1"), ft.Text("Fällig: 20.05. 18Uhr")
#                 # ]),
#                 ft.ListTile(
#                     width=500,
#                     leading=ft.Checkbox(),
#                     title="Todo1",
#                     subtitle="Categorie",
#                     trailing=ft.Text("Do date"),
#                     bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
#                 ),
#                 ft.ListTile(
#                     width=500,
#                     leading=ft.Checkbox(),
#                     title="Todo2",
#                     subtitle="Categorie",
#                     trailing=ft.Text("Do date"),
#                     bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
#                 )
#             ]
#             )
#         )
