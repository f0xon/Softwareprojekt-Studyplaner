# pyright: reportAttributeAccessIssue=false

from flet.controls.core.column import Column
import flet as ft
from presenter.login_presenter import LoginPresenter
from presenter.filtere_todo_presenter import FiltereTodoPresenter


class LoginView(ft.Column):
    def __init__(self, presenter: LoginPresenter):
        super().__init__()
        self.presenter = presenter

        self.username_field = ft.TextField(label="Benutzername")
        self.status_text = ft.Text()
        self.controls = [
            ft.Text("LOGIN - Benutzername eingeben"),
            ft.Divider(),
            self.username_field,
            ft.Button(
                "Login",
                on_click=self.on_button_clicked_save_login
            ),
            self.status_text
        ]

    def on_button_clicked_save_login(self):
        username = self.username_field.value
        success = self.presenter.login(username)
        if success:
            self.status_text.value = "Login erfolgreich"
        else:
            self.status_text.value = "Login fehlgeschlagen"
        self.update()
        if isinstance(self.page, ft.Page):
            self.page.go("/Todos")