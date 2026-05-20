# pyright: reportUnknownMemberType=false
import flet as ft
import os

try:
    from .View.Navigator import Navigator
except ImportError:
    from View.Navigator import Navigator

os.chdir(os.path.dirname(__file__))

def main(page: ft.Page): 
    
    Navigator(page)
if __name__ == "__main__":
    ft.run(main)#, view=ft.AppView.WEB_BROWSER, port=8080)