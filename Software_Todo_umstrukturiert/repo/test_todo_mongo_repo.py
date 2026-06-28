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

    def test_speichere(self):
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
        todo = ToDo(
            _todo_id=1,
            titel="Test Todo",
            notiz="Test Description",
            _erledigt= False,
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        
        repo.speichere(todo)
        mock_collection.insert_one.assert_called_once()
        
        call_args = mock_collection.insert_one.call_args
        inserted_doc = call_args[0][0]  # First positional argument
        
        self.assertEqual(inserted_doc["_todo_id"], 1)
        self.assertEqual(inserted_doc["titel"], "Test Todo")
        self.assertEqual(inserted_doc["notiz"], "Test Description")
        self.assertEqual(inserted_doc["_erledigt"], False)
        self.assertEqual(inserted_doc["priority"], "hoch")  # Should be converted to string
        self.assertEqual(inserted_doc["deadline"], "2026-06-10")  # Should be ISO format
        self.assertEqual(inserted_doc["calendar"], False)
        self.assertEqual(inserted_doc["category"], "studium")  # Should be converted to string
        
        self.assertIsNotNone(inserted_doc["extra"])
        self.assertEqual(inserted_doc["extra"]["modul"], "Test")
        self.assertEqual(inserted_doc["extra"]["gruppenarbeit"], False)

  
    def test_finde_todo_mit_id(self):
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
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
            extra=Freizeit(ort="Park", hobby= "walk")
        )
        
        # Convert to dict as it would be stored in MongoDB
        todo_dict: dict[str, Any]= {
            "_todo_id": todo_id,
            "titel": "Test Todo",
            "notiz": "Test Description",
            "_erledigt": False,
            "priority": "niedrig",
            "deadline": "2026-06-20",
            "calendar": False,
            "category": "freizeit",
            "extra": {"ort": "Park", "hobby": "walk"}
        }
        
        mock_collection.find_one.return_value = todo_dict
        result = repo.finde_todo_mit_id(todo_id)
        
        # Verify the result matches the expected todo
        self.assertEqual(result.titel, expected_todo.titel)
        self.assertEqual(result.notiz, expected_todo.notiz)
        self.assertEqual(result.erledigt, expected_todo.erledigt)
        self.assertEqual(result.priority, expected_todo.priority)
        self.assertEqual(result.deadline, expected_todo.deadline)
        self.assertEqual(result.category, expected_todo.category)
        
        # Verify the correct query was made
        mock_collection.find_one.assert_called_with({"_todo_id": todo_id}, projection={"_id": False})

    def test_update_todo(self):
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
        # Test updating a todo
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
            extra=None
        )
        
        repo.update_todo(updated_todo)
    
        # Verify the update query
        expected_update: dict[str, Any] = {
            "_todo_id": todo_id,
            "titel": "Updated Todo",
            "notiz": "Updated Description",
            "_erledigt": True,
            "priority": KEINE_P,
            "deadline": "2026-06-25",
            "calendar": True,
            "category": KEINE,
            "extra": None
        }
        
        mock_collection.update_one.assert_called_with(
            {"_todo_id": todo_id}, 
            {"$set": expected_update}
        )

    def test_delete_todo(self):
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
        # Test deleting a todo
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
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        
        repo.loesche_todo(todo_to_delete)
        mock_collection.delete_one.assert_called_with({"_todo_id": todo_id})

    def test_erledige_todo(self):
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
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
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        
        # Mock the database operations
        mock_collection.find_one.return_value = repo.list_to_doc(incomplete_todo)
        
        # Call the method to toggle completion status
        repo.erledige_todo(todo_id)
        
        # Verify that find_one was called to get the todo
        mock_collection.find_one.assert_called_with({"_todo_id": todo_id}, projection={"_id": False})
        
        # Verify that update_one was called to toggle the status
        mock_collection.update_one.assert_called_with(
            {"_todo_id": todo_id}, 
            {"$set": {"_erledigt": True}}  # Should toggle from False to True
        )
        
        # Reset the mock for the second test case
        mock_collection.reset_mock()
        
        # Now test toggling back from completed to incomplete
        complete_todo = ToDo(
            _todo_id=todo_id,
            titel="Test Todo",
            notiz="Test Description",
            _erledigt=True,  # This todo is completed
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        
        mock_collection.find_one.return_value = repo.list_to_doc(complete_todo)
        repo.erledige_todo(todo_id)
        
        # Verify that it toggles back to False
        mock_collection.update_one.assert_called_with(
            {"_todo_id": todo_id}, 
            {"$set": {"_erledigt": False}}  # Should toggle from True to False
        )

    def test_naechste_id(self):
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
        # Test getting the next available ID
        
        # Case 1: No todos exist yet
        mock_collection.find_one.return_value = None
        result = repo.naechste_id()
        self.assertEqual(result, 1)
        
        # Verify the query for finding the last todo
        mock_collection.find_one.assert_called_with(sort=[("_todo_id", -1)])
        
        # Reset mock for next test case
        mock_collection.reset_mock()
        
        # Case 2: Todos exist, get next ID
        last_todo = {"_todo_id": 42}
        mock_collection.find_one.return_value = last_todo
        result = repo.naechste_id()
        self.assertEqual(result, 43)
