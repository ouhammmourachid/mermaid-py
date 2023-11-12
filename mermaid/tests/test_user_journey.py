import unittest
from unittest.mock import MagicMock

from mermaid.userjourney import Actor, Section, Task


class TestTask(unittest.TestCase):
    def test_str_task_with_one_actor(self):
        actors = Actor('Me')
        task = Task('Make tea', 5, actors)
        expect_string = '\t\tMake tea: 5 : Me'
        self.assertEqual(expect_string, str(task))

    def test_str_task_with_actors(self):
        actors = [Actor('Me'), Actor('Cat')]
        task = Task('Make tea', 5, actors)
        expect_string = '\t\tMake tea: 5 : Me, Cat'
        self.assertEqual(expect_string, str(task))


class TestSection(unittest.TestCase):
    def test_string_section(self):
        task_mock_1 = MagicMock(spec=Task)
        task_mock_2 = MagicMock(spec=Task)
        task_mock_1.__str__.return_value = '\t\tMake tea1: 5 : Me, Cat'
        task_mock_2.__str__.return_value = '\t\tMake tea2: 5 : Me, Cat'
        section = Section('My working day', [task_mock_1, task_mock_2])
        expect_string = """\tsection My working day
\t\tMake tea1: 5 : Me, Cat
\t\tMake tea2: 5 : Me, Cat
"""
        self.assertEqual(expect_string, str(section))
