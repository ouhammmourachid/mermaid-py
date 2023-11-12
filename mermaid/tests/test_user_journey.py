import unittest

from mermaid.userjourney import Actor, Task


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
