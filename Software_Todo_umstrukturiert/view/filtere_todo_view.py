# pyright: reportAttributeAccessIssue=false

import flet as ft
from presenter.filtere_todo_presenter import FiltereTodoPresenter
from view.todo_view import TodoView
#Filterfunktion funktioniert im Debug aber die TodoSeite wird noch nicht aktualisiert nach dem Speichern
class FiltereTodoView(ft.Column):
    def __init__(self,presenter:FiltereTodoPresenter):
        super().__init__()
        # self.on_save=on_save
        self.presenter = presenter

        # RadioGroups
        self.status = ft.RadioGroup(
            value="alle",
            content=ft.Row(
                controls=[
                    ft.Radio(value="alle", label="Alle"),
                    ft.Radio(value="offen", label="Offen"),
                    ft.Radio(value="erledigt", label="Erledigt"),
                ]
            ),
            on_change=self.status_changed
        )

        self.category = ft.RadioGroup(
            value="alle",
            content=ft.Row(
                controls=[
                    ft.Radio(value="alle", label="Alle"),
                    ft.Radio(value="keine", label="Keine"),
                    ft.Radio(value="Studium", label="Studium"),
                    ft.Radio(value="Haushalt", label="Haushalt"),
                    ft.Radio(value="Freizeit", label="Freizeit"),
                ]
            ),
            on_change=self.category_changed
        )

        self.priority = ft.RadioGroup(
            value="alle",
            content=ft.Row(
                controls=[
                    ft.Radio(value="alle", label="Alle"),
                    ft.Radio(value="keine", label="Keine"),
                    ft.Radio(value="niedrig", label="Niedrig"),
                    ft.Radio(value="mittel", label="Mittel"),
                    ft.Radio(value="hoch", label="Hoch"),
                ]
            ),
            on_change=self.priority_changed
        )

        # Container für ein-/ausblendbare Bereiche
        self.status_container = ft.Column(
            visible=False,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Status"),
                        self.status,
                    ]
                )
            ]
        )

        self.category_container = ft.Column(
            visible=False,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Kategorie"),
                        self.category,
                    ]
                )
            ]
        )

        self.priority_container = ft.Column(
            visible=False,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Priorität"),
                        self.priority,
                    ]
                )
            ]
        )

        # UI aufbauen
        self.controls = [
            ft.Column(
                controls=[
                    ft.Text("Filterfunktion"),
                    ft.Divider(),

                    # Status
                    ft.Row(
                        controls=[
                            ft.Text("Status filtern:"),
                            ft.Switch(
                                value=False,
                                active_color=ft.Colors.BLUE,
                                on_change=self.on_switch_changed_status,
                            ),
                            self.status_container,
                        ]
                    ),

                    # Kategorie
                    ft.Row(
                        controls=[
                            ft.Text("Kategorie filtern:"),
                            ft.Switch(
                                value=False,
                                active_color=ft.Colors.BLUE,
                                on_change=self.on_switch_changed_category,
                            ),
                            self.category_container,
                        ]
                    ),

                    # Priorität
                    ft.Row(
                        controls=[
                            ft.Text("Priorität filtern:"),
                            ft.Switch(
                                value=False,
                                active_color=ft.Colors.BLUE,
                                on_change=self.on_switch_changed_priority,
                            ),
                            self.priority_container,
                        ]
                    ),
                    ft.Button("Speichern",on_click=self.on_button_clicked_speichern)
                ]
            )
        ]

    #verstößt gegen DRY
    def on_switch_changed_status(self, e):
        self.status_container.visible = e.control.value
        self.status.value="alle"
        self.update()

    def on_switch_changed_category(self, e):
        self.category_container.visible = e.control.value
        self.category.value="alle"
        self.update()

    def on_switch_changed_priority(self, e):
        self.priority_container.visible = e.control.value
        self.priority.value="alle"
        self.update()

    def category_changed(self, e):
        self.presenter.set_kategorie(self.category.value)

    def priority_changed(self, e):
        self.presenter.set_priority(self.priority.value)

    def status_changed(self, e):
        self.presenter.set_status(self.status.value)
    
    def on_button_clicked_speichern(self,e):
        self.presenter.get_filtered_todos()
        #beim wieder auf view sprinegn soll rsult wieder dummydaten.cpoy sein