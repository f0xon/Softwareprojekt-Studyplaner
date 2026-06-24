import unittest
from unittest.mock import Mock
from datetime import date
from model.ToDoListe_model import ToDoListModel, ToDoModel
from model.ToDoListe_model import prioritäten_dict, kategorien_dict
from model.ToDoListe_model import Studium, Haushalt, Freizeit
from repo import todo_memory_repo, todo_mongo_repo, todo_repo
from erzeuge_todo_presenter import TodoDetailPresenter

class TestTodoDetailPresenter(unittest.TestCase):

    def setUp(self):
        self.mock_model = Mock(spec=ToDoListModel)
        self.mock_repo = Mock(spec=TodoRepo)
        self.presenter = TodoDetailPresenter(self.mock_model, self.mock_repo)

    def test_initialization(self):
        self.assertIsInstance(self.presenter.model, Mock)
        self.assertIsInstance(self.presenter.repo, Mock)
        self.assertIsNone(self.presenter._current_todo)

    def test_is_create_mode_with_modus_set(self):
        self.presenter._modus = "create"
        self.assertTrue(self.presenter.is_create_mode)
        self.presenter._modus = "edit"
        self.assertFalse(self.presenter.is_create_mode)

    def test_is_edit_mode_with_modus_set(self):
        self.presenter._modus = "edit"
        self.assertTrue(self.presenter.is_edit_mode)
        self.presenter._modus = "create"
        self.assertFalse(self.presenter.is_edit_mode)

    def test_map_priority(self):
        self.assertEqual(self.presenter.map_priority("keine"), prioritäten_dict["keine"])
        self.assertEqual(self.presenter.map_priority("niedrig"), prioritäten_dict["niedrig"])
        self.assertEqual(self.presenter.map_priority("mittel"), prioritäten_dict["mittel"])
        self.assertEqual(self.presenter.map_priority("hoch"), prioritäten_dict["hoch"])
        self.assertIsNone(self.presenter.map_priority("invalid"))

    def test_map_category(self):
        self.assertEqual(self.presenter.map_category("keine"), kategorien_dict["keine"])
        self.assertEqual(self.presenter.map_category("Studium"), kategorien_dict["Studium"])
        self.assertEqual(self.presenter.map_category("Haushalt"), kategorien_dict["Haushalt"])
        self.assertEqual(self.presenter.map_category("Freizeit"), kategorien_dict["Freizeit"])
        self.assertIsNone(self.presenter.map_category("invalid"))

    def test_build_extra_studium(self):
        data = {"modul": "Mathe", "gruppenarbeit": True}
        extra = self.presenter.build_extra("Studium", data)
        self.assertIsInstance(extra, Studium)
        self.assertEqual(extra.modul, "Mathe")
        self.assertTrue(extra.gruppenarbeit)

    def test_build_extra_haushalt(self):
        data = {"wiederkehrend": False}
        extra = self.presenter.build_extra("Haushalt", data)
        self.assertIsInstance(extra, Haushalt)
        self.assertFalse(extra.wiederkehrend)

    def test_build_extra_freizeit(self):
        data = {"hobby": "Lesen", "ort": "Zuhause"}
        extra = self.presenter.build_extra("Freizeit", data)
        self.assertIsInstance(extra, Freizeit)
        self.assertEqual(extra.hobby, "Lesen")
        self.assertEqual(extra.ort, "Zuhause")

    def test_build_extra_empty_data(self):
        extra = self.presenter.build_extra("Studium", {})
        self.assertEqual(extra, {})

    def test_build_extra_invalid_category(self):
        with self.assertRaises(TypeError):
            self.presenter.build_extra("Invalid", {"key": "value"})

    def test_lade_todo_success(self):
        mock_todo = Mock(spec=ToDoModel)
        mock_todo.titel = "Test Todo"
        mock_todo.notiz = "Test Notiz"
        mock_todo.deadline = date(2026, 6, 25)
        mock_todo.calendar = False
        mock_todo.priority.name = "hoch"
        mock_todo.category.name = "Studium"

        self.mock_repo.finde_todo_mit_id.return_value = mock_todo

        result = self.presenter.lade_todo(1)

        self.mock_repo.finde_todo_mit_id.assert_called_once_with(1)
        self.assertEqual(self.presenter._current_todo, mock_todo)
        self.assertEqual(result["Titel"], "Test Todo")
        self.assertEqual(result["Notiz"], "Test Notiz")
        self.assertEqual(result["Deadline"], date(2026, 6, 25))
        self.assertFalse(result["Kalender"])
        self.assertEqual(result["Priorität"], "hoch")
        self.assertEqual(result["Kategorie"], "Studium")

    def test_lade_todo_not_found(self):
        self.mock_repo.finde_todo_mit_id.return_value = None
        result = self.presenter.lade_todo(999)
        self.assertEqual(result, {})
        self.assertIsNone(self.presenter._current_todo)

    def test_save_todo_create_mode(self):
        self.presenter._current_todo = None
        self.mock_repo.naechste_id.return_value = 100

        self.presenter.save_todo(
            titel="New Todo",
            notiz="New Notiz",
            deadline=date(2026, 6, 25),
            calendar=True,
            priority="hoch",
            category="Studium",
            extra={"modul": "Mathe", "gruppenarbeit": False}
        )

        self.mock_repo.speichere.assert_called_once()
        saved_todo = self.mock_repo.speichere.call_args[0][0]
        self.assertEqual(saved_todo._id, 100)
        self.assertEqual(saved_todo.titel, "New Todo")
        self.assertEqual(saved_todo.notiz, "New Notiz")
        self.assertEqual(saved_todo.deadline, date(2026, 6, 25))
        self.assertTrue(saved_todo.calendar)
        self.assertEqual(saved_todo.priority, prioritäten_dict["hoch"])
        self.assertEqual(saved_todo.category, kategorien_dict["Studium"])
        self.assertIsInstance(saved_todo.extra, Studium)
        self.assertEqual(saved_todo.extra.modul, "Mathe")
        self.assertFalse(saved_todo.extra.gruppenarbeit)

    def test_save_todo_edit_mode(self):
        mock_todo = Mock(spec=ToDoModel)
        mock_todo.titel = "Old Todo"
        mock_todo.notiz = "Old Notiz"
        mock_todo.deadline = date(2026, 6, 20)
        mock_todo.calendar = False
        mock_todo.priority = prioritäten_dict["niedrig"]
        mock_todo.category = kategorien_dict["Haushalt"]
        mock_todo.extra = Haushalt(wiederkehrend=True)

        self.presenter._current_todo = mock_todo

        self.presenter.save_todo(
            titel="Updated Todo",
            notiz="Updated Notiz",
            deadline=date(2026, 6, 25),
            calendar=True,
            priority="hoch",
            category="Studium",
            extra={"modul": "Mathe", "gruppenarbeit": True}
        )

        self.assertEqual(mock_todo.titel, "Updated Todo")
        self.assertEqual(mock_todo.notiz, "Updated Notiz")
        self.assertEqual(mock_todo.deadline, date(2026, 6, 25))
        self.assertTrue(mock_todo.calendar)
        self.assertEqual(mock_todo.priority, "hoch")
        self.assertEqual(mock_todo.category, "Studium")
        self.assertEqual(mock_todo.extra, {"modul": "Mathe", "gruppenarbeit": True})