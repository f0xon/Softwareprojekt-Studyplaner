import unittest
from unittest.mock import Mock
from model.todo_model import ToDo
from repo.todo_repo import TodoRepo
from todo_presenter import TodoListePresenter

class TestTodoListePresenter(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock(spec=TodoRepo)
        self.presenter = TodoListePresenter(self.mock_repo)

    def test_initialization(self):
        self.assertIsInstance(self.presenter._repo, Mock)

    def test_get_todos(self):
        mock_todo1 = Mock(spec=ToDo)
        mock_todo1.id = 1
        mock_todo2 = Mock(spec=ToDo)
        mock_todo2.id = 2
        mock_todos = [mock_todo1, mock_todo2]

        self.mock_repo.lade_alle.return_value = mock_todos

        result = self.presenter.get_todos()

        self.mock_repo.lade_alle.assert_called_once()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[1].id, 2)

    def test_erledige_todo_success(self):
        mock_todo1 = Mock(spec=ToDo)
        mock_todo1.id = 1
        mock_todo2 = Mock(spec=ToDo)
        mock_todo2.id = 2
        
        self.mock_repo.finde_todo_mit_id.return_value = mock_todo1

        self.presenter.erledige_todo(1)

        mock_todo1.toggle_erledigt_todo.assert_called_once()
        self.mock_repo.update_todo.assert_called_once_with(mock_todo1)

    def test_erledige_todo_not_found(self):
        self.mock_repo.finde_todo_mit_id.return_value = None

        self.presenter.erledige_todo(999)
        self.mock_repo.update_todo.assert_not_called()

    def test_loesche_todo_success(self):
        mock_todo1 = Mock(spec=ToDo)
        mock_todo1.id = 1
        
        self.mock_repo.finde_todo_mit_id.return_value = mock_todo1

        self.presenter.loesche_todo(1)

        self.mock_repo.loesche_todo.assert_called_once_with(mock_todo1)

    def test_loesche_todo_not_found(self):
        self.mock_repo.finde_todo_mit_id.return_value = None

        self.presenter.loesche_todo(999)
        self.mock_repo.loesche_todo.assert_not_called()

    def test_lade_todo_success(self):
        mock_todo1 = Mock(spec=ToDo)
        mock_todo1.id = 1
        mock_todo2 = Mock(spec=ToDo)
        mock_todo2.id = 2
        mock_todos = [mock_todo1, mock_todo2]

        self.mock_repo.lade_alle.return_value = mock_todos

        result = self.presenter.lade_todo(1)

        self.assertEqual(result, mock_todo1)
        self.mock_repo.lade_alle.assert_called_once()

    def test_lade_todo_not_found(self):
        mock_todo = Mock(spec=ToDo)
        mock_todo.id = 1
        self.mock_repo.lade_alle.return_value = [mock_todo]

        result = self.presenter.lade_todo(999)

        self.assertIsNone(result)
        self.mock_repo.lade_alle.assert_called_once()