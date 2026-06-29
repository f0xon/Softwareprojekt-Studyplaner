import unittest
from unittest.mock import Mock
from datetime import date
from model.todo_model import (
    KATEGORIEN_DICT,
    PRIORITAETEN_DICT,
    Freizeit,
    Haushalt,
    Studium,
    ToDo,
)
from repo.todo_repo import TodoRepo
from erzeuge_todo_presenter import TodoDetailPresenter

class TestTodoDetailPresenter(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock(spec=TodoRepo)
        self.presenter = TodoDetailPresenter(self.mock_repo)

    def test_initialization(self):
        self.assertIsInstance(self.presenter.repo, Mock)
        self.assertIsNone(self.presenter.current_todo)

    def test_is_create_mode_with_modus_set(self):
        self.assertEqual(self.presenter._modus, "create")
        self.assertTrue(self.presenter.is_create_mode)

        self.presenter.set_modus("edit")
        self.assertEqual(self.presenter._modus, "edit")
        self.assertTrue(self.presenter.is_edit_mode)

        self.presenter.set_modus("create")
        self.assertEqual(self.presenter._modus, "create")
        self.assertTrue(self.presenter.is_create_mode)

    def test_is_edit_mode_with_modus_set(self):
        self.presenter.set_modus("edit")
        self.assertTrue(self.presenter.is_edit_mode)

        self.presenter.set_modus("create")
        self.assertFalse(self.presenter.is_edit_mode)
        self.assertTrue(self.presenter.is_create_mode)

    def test_map_priority(self):
        self.assertEqual(self.presenter.map_priority("keine"), PRIORITAETEN_DICT["keine"])
        self.assertEqual(self.presenter.map_priority("niedrig"), PRIORITAETEN_DICT["niedrig"])
        self.assertEqual(self.presenter.map_priority("mittel"), PRIORITAETEN_DICT["mittel"])
        self.assertEqual(self.presenter.map_priority("hoch"), PRIORITAETEN_DICT["hoch"])
        self.assertIsNone(self.presenter.map_priority("invalid"))

    def test_map_category(self):
        self.assertEqual(self.presenter.map_category("keine"), KATEGORIEN_DICT["keine"])
        self.assertEqual(self.presenter.map_category("Studium"), KATEGORIEN_DICT["Studium"])
        self.assertEqual(self.presenter.map_category("Haushalt"), KATEGORIEN_DICT["Haushalt"])
        self.assertEqual(self.presenter.map_category("Freizeit"), KATEGORIEN_DICT["Freizeit"])
        self.assertIsNone(self.presenter.map_category("invalid"))

    def test_build_extra_studium(self):
        data: dict[str, str|bool] = {"modul": "Mathe", "gruppenarbeit": True}
        extra = self.presenter.build_extra("Studium", data)
        self.assertIsInstance(extra, Studium)
        if isinstance(extra, Studium):
            self.assertEqual(extra.modul, "Mathe")
            self.assertTrue(extra.gruppenarbeit)

    def test_build_extra_haushalt(self):
        data = {"wiederkehrend": False}
        extra = self.presenter.build_extra("Haushalt", data)
        self.assertIsInstance(extra, Haushalt)
        if isinstance(extra, Haushalt):
            self.assertFalse(extra.wiederkehrend)

    def test_build_extra_freizeit(self):
        data = {"hobby": "Lesen", "ort": "Zuhause"}
        extra = self.presenter.build_extra("Freizeit", data)
        self.assertIsInstance(extra, Freizeit)
        if isinstance(extra, Freizeit):
            self.assertEqual(extra.hobby, "Lesen")
            self.assertEqual(extra.ort, "Zuhause")

    def test_build_extra_empty_data(self):
        extra = self.presenter.build_extra("Studium", {})
        self.assertEqual(extra, {})

    def test_build_extra_invalid_category(self):
        with self.assertRaises(TypeError):
            self.presenter.build_extra("Invalid", {"key": "value"})

    def test_lade_todo_success(self):
        mock_todo = ToDo(
            _todo_id=1,
            titel="Test Todo",
            notiz="Test Notiz",
            priority=PRIORITAETEN_DICT["hoch"],
            deadline=date(2026, 6, 25),
            calendar=False,
            category=KATEGORIEN_DICT["Studium"],
        )

        self.mock_repo.finde_todo_mit_id.return_value = mock_todo

        result = self.presenter.lade_todo(1)

        self.mock_repo.finde_todo_mit_id.assert_called_once_with(1)
        self.assertEqual(self.presenter.current_todo, mock_todo)
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
        self.assertIsNone(self.presenter.current_todo)

    def test_save_todo_create_mode(self):
        self.presenter._current_todo = None # pyright: ignore[reportPrivateUsage]
        self.mock_repo.naechste_id.return_value = 100

        self.presenter.save_todo(
            titel="New Todo",
            notiz="New Notiz",
            deadline=date(2026, 6, 25),
            calendar="True",
            priority="hoch",
            category="Studium",
            extra={"modul": "Mathe", "gruppenarbeit": False}
        )

        self.mock_repo.speichere.assert_called_once()
        saved_todo = self.mock_repo.speichere.call_args[0][0]
        self.assertEqual(saved_todo._todo_id, 100)
        self.assertEqual(saved_todo.titel, "New Todo")
        self.assertEqual(saved_todo.notiz, "New Notiz")
        self.assertEqual(saved_todo.deadline, date(2026, 6, 25))
        self.assertTrue(saved_todo.calendar)
        self.assertEqual(saved_todo.priority, PRIORITAETEN_DICT["hoch"])
        self.assertEqual(saved_todo.category, KATEGORIEN_DICT["Studium"])
        self.assertIsInstance(saved_todo.extra, Studium)
        self.assertEqual(saved_todo.extra.modul, "Mathe")
        self.assertFalse(saved_todo.extra.gruppenarbeit)

    def test_save_todo_edit_mode(self):
        mock_todo = ToDo(
            _todo_id=1,
            titel="Old Todo",
            notiz="Old Notiz",
            priority=PRIORITAETEN_DICT["niedrig"],
            deadline=date(2026, 6, 20),
            calendar=False,
            category=KATEGORIEN_DICT["Haushalt"],
            extra=Haushalt(wiederkehrend=True),
        )

        self.presenter._current_todo = mock_todo  # pyright: ignore[reportPrivateUsage]

        self.presenter.save_todo(
            titel="Updated Todo",
            notiz="Updated Notiz",
            deadline=date(2026, 6, 25),
            calendar="True",
            priority="hoch",
            category="Studium",
            extra={"modul": "Mathe", "gruppenarbeit": True}
        )

        self.assertEqual(mock_todo.titel, "Updated Todo")
        self.assertEqual(mock_todo.notiz, "Updated Notiz")
        self.assertEqual(mock_todo.deadline, date(2026, 6, 25))
        self.assertTrue(mock_todo.calendar)
        self.assertEqual(mock_todo.priority, PRIORITAETEN_DICT["hoch"])
        self.assertEqual(mock_todo.category, KATEGORIEN_DICT["Studium"])
        self.assertIsInstance(mock_todo.extra, Studium)
        if isinstance(mock_todo.extra, Studium):
            self.assertEqual(mock_todo.extra.modul, "Mathe")
            self.assertTrue(mock_todo.extra.gruppenarbeit)