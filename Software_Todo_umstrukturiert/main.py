# pyright: reportUnknownMemberType=false
import os
import flet as ft
from router import Router

os.chdir(os.path.dirname(__file__))

def main(page: ft.Page):
    page.title= "ToDo-App"
    Router(page)
    page.scroll = ft.ScrollMode.AUTO
    page.go("/Todo")

ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)

#Betz: In den Vorlesungsunterlagen sind in der UML wenn man dataclasses abbildet manchmal datenklassen mit <<dataclass>> und manchmal ohne dargestellt was soll man benutzen?