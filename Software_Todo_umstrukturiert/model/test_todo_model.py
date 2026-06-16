import unittest
import todo_model
from unittest.mock import Mock


class TestTodoModel(unittest.TestCase):
    def test_Priority(self):
        self.assertEqual(todo_model.keine_p.name, "keine")
        self.assertEqual(todo_model.niedrig.name, "niedrig")
        self.assertEqual(todo_model.mittel.name, "mittel")
        self.assertEqual(todo_model.hoch.name, "hoch")

    def test_Category(self):
        self.assertEqual(todo_model.keine.name, "keine")
        self.assertEqual(todo_model.studium.name, "Studium")
        self.assertEqual(todo_model.haushalt.name, "Haushalt")
        self.assertEqual(todo_model.freizeit.name, "Freizeit")

    def test_Studium(self):
        studium = todo_model.Studium(modul="Mathematik", gruppenarbeit=True)
        self.assertEqual(studium.modul, "Mathematik")
        self.assertTrue(studium.gruppenarbeit)

    def test_Haushalt(self):
        haushalt = todo_model.Haushalt(wiederkehrend=False)
        self.assertFalse(haushalt.wiederkehrend)

    def test_Freizeit(self):
        freizeit = todo_model.Freizeit(hobby="Spaziergang", ort="Park")
        self.assertEqual(freizeit.hobby, "Spaziergang")
        self.assertEqual(freizeit.ort, "Park")

    def test_ToDoModel(self):
        mock_Priority = Mock()
        mock_Priority.lade_alle.return_value = [todo_model.Priority("keine", "X"), todo_model.Priority("niedrig", "!"), todo_model.Priority("mittel", "!!"), todo_model.Priority("hoch", "!!!")]
        mock_Category = Mock()
        mock_Category.lade_alle.return_value = [todo_model.Category("keine", "GREY_300"), todo_model.Category("Studium", "BLUE_100"), todo_model.Category("Haushalt", "DEEP_PURPLE_100"), todo_model.Category("Freizeit", "TEAL_100")]
        mock_Studium = Mock()
        mock_Studium.lade_alle.return_value = [todo_model.Studium(modul="Mathematik", gruppenarbeit=True)]
        mock_Haushalt = Mock()
        mock_Haushalt.lade_alle.return_value = [todo_model.Haushalt(wiederkehrend=False)]
        mock_Freizeit = Mock()
        mock_Freizeit.lade_alle.return_value = [todo_model.Freizeit(hobby="Spaziergang", ort="Park")]
        todo = todo_model.ToDoModel(
            _id=1, # type: ignore
            titel="Test ToDo",
            notiz="Dies ist ein Test.",
            priority=mock_Priority.lade_alle()[0],
            deadline=todo_model.date(2024, 1, 1),
            calendar=True,
            category=mock_Category.lade_alle()[0],
            extra=mock_Studium.lade_alle()[0],
            _erledigt=False
            )
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.titel, "Test ToDo")
        self.assertEqual(todo.notiz, "Dies ist ein Test.")
        self.assertEqual(todo.priority.name, "keine")
        self.assertEqual(todo.deadline, todo_model.date(2024, 1, 1))
        self.assertTrue(todo.calendar)
        for category in mock_Category.lade_alle():
        self.assertEqual(todo.category.name, "keine")