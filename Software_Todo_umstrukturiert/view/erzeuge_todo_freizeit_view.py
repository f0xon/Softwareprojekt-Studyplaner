from flet import ft
from erzeuge_todo_view import ErzeugeTodoView

class ErzeugeTodoFreizeitView(ErzeugeTodoView):
    def __init__ (self,router):
        super().__init__()

        self.ort = ft.TextField(label="Ort")
        self.hobby = ft.Column(
        controls=[
            ft.Dropdown(options=[ft.DropdownOption(option) for option in options]),
            ft.Row(
                controls=[
                    ft.TextField(
                        hint_text="Enter item name",
                        value=self.new_option,
                        on_change=lambda e: self.set_new_option(e.control.value),
                    ),
                    ft.Button("Add option", on_click=self.add_clicked),
                ]
            )
            ]
        )
    

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
                                    ft.Text("Ort:"),
                                    ft.Container(expand=True),
                                    self.ort,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Hobby:"),
                                    ft.Container(expand=True),
                                    self.hobby,
                                ]
                            ),
                        ]
                    )
                )
            )
        )

    def add_clicked(e):
        set_options(lambda cur: cur + [new_option])
        self.set_new_option("")



    