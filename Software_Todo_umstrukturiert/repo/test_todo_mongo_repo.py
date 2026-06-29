from typing import Any
import unittest
from unittest.mock import Mock
from todo_mongo_repo import MongoTodoRepo
from datetime import date
from model.todo_model import (
    ToDo,
    HOCH,
    NIEDRIG,
    KEINE_P,
    STUDIUM,
    KEINE,
    FREIZEIT,
    Studium,
    Freizeit,
)

class TestTodoMongoRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_db = Mock()
        self.mock_collection = Mock()
        self.mock_db.todos = self.mock_collection
        self.repo = MongoTodoRepo(self.mock_db)

    def test_speichere(self):
        todo = ToDo(
            _todo_id=1,
            titel="Test Todo",
            notiz="Test Description",
            _erledigt=False,
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False),
        )

        self.repo.speichere(todo)
        self.mock_collection.insert_one.assert_called_once()

        call_args = self.mock_collection.insert_one.call_args
        inserted_doc = call_args[0][0]  # First positional argument

        self.assertEqual(inserted_doc["_todo_id"], 1)
        self.assertEqual(inserted_doc["titel"], "Test Todo")
        self.assertEqual(inserted_doc["notiz"], "Test Description")
        self.assertEqual(inserted_doc["_erledigt"], False)
        self.assertEqual(inserted_doc["priority"], "hoch")
        self.assertEqual(inserted_doc["deadline"], "2026-06-10")
        self.assertEqual(inserted_doc["calendar"], False)
        self.assertEqual(inserted_doc["category"], "Studium")
        self.assertIsNotNone(inserted_doc["extra"])
        self.assertEqual(inserted_doc["extra"]["modul"], "Test")
        self.assertEqual(inserted_doc["extra"]["gruppenarbeit"], False)

    def test_finde_todo_mit_id(self):
        todo_id = 1
        expected_todo = ToDo(
            _todo_id=todo_id,
            titel="Test Todo",
            notiz="Test Description",
            _erledigt=False,
            priority=NIEDRIG,
            deadline=date(2026, 6, 20),
            calendar=False,
            category=FREIZEIT,
            extra=Freizeit(ort="Park", hobby="walk"),
        )

        todo_dict: dict[str, Any] = {
            "_todo_id": todo_id,
            "titel": "Test Todo",
            "notiz": "Test Description",
            "_erledigt": False,
            "priority": "niedrig",
            "deadline": "2026-06-20",
            "calendar": False,
            "category": "Freizeit",
            "extra": {"ort": "Park", "hobby": "walk"},
        }

        self.mock_collection.find_one.return_value = todo_dict
        result = self.repo.finde_todo_mit_id(todo_id)

        self.assertEqual(result.titel, expected_todo.titel)
        self.assertEqual(result.notiz, expected_todo.notiz)
        self.assertEqual(result.erledigt, expected_todo.erledigt)
        self.assertEqual(result.priority, expected_todo.priority)
        self.assertEqual(result.deadline, expected_todo.deadline)
        self.assertEqual(result.category, expected_todo.category)
        self.mock_collection.find_one.assert_called_with({"_todo_id": todo_id}, projection={"_id": False})

    def test_update_todo(self):
        todo_id = 1
        updated_todo = ToDo(
            _todo_id=todo_id,
            titel="Updated Todo",
            notiz="Updated Description",
            _erledigt=True,
            priority=KEINE_P,
            deadline=date(2026, 6, 25),
            calendar=True,
            category=KEINE,
            extra=None,
        )

        self.repo.update_todo(updated_todo)

        expected_update: dict[str, Any] = {
            "_todo_id": todo_id,
            "titel": "Updated Todo",
            "notiz": "Updated Description",
            "_erledigt": True,
            "priority": "keine",
            "deadline": "2026-06-25",
            "calendar": True,
            "category": "keine",
            "extra": None,
        }

        self.mock_collection.update_one.assert_called_with(
            {"_todo_id": todo_id},
            {"$set": expected_update},
        )

    def test_delete_todo(self):
        todo_id = 1
        todo_to_delete = ToDo(
            _todo_id=todo_id,
            titel="Todo to delete",
            notiz="This will be deleted",
            _erledigt=False,
            priority=HOCH,
            deadline=date(2026, 6, 30),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False),
        )

        self.repo.loesche_todo(todo_to_delete)
        self.mock_collection.delete_one.assert_called_once_with({"_todo_id": todo_id})

    def test_erledige_todo(self):
        todo_id = 1
        incomplete_todo = ToDo(
            _todo_id=todo_id,
            titel="Test Todo",
            notiz="Test Description",
            _erledigt=False,
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False),
        )

        self.mock_collection.find_one.return_value = self.repo.list_to_doc(incomplete_todo)
        self.repo.erledige_todo(todo_id)

        self.mock_collection.find_one.assert_called_once_with({"_todo_id": todo_id}, projection={"_id": False})
        self.mock_collection.update_one.assert_called_once_with(
            {"_todo_id": todo_id},
            {"$set": {"_erledigt": True}},
        )

        self.mock_collection.reset_mock()

        complete_todo = ToDo(
            _todo_id=todo_id,
            titel="Test Todo",
            notiz="Test Description",
            _erledigt=True,
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False),
        )

        self.mock_collection.find_one.return_value = self.repo.list_to_doc(complete_todo)
        self.repo.erledige_todo(todo_id)

        self.mock_collection.update_one.assert_called_once_with(
            {"_todo_id": todo_id},
            {"$set": {"_erledigt": False}},
        )

    def test_naechste_id(self):
        self.mock_collection.find_one.return_value = None
        result = self.repo.naechste_id()
        self.assertEqual(result, 1)
        self.mock_collection.find_one.assert_called_once_with(sort=[("_todo_id", -1)])

        self.mock_collection.reset_mock()
        self.mock_collection.find_one.return_value = {"_todo_id": 42}
        result = self.repo.naechste_id()
        self.assertEqual(result, 43)
