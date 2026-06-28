import unittest
from unittest.mock import Mock
from todo_mongo_repo import MongoTodoRepo
from datetime import date
from model.todo_model import (
    ToDo,
    HOCH,
    MITTEL,
    NIEDRIG,
    KEINE_P,
    STUDIUM,
    KEINE,
    HAUSHALT,
    FREIZEIT,
    Studium,
    Haushalt,
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
        
        # Test saving a todo - verify data transformation and insertion
        todo = ToDo(
            _todo_id=1,
            titel="Test Todo",
            notiz="Test Description",
            erledigt=False,
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        
        repo.speichere(todo)
        
        # Verify insert_one was called exactly once
        mock_collection.insert_one.assert_called_once()
        
        # Get the argument that was passed to insert_one
        call_args = mock_collection.insert_one.call_args
        inserted_doc = call_args[0][0]  # First positional argument
        
        # Verify the document structure and content
        self.assertEqual(inserted_doc["_todo_id"], 1)
        self.assertEqual(inserted_doc["titel"], "Test Todo")
        self.assertEqual(inserted_doc["notiz"], "Test Description")
        self.assertEqual(inserted_doc["erledigt"], False)
        self.assertEqual(inserted_doc["priority"], "hoch")  # Should be converted to string
        self.assertEqual(inserted_doc["deadline"], "2026-06-10")  # Should be ISO format
        self.assertEqual(inserted_doc["calendar"], False)
        self.assertEqual(inserted_doc["category"], "studium")  # Should be converted to string
        
        # Verify extra field is properly converted to dict
        self.assertIsNotNone(inserted_doc["extra"])
        self.assertEqual(inserted_doc["extra"]["modul"], "Test")
        self.assertEqual(inserted_doc["extra"]["gruppenarbeit"], False)

    def test_add_todo(self):
        # Setup for this test
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
        # Test adding a todo (this seems to be a duplicate of test_speichere, so let's test a different scenario)
        todo = ToDo(
            _todo_id=2,
            titel="Hausaufgaben",
            notiz="Englisch Übungen",
            erledigt=False,
            priority=MITTEL,
            deadline=date(2026, 6, 15),
            calendar=True,
            category=HAUSHALT,
            extra=Haushalt(raum="Küche", wiederkehrend=True)
        )
        
        repo.speichere(todo)
        # Verify the document conversion and insertion
        expected_doc = {
            "_todo_id": 2,
            "titel": "Hausaufgaben",
            "notiz": "Englisch Übungen",
            "erledigt": False,
            "priority": "mittel",
            "deadline": "2026-06-15",
            "calendar": True,
            "category": "haushalt",
            "extra": {"raum": "Küche", "wiederkehrend": True}
        }
        mock_collection.insert_one.assert_called_with(expected_doc)

    def test_get_todo(self):
        # Setup for this test
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
        # Test finding a todo by ID
        todo_id = 1
        expected_todo = ToDo(
            _todo_id=todo_id,
            titel="Test Todo",
            notiz="Test Description",
            erledigt=False,
            priority=NIEDRIG,
            deadline=date(2026, 6, 20),
            calendar=False,
            category=FREIZEIT,
            extra=Freizeit(ort="Park", sozial=True)
        )
        
        # Convert to dict as it would be stored in MongoDB
        todo_dict = {
            "_todo_id": todo_id,
            "titel": "Test Todo",
            "notiz": "Test Description",
            "erledigt": False,
            "priority": "niedrig",
            "deadline": "2026-06-20",
            "calendar": False,
            "category": "freizeit",
            "extra": {"ort": "Park", "sozial": True}
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
        # Setup for this test
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
            erledigt=True,
            priority=KEINE_P,
            deadline=date(2026, 6, 25),
            calendar=True,
            category=KEINE,
            extra=None
        )
        
        repo.update_todo(updated_todo)
        
        # Verify the update query
        expected_update = {
            "_todo_id": todo_id,
            "titel": "Updated Todo",
            "notiz": "Updated Description",
            "erledigt": True,
            "priority": None,
            "deadline": "2026-06-25",
            "calendar": True,
            "category": None,
            "extra": None
        }
        
        mock_collection.update_one.assert_called_with(
            {"_todo_id": todo_id}, 
            {"$set": expected_update}
        )

    def test_delete_todo(self):
        # Setup for this test
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
            erledigt=False,
            priority=HOCH,
            deadline=date(2026, 6, 30),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        
        repo.loesche_todo(todo_to_delete)
        mock_collection.delete_one.assert_called_with({"_todo_id": todo_id})

    def test_erledige_todo(self):
        # Setup for this test
        mock_client = Mock()
        mock_db = Mock()
        mock_collection = Mock()
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        repo = MongoTodoRepo(mock_client)
        
        # Test toggling todo completion status
        todo_id = 1
        
        # Mock a todo that is not completed
        incomplete_todo = ToDo(
            _todo_id=todo_id,
            titel="Test Todo",
            notiz="Test Description",
            erledigt=False,
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        
        # Mock the database operations
        mock_collection.find_one.return_value = incomplete_todo.to_dict()
        
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
            erledigt=True,  # This todo is completed
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        
        mock_collection.find_one.return_value = complete_todo.to_dict()
        repo.erledige_todo(todo_id)
        
        # Verify that it toggles back to False
        mock_collection.update_one.assert_called_with(
            {"_todo_id": todo_id}, 
            {"$set": {"_erledigt": False}}  # Should toggle from True to False
        )

    def test_naechste_id(self):
        # Setup for this test
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

if __name__ == '__main__':
    unittest.main()