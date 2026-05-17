import flet as ft
from views.home_view import HomeView
from views.todo_view import TodoView
from views.settings_view import SettingsView


def main(page: ft.Page):
    page.title = "Studyplaner — UI Mockup"
    page.window_width = 900
    page.window_height = 600

    # instantiate views
    home = HomeView(page)
    todos = TodoView(page)
    settings = SettingsView(page)

    # content area that will be replaced when switching views
    content = ft.Column([home.build()], spacing=10, expand=True)

    def show_view(view):
        content.controls[:] = [view.build()]
        page.update()

    controls = ft.Row(
        [
            ft.ElevatedButton("Home", on_click=lambda e: show_view(home)),
            ft.ElevatedButton("Todos", on_click=lambda e: show_view(todos)),
            ft.ElevatedButton("Settings", on_click=lambda e: show_view(settings)),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=12,
    )

    page.add(ft.Column([controls, ft.Divider(), content], expand=True))


if __name__ == "__main__":
    ft.app(target=main)
