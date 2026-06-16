# pyright: reportAttributeAccessIssue=false

import flet as ft
from presenter.filtere_todo_presenter import FiltereTodoPresenter

class FiltereTodoView(ft.Column):
    def __init__(self,presenter:FiltereTodoPresenter):
        super().__init__()
        # self.on_save=on_save
        self.presenter = presenter

        # RadioGroups
        self.status = ft.RadioGroup(
            value=presenter.status,
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
            value=presenter.kat,
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
            value=presenter.prio,
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
            visible=self.presenter.status != "alle",
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
            visible=self.presenter.kat != "alle",
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
            visible=self.presenter.prio != "alle",
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
                                value=self.presenter.status != "alle",
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
                                value=self.presenter.kat != "alle",
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
                                value=self.presenter.prio != "alle",
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
    def on_switch_changed_status(self, e: ft.Event[ft.Switch]):
        print("Switch Status changed:", e.control.value, type(e))
        self.status_container.visible = e.control.value
        self.status.value=self.presenter.status
        self.update()

    def on_switch_changed_category(self, e: ft.Event[ft.Switch]):
        self.category_container.visible = e.control.value
        self.category.value=self.presenter.kat
        self.update()

    def on_switch_changed_priority(self, e: ft.Event[ft.Switch]):
        self.priority_container.visible = e.control.value
        self.priority.value=self.presenter.prio
        self.update()

    def category_changed(self, e: ft.Event[ft.RadioGroup]):
        self.presenter.set_kategorie(self.category.value)

    def priority_changed(self, e: ft.Event[ft.RadioGroup]):
        self.presenter.set_priority(self.priority.value)

    def status_changed(self, e: ft.Event[ft.RadioGroup]):
        self.presenter.set_status(self.status.value)
    
    def on_button_clicked_speichern(self,e: ft.Event[ft.Button]):
        self.presenter.get_filtered_todos()
        if isinstance(self.page, ft.Page): # für den TypeChecker, eigentlich immer der Fall
            self.page.go("/Todos")
        #beim wieder auf view sprinegn soll rsult wieder dummydaten.cpoy sein