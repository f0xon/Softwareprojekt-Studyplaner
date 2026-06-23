import unittest
from unittest.mock import Mock
from model.todo_model import ToDoModel
from model.todo_model import keine_p, niedrig, mittel, hoch
from model.todo_model import studium, haushalt, freizeit
from ToDoListe_model import ToDoListModel

class TestToDoListModel(unittest.TestCase):

    def test_initialization(self):
        model = ToDoListModel()
        self.assertEqual(len(model.dummydaten), 16)
        self.assertEqual(len(model.todos), 0)
        self.assertEqual(len(model.result), 16)
        self.assertIsNot(model.result, model.dummydaten)  
        
    def test_add_todo(self):
        model = ToDoListModel()
        mock_todo = Mock(spec=ToDoModel)
        mock_todo._id = 100
        mock_todo.titel = "Mock Todo"

        initial_count = len(model.dummydaten)
        model.add_todo(mock_todo)

        self.assertEqual(len(model.dummydaten), initial_count + 1)
        self.assertEqual(model.dummydaten[-1]._id, 100) # pyright: ignore[reportPrivateUsage]
        self.assertEqual(model.dummydaten[-1].titel, "Mock Todo")

    def test_priority_aus_name(self):
        model = ToDoListModel()
        self.assertEqual(model._priority_aus_name("keine"), keine_p) # pyright: ignore[reportPrivateUsage]
        self.assertEqual(model._priority_aus_name("niedrig"), niedrig)# pyright: ignore[reportPrivateUsage]
        self.assertEqual(model._priority_aus_name("mittel"), mittel)# pyright: ignore[reportPrivateUsage]
        self.assertEqual(model._priority_aus_name("hoch"), hoch)# pyright: ignore[reportPrivateUsage]
        with self.assertRaises(ValueError):
            model._priority_aus_name("invalid") # pyright: ignore[reportPrivateUsage]

    def test_category_aus_name(self):
        model = ToDoListModel()
        self.assertEqual(model._category_aus_name("Studium"), studium) # pyright: ignore[reportPrivateUsage]
        self.assertEqual(model._category_aus_name("Haushalt"), haushalt) # pyright: ignore[reportPrivateUsage]
        self.assertEqual(model._category_aus_name("Freizeit"), freizeit) # pyright: ignore[reportPrivateUsage]

        with self.assertRaises(ValueError):
            model._category_aus_name("invalid") # pyright: ignore[reportPrivateUsage]

    def test_filter_todos_no_filter(self):
        model = ToDoListModel()
        result = model.filter_todos("alle", "alle", "alle")
        self.assertEqual(len(result), 16)
        self.assertEqual(result, model.dummydaten)

    def test_filter_todos_by_category(self):
        model = ToDoListModel()
        # Filter by Studium
        result = model.filter_todos("Studium", "alle", "alle")
        self.assertTrue(all(todo.category == studium for todo in result))
        self.assertEqual(len(result), 5)  # IDs: 1, 3, 7, 12, 16

        # Filter by Haushalt
        result = model.filter_todos("Haushalt", "alle", "alle")
        self.assertTrue(all(todo.category == haushalt for todo in result))
        self.assertEqual(len(result), 5)  # IDs: 4, 6, 8, 13, 14

        # Filter by Freizeit
        result = model.filter_todos("Freizeit", "alle", "alle")
        self.assertTrue(all(todo.category == freizeit for todo in result))
        self.assertEqual(len(result), 6)  # IDs: 2, 5, 9, 10, 11, 15

    def test_filter_todos_by_priority(self):
        model = ToDoListModel()
        # Filter by hoch
        result = model.filter_todos("alle", "hoch", "alle")
        self.assertTrue(all(todo.priority == hoch for todo in result))
        self.assertEqual(len(result), 4)  # IDs: 1, 5, 7, 12

        # Filter by mittel
        result = model.filter_todos("alle", "mittel", "alle")
        self.assertTrue(all(todo.priority == mittel for todo in result))
        self.assertEqual(len(result), 5)  # IDs: 3, 4, 9, 11, 14, 16

    def test_filter_todos_by_status(self):
        model = ToDoListModel()
        # Initially all todos are not completed
        result_open = model.filter_todos("alle", "alle", "offen")
        self.assertEqual(len(result_open), 16)
        self.assertTrue(all(not todo.erledigt for todo in result_open))

        result_done = model.filter_todos("alle", "alle", "erledigt")
        self.assertEqual(len(result_done), 0)

        # Mark one todo as completed and test again
        model.dummydaten[0]._erledigt = True # pyright: ignore[reportPrivateUsage]
        result_open = model.filter_todos("alle", "alle", "offen")
        self.assertEqual(len(result_open), 15)
        result_done = model.filter_todos("alle", "alle", "erledigt")
        self.assertEqual(len(result_done), 1)
        self.assertEqual(result_done[0].id, 1)

    def test_filter_todos_combined(self):
        model = ToDoListModel()
        # Filter by category=Studium and priority=hoch
        result = model.filter_todos("Studium", "hoch", "alle")
        self.assertTrue(all(todo.category == studium and todo.priority == hoch for todo in result))
        self.assertEqual(len(result), 3)  # IDs: 1, 7, 12

        # Filter by category=Haushalt and priority=mittel
        result = model.filter_todos("Haushalt", "mittel", "alle")
        self.assertTrue(all(todo.category == haushalt and todo.priority == mittel for todo in result))
        self.assertEqual(len(result), 2)  # IDs: 4, 14

    def test_filter_todos_empty_result(self):
        model = ToDoListModel()
        result = model.filter_todos("Studium", "keine", "alle")
        self.assertEqual(len(result), 0)

    def test_filter_with_controlled_mock_data(self):
        model = ToDoListModel()
        # Clear existing data and add controlled mock todos
        model.dummydaten.clear()

        mock_todo1 = Mock(spec=ToDoModel)
        mock_todo1.category = studium
        mock_todo1.priority = hoch
        mock_todo1.erledigt = False
        mock_todo1.id = 1

        mock_todo2 = Mock(spec=ToDoModel)
        mock_todo2.category = haushalt
        mock_todo2.priority = mittel
        mock_todo2.erledigt = True
        mock_todo2.id = 2

        mock_todo3 = Mock(spec=ToDoModel)
        mock_todo3.category = studium
        mock_todo3.priority = hoch
        mock_todo3.erledigt = False
        mock_todo3.id = 3

        model.dummydaten.extend([mock_todo1, mock_todo2, mock_todo3])

        # Test category filter
        result = model.filter_todos("Studium", "alle", "alle")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(t.category == studium for t in result))

        # Test priority filter
        result = model.filter_todos("alle", "hoch", "alle")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(t.priority == hoch for t in result))

        # Test status filter
        result = model.filter_todos("alle", "alle", "offen")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(not t.erledigt for t in result))

        result = model.filter_todos("alle", "alle", "erledigt")
        self.assertEqual(len(result), 1)
        self.assertTrue(all(t.erledigt for t in result))

        # Test combined filters
        result = model.filter_todos("Studium", "hoch", "offen")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(t.category == studium and t.priority == hoch and not t.erledigt for t in result))