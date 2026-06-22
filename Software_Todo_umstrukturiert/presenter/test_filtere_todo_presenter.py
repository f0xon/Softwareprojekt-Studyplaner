import unittest
from unittest.mock import Mock
from model.ToDoListe_model import ToDoListModel, ToDoModel
from repo import TodoRepo
from filtere_todo_presenter import FiltereTodoPresenter

class TestFiltereTodoPresenter(unittest.TestCase):

    def setUp(self):
        self.mock_model = Mock(spec=ToDoListModel)
        self.mock_repo = Mock(spec=TodoRepo)
        self.presenter = FiltereTodoPresenter(self.mock_model, self.mock_repo)

    # --- Initialization Tests ---
    def test_initialization(self):
        self.assertIsInstance(self.presenter.model, Mock)
        self.assertIsInstance(self.presenter.repo, Mock)
        self.assertEqual(self.presenter.kat, "alle")
        self.assertEqual(self.presenter.prio, "alle")
        self.assertEqual(self.presenter.status, "alle")

    # --- Setter Tests ---
    def test_set_kategorie(self):
        self.presenter.set_kategorie("Studium")
        self.assertEqual(self.presenter.kat, "Studium")
        self.presenter.set_kategorie("Haushalt")
        self.assertEqual(self.presenter.kat, "Haushalt")

    def test_set_priority(self):
        self.presenter.set_priority("hoch")
        self.assertEqual(self.presenter.prio, "hoch")
        self.presenter.set_priority("niedrig")
        self.assertEqual(self.presenter.prio, "niedrig")

    def test_set_status(self):
        self.presenter.set_status("offen")
        self.assertEqual(self.presenter.status, "offen")
        self.presenter.set_status("erledigt")
        self.assertEqual(self.presenter.status, "erledigt")

    # --- get_filtered_todos Tests ---
    def test_get_filtered_todos_default(self):
        mock_todo1 = Mock(spec=ToDoModel)
        mock_todo1.id = 1
        mock_todo2 = Mock(spec=ToDoModel)
        mock_todo2.id = 2
        mock_todos = [mock_todo1, mock_todo2]

        self.mock_repo.filtere_todos.return_value = mock_todos

        result = self.presenter.get_filtered_todos()

        self.mock_repo.filtere_todos.assert_called_once_with("alle", "alle", "alle")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[1].id, 2)

    def test_get_filtered_todos_with_custom_filters(self):
        self.presenter.set_kategorie("Studium")
        self.presenter.set_priority("hoch")
        self.presenter.set_status("offen")

        mock_todo = Mock(spec=ToDoModel)
        mock_todo.id = 1
        self.mock_repo.filtere_todos.return_value = [mock_todo]

        result = self.presenter.get_filtered_todos()

        self.mock_repo.filtere_todos.assert_called_once_with("Studium", "hoch", "offen")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)