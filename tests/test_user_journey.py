import unittest
from unittest.mock import MagicMock

from mermaid.configuration import Config, Themes
from mermaid.userjourney import Actor, Section, Task, UserJourney


class TestTask(unittest.TestCase):
    def test_str_task_with_one_actor(self):
        actors = Actor("Me")
        task = Task("Make tea", 5, actors)
        expect_string = "\t\tMake tea: 5 : Me"
        self.assertEqual(expect_string, str(task))

    def test_str_task_with_actors(self):
        actors = [Actor("Me"), Actor("Cat")]
        task = Task("Make tea", 5, actors)
        expect_string = "\t\tMake tea: 5 : Me, Cat"
        self.assertEqual(expect_string, str(task))


class TestSection(unittest.TestCase):
    def test_string_section(self):
        task_mock_1 = MagicMock(spec=Task)
        task_mock_2 = MagicMock(spec=Task)
        task_mock_1.__str__.return_value = "\t\tMake tea1: 5 : Me, Cat"
        task_mock_2.__str__.return_value = "\t\tMake tea2: 5 : Me, Cat"
        section = Section("My working day", [task_mock_1, task_mock_2])
        expect_string = """\tsection My working day
\t\tMake tea1: 5 : Me, Cat
\t\tMake tea2: 5 : Me, Cat
"""
        self.assertEqual(expect_string, str(section))


class TestUserJourney(unittest.TestCase):
    def test_script_with_task(self):
        task_mock_1 = MagicMock(spec=Task)
        task_mock_2 = MagicMock(spec=Task)
        task_mock_1.__str__.return_value = "\tMake tea1: 5 : Me, Cat"
        task_mock_2.__str__.return_value = "\tMake tea2: 5 : Me, Cat"
        userjourney = UserJourney("simple user journey", [task_mock_1, task_mock_2])
        expect_string = """---
title: simple user journey
---
journey
\ttitle simple user journey
\tMake tea1: 5 : Me, Cat
\tMake tea2: 5 : Me, Cat
"""
        self.assertEqual(expect_string, userjourney.script)

    def test_script_with_section(self):
        section_mock_1 = MagicMock(spec=Section)
        section_mock_2 = MagicMock(spec=Section)
        section_mock_1.__str__.return_value = """\tsection section-1
\t\tMake tea1: 5 : Me, Cat
\t\tMake tea2: 5 : Me, Cat
"""
        section_mock_2.__str__.return_value = """\tsection section-2
\t\tMake tea1: 5 : Me, Cat
\t\tMake tea2: 5 : Me, Cat
"""
        userjourney = UserJourney(
            "simple user journey", [section_mock_1, section_mock_2]
        )
        expect_string = """---
title: simple user journey
---
journey
\ttitle simple user journey
\tsection section-1
\t\tMake tea1: 5 : Me, Cat
\t\tMake tea2: 5 : Me, Cat

\tsection section-2
\t\tMake tea1: 5 : Me, Cat
\t\tMake tea2: 5 : Me, Cat

"""
        self.assertEqual(expect_string, userjourney.script)

    def test_script_wth_config(self):
        config_mock = Config(theme=Themes.FOREST)
        userjourney = UserJourney("simple user journey", [], config_mock)
        expect_string = """---
title: simple user journey
---
%%{
\tinit: {
\t\t"theme": "forest",
\t\t"themeVariables": {
\t\t}
\t}
}%%

journey
\ttitle simple user journey
"""
        self.assertEqual(expect_string, userjourney.script)
