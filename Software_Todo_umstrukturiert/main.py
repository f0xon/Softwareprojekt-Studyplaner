# pyright: reportUnknownMemberType=false
import flet as ft
from router import Router

def main(page: ft.Page):
    Router(page)
    page.go("/meinStudium")
    #page.go("/Startseite")


ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)