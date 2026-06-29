import unittest
from unittest.mock import Mock
from datetime import date
from repo.todo_repo import TodoRepo
from model.todo_model import ToDo, HOCH, STUDIUM

class TestTodoRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.repo = Mock(spec=TodoRepo)

    def test_speichere(self):
        todo = ToDo(
            _todo_id=1,
            titel="Test Todo",
            notiz="Test Description",
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=None,
        )

        self.repo.speichere(todo)
        self.repo.speichere.assert_called_once_with(todo)

    def test_finde_todo_mit_id(self):
        todo_id = 1
        expected_todo = ToDo(
            _todo_id=todo_id,
            titel="Test Todo",
            notiz="Test Description",
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=None,
        )
        self.repo.finde_todo_mit_id.return_value = expected_todo

        result = self.repo.finde_todo_mit_id(todo_id)

        self.assertEqual(result, expected_todo)
        self.repo.finde_todo_mit_id.assert_called_once_with(todo_id)

    def test_update_todo(self):
        updated_todo = ToDo(
            _todo_id=1,
            titel="Updated Todo",
            notiz="Updated Description",
            priority=HOCH,
            deadline=date(2026, 6, 20),
            calendar=True,
            category=STUDIUM,
            extra=None,
        )

        self.repo.update_todo(updated_todo)
        self.repo.update_todo.assert_called_once_with(updated_todo)

    def test_lade_alle(self):
        self.repo.lade_alle()
        self.repo.lade_alle.assert_called_once()

    def test_erledige_todo(self):
        todo_id = 1
        self.repo.erledige_todo(todo_id)
        self.repo.erledige_todo.assert_called_once_with(todo_id)

    def test_filtere_todos(self):
        self.repo.filtere_todos("Studium", "hoch", "offen")
        self.repo.filtere_todos.assert_called_once_with("Studium", "hoch", "offen")

    def test_naechste_id(self):
        self.repo.naechste_id()
        self.repo.naechste_id.assert_called_once()

    def test_loesche_todo(self):
        todo = ToDo(
            _todo_id=1,
            titel="Todo to delete",
            notiz="This will be deleted",
            priority=HOCH,
            deadline=date(2026, 6, 30),
            calendar=False,
            category=STUDIUM,
            extra=None,
        )

        self.repo.loesche_todo(todo)
        self.repo.loesche_todo.assert_called_once_with(todo)

if __name__ == '__main__':
    unittest.main()