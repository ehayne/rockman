from django.test import TestCase
from rockman.todo.models import Todo
from datetime import datetime

class TodoTestCase(TestCase):
    def setUp(self):
        due_date = datetime.now()
        Todo.objects.create(task="Make test.", category="House", assignee="Emily", due=due_date)

    def test_return_tasks(self):
        """Play test case for place holding to get testing up and running"""
        todo_task = Todo.objects.get(assignee="Emily")
        self.assertEqual(todo_task.task, 'Make test.')
