# pyright: reportAttributeAccessIssue=false
import flet as ft
from presenter.filtere_todo_presenter import FiltereTodoPresenter

class FiltereTodoView(ft.Column):
    def __init__(self):
        super().__init__()
        self.presenter=FiltereTodoPresenter
        self.status_value = "alle"
        self.filter_active = False

        self.status = ft.Column( #nur sichtbar wenn Switch ON
            visible=False,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Status"),
                        ft.RadioGroup(
                            value=self.status_value,
                            #on_change=self.status_changed, noch zu implementieren
                            content=ft.Row(
                                controls=[
                                    ft.Radio(value="alle", label="Alle"),
                                    ft.Radio(value="offen", label="Offen"),
                                    ft.Radio(value="erledigt", label="Erledigt"),
                                ]
                            )
                        )
                    ]
                )
            ]
        )

        self.category = ft.Column( #nur sichtbar wenn Switch ON
            visible=False,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Kategorie"),
                        ft.RadioGroup(
                            content=ft.Row([
                                ft.Radio(value="keine", label="Keine"),
                                ft.Radio(value="Studium", label="Studium"),
                                ft.Radio(value="Haushalt", label="Haushalt"),
                                ft.Radio(value="Freizeit", label="Freizeit"),
                            ]),
                            #on_change=self.category_changed 
                        )
                    ]
                )
            ]
        )

        self.priority = ft.Column( #nur sichtbar wenn Switch ON
            visible=False,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Priorität"),
                        ft.RadioGroup(
                            value="keine",
                            content=ft.Row([
                                ft.Radio(value="keine", label="Keine"),
                                ft.Radio(value="niedrig", label="niedrig"),
                                ft.Radio(value="mittel", label="mittel"),
                                ft.Radio(value="hoch", label="hoch"),
                            ]),
                            #on_change=self.category_changed noch zu implementieren
                        )
                    ]
                )
            ]
        )

        #Buil UI
        self.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Filterfunktion"),
                    ft.Text(""),
                    ft.Row(
                        controls=[
                            ft.Text("Status filtern:"),
                            ft.Switch(
                                value=False,
                                active_color=ft.Colors.BLUE,
                                on_change=self.on_switch_changed_status
                            ),
                            self.status 
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Kategorie filtern:"),
                            ft.Switch(
                                value=False,
                                active_color=ft.Colors.BLUE,
                                on_change=self.on_switch_changed_category
                            ),
                            self.category
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Priorität filtern:"),
                            ft.Switch(
                                value=False,
                                active_color=ft.Colors.BLUE,
                                on_change=self.on_switch_changed_priority
                            ),
                            self.priority
                        ]
                    )
                ]
            )
        )

#verstößt gegen DRY
    def on_switch_changed_status(self, e):
        self.status.visible = e.control.value
        self.update()

    def on_switch_changed_category(self, e):
        self.category.visible = e.control.value
        self.update()
    
    def on_switch_changed_priority(self, e):
        self.priority.visible = e.control.value
        self.update()
#
    # def category_changed(self,e):
    #     self.category.value=e.control.value
    #     self.presenter.filtere_kategorie(self.category.value)