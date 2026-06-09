# pyright: reportUnknownMemberType=false
import os
import flet as ft
from router import Router
from pymongo import MongoClient
from pymongo.database import Database
from typing import Any
from repo import MongoPersonTodoRepo,InMemoryTodoRepo
os.chdir(os.path.dirname(__file__))

#Nutze DB optionen: 'MongoPersonTodoRepo', 'InMemoryTodoRepo'
Welche_DB: str = 'InMemoryTodoRepo'

if(Welche_DB== 'InMemoryTodoRepo'):
    InMemoryTodoRepo()
elif(Welche_DB=='MongoPersonTodoRepo'):
    #Logindaten Für die MongoDB Datenbank:
    DB_URL = "mongodb+srv://cluster0.9w2gjme.mongodb.net"
    DB_USER = "soen_labor"
    DB_PASSWORD = "6HQgiBWd7IDAXa6g"
    DB_NAME = "soen_vorlesung"

    db: Database[Any] = MongoClient(DB_URL, username=DB_USER, password=DB_PASSWORD).get_database(DB_NAME)
    MongoPersonTodoRepo(db)




def main(page: ft.Page):
    page.title= "ToDo-App"
    Router(page)
    page.scroll = ft.ScrollMode.AUTO
    page.go("/Todo")

ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)