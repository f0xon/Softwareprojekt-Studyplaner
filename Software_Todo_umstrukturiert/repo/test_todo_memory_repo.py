import unittest
from todo_memory_repo import InMemoryTodoRepo
from model.todo_model import Todo

class TestTodoMemoryRepo(unittest.TestCase):
    def __init__(self):
        self.repo = InMemoryTodoRepo()

    def test_add_todo(self):
        todo = Todo("Test Todo", "Test Description")
        self.repo.add_todo(todo)
        self.assertEqual(len(self.repo.todos), 1)
        self.assertEqual(self.repo.todos[0], todo)

    def test_get_todo(self):
        todo = Todo("Test Todo", "Test Description")
        self.repo.add_todo(todo)
        result = self.repo.get_todo(0)
        self.assertEqual(result, todo)

    def test_update_todo(self):
        todo = Todo("Test Todo", "Test Description")
        self.repo.add_todo(todo)
        updated_todo = Todo("Updated Todo", "Updated Description")
        self.repo.update_todo(0, updated_todo)
        self.assertEqual(self.repo.todos[0], updated_todo)

    def test_delete_todo(self):
        todo = Todo("Test Todo", "Test Description")
        self.repo.add_todo(todo)
        self.repo.delete_todo(0)
        self.assertEqual(len(self.repo.todos), 0)

if __name__ == '__main__':
    unittest.main()