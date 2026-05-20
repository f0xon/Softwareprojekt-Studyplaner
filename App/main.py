# pyright: reportUnknownMemberType=false
import flet as ft   
from App.View.Navigator import Navigator

def main(page: ft.Page): 
    Navigator(page)

ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)