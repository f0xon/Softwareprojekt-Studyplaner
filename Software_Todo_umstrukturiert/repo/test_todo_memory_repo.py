import unittest
from todo_memory_repo import InMemoryTodoRepo
from datetime import date
from model.todo_model import (
    ToDo,
    HOCH,
    MITTEL,
    NIEDRIG,
    STUDIUM,
    FREIZEIT,
    Studium,
    Freizeit,
)

class TestTodoMemoryRepo(unittest.TestCase):
   
    def setUp(self):
        self.repo = InMemoryTodoRepo()

    def test_speichere(self):
        initial_count = len(self.repo.lade_alle())
        todo = ToDo(
            _todo_id=100,
            titel="Test Todo",
            notiz="Test Description",
            _erledigt=False,
            priority=HOCH,
            deadline=date(2026, 6, 10),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="Test", gruppenarbeit=False)
        )
        self.repo.speichere(todo)
        
        # Verify the todo was added
        self.assertEqual(len(self.repo.lade_alle()), initial_count + 1)
        self.assertIn(todo, self.repo.lade_alle())

    def test_update_todo(self):
        original_todo = self.repo.finde_todo_mit_id(1)
        self.assertIsNotNone(original_todo)
        
        if original_todo is not None:
            original_todo.titel = "Updated Title"
            original_todo.notiz = "Updated Note"
            original_todo._erledigt = True # pyright: ignore[reportPrivateUsage]
            original_todo.priority = NIEDRIG
            original_todo.deadline = date(2026, 6, 20)
            original_todo.calendar = True
            original_todo.category = FREIZEIT
            original_todo.extra = Freizeit(hobby="Updated", ort="Updated")
        
            self.repo.update_todo(original_todo)
        result = self.repo.finde_todo_mit_id(1)
        if result is not None:
            self.assertEqual(result.titel, "Updated Title")
            self.assertEqual(result.notiz, "Updated Note")
            self.assertEqual(result.erledigt, True)

    def test_lade_alle(self):
        todos = self.repo.lade_alle()
        self.assertGreater(len(todos), 0)
        self.assertEqual(len(self.repo.lade_alle()), len(self.repo._todos)) # pyright: ignore[reportPrivateUsage]
        self.assertIsInstance(todos, list)
        self.assertIsInstance(todos[0], ToDo)

    def test_finde_todo_mit_id(self):
        result = self.repo.finde_todo_mit_id(1)
        self.assertIsNotNone(result)
        if result is not None:
            self.assertEqual(result.todo_id, 1)
            self.assertEqual(result.titel, "Mathe lernen")
        
        # Test non-existent ID
        result = self.repo.finde_todo_mit_id(999)
        self.assertIsNone(result)

    def test_erledige_todo(self):
            todo = self.repo.finde_todo_mit_id(1)
            self.assertIsNotNone(todo)
            if todo is not  None:
                initial_status = todo.erledigt
            
                self.repo.erledige_todo(1)
                updated_todo = self.repo.finde_todo_mit_id(1)
                
                # Verify the status was toggled
                if updated_todo is not None:
                    self.assertEqual(updated_todo.erledigt, not initial_status)
                
                # Toggle back
                self.repo.erledige_todo(1)
                updated_todo = self.repo.finde_todo_mit_id(1)
                if updated_todo is not None:
                    self.assertEqual(updated_todo.erledigt, initial_status)

    def test_loesche_todo(self):
        todo = self.repo.finde_todo_mit_id(1)
        self.assertIsNotNone(todo)
        
        initial_count = len(self.repo.lade_alle())
        if todo is not None:
            self.repo.loesche_todo(todo)
        
        # Verify the todo was removed
        self.assertEqual(len(self.repo.lade_alle()), initial_count - 1)
        self.assertIsNone(self.repo.finde_todo_mit_id(1))


    def test_filtere_todos(self):
        # Filter by category
        studium_todos = self.repo.filtere_todos("Studium", "alle", "alle")
        self.assertGreater(len(studium_todos), 0)
        for todo in studium_todos:
            self.assertEqual(todo.category, STUDIUM)
        
        # Filter by priority
        hoch_todos = self.repo.filtere_todos("alle", "hoch", "alle")
        self.assertGreater(len(hoch_todos), 0)
        for todo in hoch_todos:
            self.assertEqual(todo.priority, HOCH)
        
        # Filter by status
        offen_todos = self.repo.filtere_todos("alle", "alle", "offen")
        for todo in offen_todos:
            self.assertFalse(todo.erledigt)
        erledigt_todos = self.repo.filtere_todos("alle", "alle", "erledigt")
        for todo in erledigt_todos:
            self.assertTrue(todo.erledigt)

    def test_naechste_id(self):
        # Get current next ID
        next_id = self.repo.naechste_id()
        
        # Should be higher than the highest existing ID
        all_todos = self.repo.lade_alle()
        max_id = max(todo.todo_id for todo in all_todos)
        self.assertEqual(next_id, max_id + 1)
        
        # Add a new todo with the next ID
        new_todo = ToDo(
            _todo_id=next_id,
            titel="New Todo",
            notiz="New Description",
            _erledigt=False,
            priority=MITTEL,
            deadline=date(2026, 6, 25),
            calendar=False,
            category=STUDIUM,
            extra=Studium(modul="New", gruppenarbeit=False)
        )
        self.repo.speichere(new_todo)
        
        # The next ID should have incremented
        updated_next_id = self.repo.naechste_id()
        self.assertEqual(updated_next_id, next_id + 1)
