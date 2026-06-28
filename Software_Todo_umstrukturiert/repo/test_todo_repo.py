import unittest
from unittest.mock import Mock
from todo_repo import TodoRepo
from model.todo_model import ToDo

class TestTodoRepo(unittest.TestCase):


    #TODO was 


    def __init__(self):
        self.mock_db = Mock()
        self.repo = TodoRepo(self.mock_db)

    def test_add_todo(self):
        todo = Todo("Test Todo", "Test Description")
        self.repo.add_todo(todo)
        self.mock_db.add_todo.assert_called_with(todo)

    def test_get_todo(self):
        todo_id = 1
        expected_todo = Todo("Test Todo", "Test Description")
        self.mock_db.get_todo.return_value = expected_todo
        result = self.repo.get_todo(todo_id)
        self.assertEqual(result, expected_todo)
        self.mock_db.get_todo.assert_called_with(todo_id)

    def test_update_todo(self):
        todo_id = 1
        updated_todo = Todo("Updated Todo", "Updated Description")
        self.repo.update_todo(todo_id, updated_todo)
        self.mock_db.update_todo.assert_called_with(todo_id, updated_todo)

    def test_delete_todo(self):
        todo_id = 1
        self.repo.delete_todo(todo_id)
        self.mock_db.delete_todo.assert_called_with(todo_id)

if __name__ == '__main__':
    unittest.main()