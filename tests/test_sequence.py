import unittest
from unittest import mock

from mermaid.configuration import Config
from mermaid.sequence import SequenceDiagram
from mermaid.sequence.element import Actor, Box, Note, NotePosition, Participant, Rect
from mermaid.sequence.link import ArrowTypes, Link
from mermaid.sequence.logic import Alt, Break, Critical, Loop, Optional, Parallel


class TestActor(unittest.TestCase):
    def test_str(self):
        actor = Actor("John")
        expect_str = "\tactor John\n"
        self.assertEqual(str(actor), expect_str)
        self.assertEqual(actor.id_, "John")


class TestParticipant(unittest.TestCase):
    def test_str(self):
        participant = Participant("Alice")
        expect_str = "\tparticipant alice as Alice\n"
        self.assertEqual(str(participant), expect_str)


class TestBox(unittest.TestCase):
    def test_str(self):
        # use mocks to create an actor and a participant element
        actor = mock.MagicMock(spec=Actor)
        actor.__str__ = mock.Mock(return_value="\tActor John\n")
        participant = mock.MagicMock(spec=Participant)
        participant.__str__ = mock.Mock(return_value="\tparticipant alice as Alice\n")

        box = Box("Test Box", [actor, participant])
        expect_str = """\tbox Test Box
\tActor John
\tparticipant alice as Alice
\tend\n"""
        self.assertEqual(str(box), expect_str)


class TestLink(unittest.TestCase):
    def setUp(self):
        self.source = mock.MagicMock(spec=Actor)
        self.source.id_ = "John"
        self.target = mock.MagicMock(spec=Participant)
        self.target.id_ = "Alice"

    def test_str_without_activation_deactivation(self):
        link = Link(self.source, self.target, "Solid-line", "Hello World")
        expected_str = "\tJohn->Alice: Hello World\n"
        self.assertEqual(str(link), expected_str)

    def test_str_with_arrow_type_classe(self):
        link = Link(self.source, self.target, ArrowTypes.SOLID_LINE, "Hello World")
        expected_str = "\tJohn->Alice: Hello World\n"
        self.assertEqual(str(link), expected_str)

    def test_str_with_activation(self):
        link = Link(
            self.source, self.target, "Solid-line", "Hello World", activate_target=True
        )
        expected_str = "\tJohn->Alice: Hello World\nactivate Alice\n"
        self.assertEqual(str(link), expected_str)

    def test_str_with_deactivation(self):
        link = Link(
            self.source,
            self.target,
            "Solid-line",
            "Hello World",
            deactivate_target=True,
        )
        expected_str = "\tJohn->Alice: Hello World\ndeactivate Alice\n"
        self.assertEqual(str(link), expected_str)


class TestNote(unittest.TestCase):
    def setUp(self) -> None:
        self.actor = mock.Mock(spec=Actor)
        self.actor.id_ = "actor"
        self.participant = mock.Mock(spec=Participant)
        self.participant.id_ = "participant"
        self.note = "This is a note"
        return super().setUp()

    def test_note_str_single_element(self) -> None:
        note = Note(self.note, self.actor)
        self.assertEqual(str(note), "\tNote over actor: This is a note\n")

    def test_note_str_multiple_elements(self) -> None:
        note_multiple = Note(
            self.note, [self.actor, self.participant], NotePosition.OVER
        )
        self.assertEqual(
            str(note_multiple), "\tNote over actor,participant: This is a note\n"
        )

    def test_note_position(self) -> None:
        note_left = Note(self.note, self.actor, NotePosition.LEFT_OF)
        self.assertEqual(str(note_left), "\tNote left of actor: This is a note\n")
        note_right = Note(self.note, self.actor, NotePosition.RIGHT_OF)
        self.assertEqual(str(note_right), "\tNote right of actor: This is a note\n")

    def test_note_assertion(self) -> None:
        with self.assertRaises(ValueError):
            Note(self.note, [self.actor, self.participant], NotePosition.LEFT_OF)
        with self.assertRaises(ValueError):
            Note(self.note, [self.actor, self.participant], NotePosition.RIGHT_OF)


class TestLoop(unittest.TestCase):
    def test_loop_str(self) -> None:
        link = mock.MagicMock(spec=Link)
        link.configure_mock(__str__=lambda _: "\tJohn->Alice: Hello World\n")
        loop = Loop("condition", [link])
        self.assertEqual(
            str(loop), "\tloop condition\n\tJohn->Alice: Hello World\n\tend\n"
        )


class TestAlt(unittest.TestCase):
    def setUp(self):
        self.link_1 = mock.MagicMock(spec=Link)
        self.link_1.configure_mock(__str__=lambda _: "\tA-->B: message\n")
        self.link_2 = mock.MagicMock(spec=Link)
        self.link_2.configure_mock(__str__=lambda _: "\tA-->B: message\n")

    def test_str_one_condition(self):
        alt = Alt({"condition": [self.link_1]})
        excepted_str = "\talt condition\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(alt), excepted_str)

    def test_str_multiple_condition(self):
        alt = Alt({"condition-1": [self.link_1], "condition-2": [self.link_2]})
        except_str = "\talt condition-1\n\tA-->B: message\n\telse condition-2\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(alt), except_str)


class TestOptional(unittest.TestCase):
    def setUp(self):
        self.link = mock.MagicMock(spec=Link)
        self.link.configure_mock(__str__=lambda _: "\tA-->B: message\n")

    def test_str_with_one_condition(self):
        optional = Optional("condition", [self.link])
        excepted_str = "\topt condition\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(optional), excepted_str)

    def test_str_with_multiple_condition(self):
        optional = Optional("condition-1", [self.link, self.link])
        excepted_str = "\topt condition-1\n\tA-->B: message\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(optional), excepted_str)


class TestParallel(unittest.TestCase):
    def setUp(self):
        self.link = mock.MagicMock(spec=Link)
        self.link.configure_mock(__str__=lambda _: "\tA-->B: message\n")

    def test_str_with_one_condition(self):
        parallel = Parallel({"condition": [self.link]})
        excepted_str = "\tpar condition\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(parallel), excepted_str)

    def test_str_with_multiple_condition(self):
        parallel = Parallel({"condition-1": [self.link], "condition-2": [self.link]})
        excepted_str = "\tpar condition-1\n\tA-->B: message\n\tand condition-2\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(parallel), excepted_str)

    def test_str_with_multiple_condition_and_logic(self):
        loop = mock.MagicMock(spec=Loop)
        loop.configure_mock(
            __str__=lambda _: "\tloop condition\n\tA-->B: message\n\tend\n"
        )
        parallel = Parallel({"condition-1": [self.link], "condition-2": [loop]})
        excepted_str = "\tpar condition-1\n\tA-->B: message\n\tand condition-2\n\tloop "
        excepted_str += "condition\n\tA-->B: message\n\tend\n\tend\n"
        self.assertEqual(str(parallel), excepted_str)


class TestCritical(unittest.TestCase):
    def setUp(self):
        self.link = mock.MagicMock(spec=Link)
        self.link.configure_mock(__str__=lambda _: "\tA-->B: message\n")

    def test_str_with_one_condition(self):
        critical = Critical("condition-1", [self.link], {"condition-2": [self.link]})
        expected_str = "\tcritical condition-1\n\tA-->B: message\n"
        expected_str += "\toption condition-2\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(critical), expected_str)

    def test_str_with_multiple_condition(self):
        critical = Critical(
            "condition-1",
            [self.link, self.link],
            {"condition-2": [self.link], "condition-3": [self.link]},
        )
        expected_str = "\tcritical condition-1\n\tA-->B: message\n"
        expected_str += "\tA-->B: message\n"
        expected_str += "\toption condition-2\n\tA-->B: message\n"
        expected_str += "\toption condition-3\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(critical), expected_str)


class TestBreak(unittest.TestCase):
    def setUp(self) -> None:
        self.link = mock.MagicMock(spec=Link)
        self.link.configure_mock(__str__=lambda _: "\tA-->B: message\n")

    def test_str_with_one_statement(self):
        break_ = Break("condition", [self.link])
        expected_str = "\tbreak condition\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(break_), expected_str)

    def test_str_with_multiple_statements(self):
        break_ = Break("condition", [self.link, self.link])
        expected_str = "\tbreak condition\n\tA-->B: message\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(break_), expected_str)


class TestRect(unittest.TestCase):
    def setUp(self) -> None:
        self.link = mock.MagicMock(spec=Link)
        self.link.configure_mock(__str__=lambda _: "\tA-->B: message\n")

    def test_str_with_one_statement(self):
        rect = Rect([self.link], (255, 0, 0))
        expected_str = "\trect rgb(255,0,0)\n\tA-->B: message\n\tend\n"
        self.assertEqual(str(rect), expected_str)

    def test_str_with_multiple_statements(self):
        rect = Rect([self.link, self.link], (255, 0, 0))
        expected_str = (
            "\trect rgb(255,0,0)\n\tA-->B: message\n\tA-->B: message\n\tend\n"
        )
        self.assertEqual(str(rect), expected_str)

    def test_rect_assertion(self):
        with self.assertRaises(ValueError):
            Rect([self.link, self.link], (257, 3, 4, 4))
        with self.assertRaises(ValueError):
            Rect([self.link, self.link], (257, 3, -4))


class TestSequenceDiagram(unittest.TestCase):
    def setUp(self) -> None:
        self.actor_1 = mock.MagicMock(spec=Actor)
        self.actor_1.configure_mock(__str__=lambda _: "\tactor A\n")
        self.actor_2 = mock.MagicMock(spec=Actor)
        self.actor_2.configure_mock(__str__=lambda _: "\tactor B\n")
        self.link_1 = mock.MagicMock(spec=Link)
        self.link_1.configure_mock(__str__=lambda _: "\tA-->B: message\n")
        self.link_2 = mock.MagicMock(spec=Link)
        self.link_2.configure_mock(__str__=lambda _: "\tA-->B: message\n")

    def test_str_without_auto_number(self):
        diagram = SequenceDiagram(
            "Test Diagram", [self.actor_1, self.actor_2, self.link_1, self.link_2]
        )
        expected_str = """---
title: Test Diagram
---
sequenceDiagram
\tactor A
\tactor B
\tA-->B: message
\tA-->B: message
"""
        self.assertEqual(diagram.script, expected_str)

    def test_str_with_auto_number(self):
        diagram = SequenceDiagram(
            "Test Diagram",
            [self.actor_1, self.actor_2, self.link_1, self.link_2],
            auto_number=True,
        )
        expected_str = """---
title: Test Diagram
---
sequenceDiagram
\tautonumber
\tactor A
\tactor B
\tA-->B: message
\tA-->B: message
"""
        self.assertEqual(diagram.script, expected_str)

    def test_str_with_config(self):
        config = Config(primary_color="red")
        diagram = SequenceDiagram(
            "Test Diagram",
            [self.actor_1, self.actor_2, self.link_1, self.link_2],
            config=config,
        )
        expected_str = """---
title: Test Diagram
---
%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t\t"primaryColor": "red"
\t\t}
\t}
}%%

sequenceDiagram
\tactor A
\tactor B
\tA-->B: message
\tA-->B: message
"""
        self.assertEqual(diagram.script, expected_str)
