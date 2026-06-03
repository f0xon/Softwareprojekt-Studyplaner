# pyright: reportUnknownMemberType=false
import flet as ft
from router import Router

os.chdir(os.path.dirname(__file__))

def main(page: ft.Page):
    Router(page)
    page.go("/Todo")
    #page.go("/Startseite")


ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)