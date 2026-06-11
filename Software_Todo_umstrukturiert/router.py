# pyright: ignore[reportArgumentType]
from typing import Callable,Any
import flet as ft

from pymongo import MongoClient
from pymongo.database import Database

from model.todo_model import ToDoModel, Priority, hoch, mittel, niedrig, keine_p, Category, studium, haushalt, freizeit
from model.ToDoListe_model import ToDoListModel
from view.todo_view import TodoView
from view.filtere_todo_view import FiltereTodoView
from view.navigationBar_view import NavigationBarView
from view.erzeuge_todo_view import ErzeugeTodoView
from presenter.todo_presenter import TodoListePresenter
from presenter.erzeuge_todo_presenter import TodoDetailPresenter
from presenter.filtere_todo_presenter import FiltereTodoPresenter
from repo import InMemoryTodoRepo,MongoTodoRepo

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.todolist_model=ToDoListModel()
        self.todo_model = ToDoModel()
        self.todo:str="/Todo"
        self.erzeuge_todo:str="/erzeugeTodo"
        self.filtere_todo:str="/filtereTodo"
        self.page.navigation_bar = NavigationBarView(self).build()

        page.on_route_change = self.on_route_change

        # TODO Repo erzeugen und an Presenter übergeben
        db: Database[Any] = MongoClient(DB_URL, username=DB_USER, password=DB_PASSWORD).get_database(DB_NAME)
        self.repo_mongo = MongoTodoRepo(db)
        self.repo_memory=InMemoryTodoRepo
        #wähle hier dein gewünschtes repo aus
        self.ausgewaehltes_repo=self.repo_memory
        
        # Presenter hier erzeugen 
        self.presenter_todo=TodoListePresenter(self.todolist_model,self.ausgewaehltes_repo)
        self.presenter_detail=TodoDetailPresenter(self.todolist_model,self.ausgewaehltes_repo)
        self.presenter_filtern=FiltereTodoPresenter(self.todolist_model,self.ausgewaehltes_repo)

        #self.routes:dict[str,Callable[[], ft.Column]]={ #richtiges Typing?
         #   self.todo: lambda: TodoView(), 
         #   self.erzeuge_todo: lambda:ErzeugeTodoView(on_save=self.go_to_todos),
         #   self.filtere_todo:lambda:FiltereTodoView(on_save=self.go_to_todos),
        #}

        self.navigation:dict[int, str]={
            0:self.erzeuge_todo,
            1:self.todo,
            2:self.filtere_todo
        }

        self.page.on_route_change = self.on_route_change

        self.page.navigation_bar = NavigationBarView(self).build()

        '''self.routes:dict[str,Callable[[], ft.Column]]={ #richtiges Typing?
            self.todo: TodoView, 
            self.erzeuge_todo: ErzeugeTodoView,
            self.filtere_todo:FiltereTodoView,
        }
        '''
    def on_route_change(self, e: ft.RouteChangeEvent):

        self.page.clean()

        if self.page.route == self.todo:
            self.page.add(TodoView(self.presenter_todo,self.presenter_filtern))

        elif self.page.route == self.erzeuge_todo:
            self.page.add(ErzeugeTodoView(self.presenter_detail))

        elif self.page.route == self.filtere_todo:
            self.page.add(FiltereTodoView(self.presenter_filtern))

        else:
            self.page.go(self.todo)

        self.page.update()

        '''      
        self.page.clean()
        erzeuge_view = self.routes.get(self.page.route)
        if erzeuge_view:
            self.page.add(erzeuge_view())
        self.page.update()
'''
        

    def on_nav_change(self, e:ft.ControlEvent):
        index:int = e.control.selected_index
        route=self.navigation.get(index)
        if route:
            if isinstance(self.page, ft.Page): # pyright: ignore[reportUnnecessaryIsInstance]
                self.page.go(route)


    def go_to_todos(self):
        self.page.go (self.todo) #mit Index machen?

