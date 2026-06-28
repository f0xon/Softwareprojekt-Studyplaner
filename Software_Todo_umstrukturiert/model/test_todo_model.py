import unittest
import todo_model
from unittest.mock import Mock
from datetime import date

class TestTodoModel(unittest.TestCase):
    # --- Priority Tests ---
    def test_Priority_constants(self):
        """Test all Priority constants and their attributes"""
        self.assertEqual(todo_model.PRIORITAETEN_DICT["keine"].name, "keine")
        self.assertEqual(todo_model.PRIORITAETEN_DICT["keine"].symbol, "X")
        self.assertEqual(todo_model.PRIORITAETEN_DICT["niedrig"].name, "niedrig")
        self.assertEqual(todo_model.PRIORITAETEN_DICT["niedrig"].symbol, "!")
        self.assertEqual(todo_model.PRIORITAETEN_DICT["mittel"].name, "mittel")
        self.assertEqual(todo_model.PRIORITAETEN_DICT["mittel"].symbol, "!!")
        self.assertEqual(todo_model.PRIORITAETEN_DICT["hoch"].name, "hoch")
        self.assertEqual(todo_model.PRIORITAETEN_DICT["hoch"].symbol, "!!!")

    def test_prioritäten_dict(self):
        """Test the priority dictionary mappings"""
        self.assertEqual(todo_model.PRIORITAETEN_DICT["keine"], todo_model.KEINE_P)
        self.assertEqual(todo_model.PRIORITAETEN_DICT["niedrig"], todo_model.NIEDRIG)
        self.assertEqual(todo_model.PRIORITAETEN_DICT["mittel"], todo_model.MITTEL)
        self.assertEqual(todo_model.PRIORITAETEN_DICT["hoch"], todo_model.HOCH)

    # --- Category Tests ---
    def test_Category_constants(self):
        """Test all Category constants and their attributes"""
        self.assertEqual(todo_model.KEINE.name, "keine")
        self.assertEqual(todo_model.KEINE.farbe, "GREY_300")
        self.assertEqual(todo_model.STUDIUM.name, "Studium")
        self.assertEqual(todo_model.STUDIUM.farbe, "BLUE_100")
        self.assertEqual(todo_model.HAUSHALT.name, "Haushalt")
        self.assertEqual(todo_model.HAUSHALT.farbe, "DEEP_PURPLE_100")
        self.assertEqual(todo_model.FREIZEIT.name, "Freizeit")
        self.assertEqual(todo_model.FREIZEIT.farbe, "TEAL_100")

    def test_kategorien_dict(self):
        """Test the category dictionary mappings"""
        self.assertEqual(todo_model.KATEGORIEN_DICT["keine"], todo_model.KEINE)
        self.assertEqual(todo_model.KATEGORIEN_DICT["Studium"], todo_model.STUDIUM)
        self.assertEqual(todo_model.KATEGORIEN_DICT["Haushalt"], todo_model.HAUSHALT)
        self.assertEqual(todo_mod
        expected_todo = Todel.KATEGORIEN_DICT["Freizeit"], todo_model.FREIZEIT)

    # --- Extra Data Model Tests ---
    def test_Studium(self):
        """Test Studium dataclass"""
        studium = todo_model.Studium(modul="Mathematik", gruppenarbeit=True)
        self.assertEqual(studium.modul, "Mathematik")
        self.assertTrue(studium.gruppenarbeit)

        studium2 = todo_model.Studium(modul="Informatik", gruppenarbeit=False)
        self.assertEqual(studium2.modul, "Informatik")
        self.assertFalse(studium2.gruppenarbeit)

    def test_Haushalt(self):
        """Test Haushalt dataclass"""
        haushalt = todo_model.Haushalt(wiederkehrend=False)
        self.assertFalse(haushalt.wiederkehrend)

        haushalt2 = todo_model.Haushalt(wiederkehrend=True)
        self.assertTrue(haushalt2.wiederkehrend)

    def test_Freizeit(self):
        """Test Freizeit dataclass"""
        freizeit = todo_model.Freizeit(hobby="Spaziergang", ort="Park")
        self.assertEqual(freizeit.hobby, "Spaziergang")
        self.assertEqual(freizeit.ort, "Park")

        freizeit2 = todo_model.Freizeit(hobby="Lesen", ort="Bibliothek")
        self.assertEqual(freizeit2.hobby, "Lesen")
        self.assertEqual(freizeit2.ort, "Bibliothek")

    # --- ToDoModel Tests ---
    def test_ToDoModel_creation_with_Studium(self):
        """Test ToDoModel creation with Studium extra data"""
        todo = todo_model.ToDo(
            _todo_id=1,
            titel="Mathe lernen",
            notiz="Kapitel 1-3 durcharbeiten",
            priority=todo_model.HOCH,
            deadline=date(2024, 12, 1),
            calendar=True,
            category=todo_model.STUDIUM,
            extra=todo_model.Studium(modul="Mathematik", gruppenarbeit=True),
            _erledigt=False
        )

        self.assertEqual(type(todo.todo_id), int)
        self.assertEqual(todo.todo_id, 1)
        self.assertEqual(todo.titel, "Mathe lernen")
        self.assertEqual(todo.notiz, "Kapitel 1-3 durcharbeiten")
        self.assertEqual(todo.priority.name, "hoch")
        self.assertEqual(todo.priority.symbol, "!!!")
        self.assertEqual(type(todo.deadline), date)
        self.assertEqual(todo.deadline, date(2024, 12, 1))
        self.assertTrue(todo.calendar)
        self.assertEqual(todo.category.name, "Studium")
        self.assertEqual(todo.category.farbe, "BLUE_100")
        self.assertIsInstance(todo.extra, todo_model.Studium)
        if isinstance(todo.extra, todo_model.Studium):
            self.assertEqual(todo.extra.modul, "Mathematik")
        else:
            self.assertIsNone(todo.extra)
       

    def test_ToDoModel_creation_with_Haushalt(self):
        """Test ToDoModel creation with Haushalt extra data"""
        todo = todo_model.ToDo(
            _todo_id=2,
            titel="Wohnung putzen",
            notiz="Staubsaugen und wischen",
            priority=todo_model.MITTEL,
            deadline=date(2024, 11, 15),
            calendar=False,
            category=todo_model.HAUSHALT,
            extra=todo_model.Haushalt(wiederkehrend=True),
            _erledigt=True
        )

        self.assertEqual(todo.todo_id, 2)
        self.assertEqual(todo.category.name, "Haushalt")
        self.assertIsInstance(todo.extra, todo_model.Haushalt)
        if isinstance(todo.extra, todo_model.Haushalt):
            self.assertTrue(todo.extra.wiederkehrend)
        self.assertTrue(todo.erledigt)

    def test_ToDoModel_creation_with_Freizeit(self):
        """Test ToDoModel creation with Freizeit extra data"""
        todo = todo_model.ToDo(
            _todo_id=3,
            titel="Wandertour",
            notiz="Gipfelsturm",
            priority=todo_model.NIEDRIG,
            deadline=date(2024, 10, 10),
            calendar=True,
            category=todo_model.FREIZEIT,
            extra=todo_model.Freizeit(hobby="Wandern", ort="Alpen"),
            _erledigt=False
        )

        self.assertEqual(todo.todo_id, 3)
        self.assertEqual(todo.category.name, "Freizeit")
        self.assertIsInstance(todo.extra, todo_model.Freizeit)
        if isinstance(todo.extra, todo_model.Freizeit):
            self.assertEqual(todo.extra.hobby, "Wandern")
            self.assertEqual(todo.extra.ort, "Alpen")

    def test_ToDoModel_creation_with_no_extra(self):
        """Test ToDoModel creation without extra data"""
        todo = todo_model.ToDo(
            _todo_id=4,
            titel="Einkaufen",
            notiz="Milch, Eier, Brot",
            priority=todo_model.KEINE_P,
            deadline=date(2024, 9, 1),
            calendar=False,
            category=todo_model.KEINE,
            extra=None,
            _erledigt=False
        )

        self.assertEqual(todo.todo_id, 4)
        self.assertEqual(todo.category.name, "keine")
        self.assertIsNone(todo.extra)
        self.assertFalse(todo.erledigt)

    # --- Toggle Completion Tests ---
    def test_toggle_erledigt_todo(self):
        """Test the toggle_erledigt_todo method"""
        todo = todo_model.ToDo(
            _todo_id=5,
            titel="Test",
            notiz="Testbeschreibung",
            priority=todo_model.KEINE_P,
            deadline=date(2024, 1, 1),
            calendar=False,
            category=todo_model.KEINE,
            _erledigt=False
        )

        # Initial state
        self.assertFalse(todo.erledigt)

        # First toggle: False -> True
        todo.toggle_erledigt_todo()
        self.assertTrue(todo.erledigt)

        # Second toggle: True -> False
        todo.toggle_erledigt_todo()
        self.assertFalse(todo.erledigt)

        # Third toggle: False -> True
        todo.toggle_erledigt_todo()
        self.assertTrue(todo.erledigt)

    # --- Mutation Tests ---
    def test_ToDoModel_change_category_and_extra(self):
        """Test changing category and extra after creation"""
        todo = todo_model.ToDo(
            _todo_id=6,
            titel="Aktivität",
            notiz="Test",
            priority=todo_model.MITTEL,
            deadline=date(2024, 1, 1),
            calendar=True,
            category=todo_model.STUDIUM,
            extra=todo_model.Studium(modul="Informatik", gruppenarbeit=True),
            _erledigt=False
        )

        # Change to Haushalt
        todo.category = todo_model.HAUSHALT
        todo.extra = todo_model.Haushalt(wiederkehrend=False)
        self.assertEqual(todo.category.name, "Haushalt")
        self.assertEqual(todo.category.farbe, "DEEP_PURPLE_100")
        self.assertIsInstance(todo.extra, todo_model.Haushalt)
        self.assertFalse(todo.extra.wiederkehrend)

        # Change to Freizeit
        todo.category = todo_model.FREIZEIT
        todo.extra = todo_model.Freizeit(hobby="Kino", ort="Cinemax")
        self.assertEqual(todo.category.name, "Freizeit")
        self.assertIsInstance(todo.extra, todo_model.Freizeit)
        self.assertEqual(todo.extra.hobby, "Kino")
        self.assertEqual(todo.extra.ort, "Cinemax")

        # Change to keine with no extra
        todo.category = todo_model.KEINE
        todo.extra = None
        self.assertEqual(todo.category.name, "keine")
        self.assertIsNone(todo.extra)

    def test_ToDoModel_change_priority(self):
        """Test changing priority after creation"""
        todo = todo_model.ToDo(
            _todo_id=7,
            titel="Priority Test",
            notiz="Test",
            priority=todo_model.KEINE_P,
            deadline=date(2024, 1, 1),
            calendar=False,
            category=todo_model.KEINE,
            _erledigt=False
        )

        self.assertEqual(todo.priority.name, "keine")

        todo.priority = todo_model.NIEDRIG
        self.assertEqual(todo.priority.name, "niedrig")

        todo.priority = todo_model.MITTEL
        self.assertEqual(todo.priority.name, "mittel")

        todo.priority = todo_model.HOCH
        self.assertEqual(todo.priority.name, "hoch")

    # --- Mock Tests (for potential future repository integration) ---
    def test_ToDoModel_with_mock_repository_data(self):
        """Test ToDoModel with mock data (simulating repository behavior)"""
        # Mock a repository that returns test data
        mock_repo = Mock()
        mock_repo.get_priority.return_value = todo_model.HOCH
        mock_repo.get_category.return_value = todo_model.STUDIUM
        mock_repo.get_extra.return_value = todo_model.Studium(modul="Physik", gruppenarbeit=False)

        # Create ToDoModel using mock data
        todo = todo_model.ToDo(
            _todo_id=100,
            titel=mock_repo.get_title.return_value or "Mock Todo",
            notiz="Mock Notiz",
            priority=mock_repo.get_priority(),
            deadline=date(2024, 6, 15),
            calendar=True,
            category=mock_repo.get_category(),
            extra=mock_repo.get_extra(),
            _erledigt=False
        )

        self.assertEqual(todo.priority.name, "hoch")
        self.assertEqual(todo.category.name, "Studium")
        self.assertIsInstance(todo.extra, todo_model.Studium)
        if isinstance(todo.extra, todo_model.Studium):
            self.assertEqual(todo.extra.modul, "Physik")
            self.assertFalse(todo.extra.gruppenarbeit)