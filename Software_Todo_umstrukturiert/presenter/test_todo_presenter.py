import unittest
from unittest.mock import Mock
from model.ToDoListe_model import ToDoListModel, ToDoModel
from repo import TodoRepo
from todo_presenter import TodoListePresenter

class TestTodoListePresenter(unittest.TestCase):

    def setUp(self):
        self.mock_model = Mock(spec=ToDoListModel)
        self.mock_repo = Mock(spec=TodoRepo)
        self.presenter = TodoListePresenter(self.mock_model, self.mock_repo)

    # --- Initialization Tests ---
    def test_initialization(self):
        self.assertIsInstance(self.presenter.model, Mock)
        self.assertIsInstance(self.presenter.repo, Mock)

    # --- get_todos Tests ---
    def test_get_todos(self):
        mock_todo1 = Mock(spec=ToDoModel)
        mock_todo1.id = 1
        mock_todo2 = Mock(spec=ToDoModel)
        mock_todo2.id = 2
        mock_todos = [mock_todo1, mock_todo2]

        self.mock_repo.lade_alle.return_value = mock_todos

        result = self.presenter.get_todos()

        self.mock_repo.lade_alle.assert_called_once()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[1].id, 2)

    # --- erledige_todo Tests ---
    def test_erledige_todo_success(self):
        mock_todo1 = Mock(spec=ToDoModel)
        mock_todo1.id = 1
        mock_todo2 = Mock(spec=ToDoModel)
        mock_todo2.id = 2
        mock_todos = [mock_todo1, mock_todo2]

        self.mock_repo.lade_alle.return_value = mock_todos

        self.presenter.erledige_todo(1)

        mock_todo1.erledige_todo.assert_called_once()
        mock_todo2.erledige_todo.assert_not_called()

    def test_erledige_todo_not_found(self):
        mock_todo = Mock(spec=ToDoModel)
        mock_todo.id = 1
        self.mock_repo.lade_alle.return_value = [mock_todo]

        self.presenter.erledige_todo(999)
        mock_todo.erledige_todo.assert_not_called()

    # --- loesche_todo Tests ---
    def test_loesche_todo_success(self):
        mock_todo1 = Mock(spec=ToDoModel)
        mock_todo1.id = 1
        mock_todo2 = Mock(spec=ToDoModel)
        mock_todo2.id = 2
        mock_todos = [mock_todo1, mock_todo2]

        self.mock_repo.lade_alle.return_value = mock_todos

        self.presenter.loesche_todo(1)

        self.mock_repo.loesche_todo.assert_called_once_with(1)

    def test_loesche_todo_not_found(self):
        mock_todo = Mock(spec=ToDoModel)
        mock_todo.id = 1
        self.mock_repo.lade_alle.return_value = [mock_todo]

        self.presenter.loesche_todo(999)
        self.mock_repo.loesche_todo.assert_not_called()

    # --- lade_todo Tests ---
    def test_lade_todo_success(self):
        mock_todo1 = Mock(spec=ToDoModel)
        mock_todo1.id = 1
        mock_todo2 = Mock(spec=ToDoModel)
        mock_todo2.id = 2
        mock_todos = [mock_todo1, mock_todo2]

        self.mock_repo.lade_alle.return_value = mock_todos

        result = self.presenter.lade_todo(1)

        self.assertEqual(result, mock_todo1)
        self.mock_repo.lade_alle.assert_called_once()

    def test_lade_todo_not_found(self):
        mock_todo = Mock(spec=ToDoModel)
        mock_todo.id = 1
        self.mock_repo.lade_alle.return_value = [mock_todo]

        result = self.presenter.lade_todo(999)

        self.assertIsNone(result)
        self.mock_repo.lade_alle.assert_called_once()