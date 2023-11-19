import unittest
from unittest import mock

from mermaid.sequence import Actor, ArrowTypes, Box, Link, Participant


class TestActor(unittest.TestCase):
    def test_str(self):
        actor = Actor('John')
        expect_str = '\tActor John\n'
        self.assertEqual(str(actor), expect_str)


class TestParticipant(unittest.TestCase):
    def test_str(self):
        participant = Participant('Alice')
        expect_str = '\tparticipant alice as Alice\n'
        self.assertEqual(str(participant), expect_str)


class TestBox(unittest.TestCase):
    def test_str(self):
        # use mocks to create an actor and a participant element
        actor = mock.MagicMock(spec=Actor)
        actor.__str__.return_value = '\tActor John\n'
        participant = mock.MagicMock(spec=Participant)
        participant.__str__.return_value = '\tparticipant alice as Alice\n'

        box = Box('Test Box', [actor, participant])
        expect_str = """\tbox Test Box
\tActor John
\tparticipant alice as Alice
\tend\n"""
        self.assertEqual(str(box), expect_str)


class TestLink(unittest.TestCase):
    def setUp(self):
        self.source = mock.MagicMock(spec=Actor)
        self.source.id_ = 'John'
        self.target = mock.MagicMock(spec=Participant)
        self.target.id_ = 'Alice'

    def test_str_without_activation_deactivation(self):
        link = Link(self.source, self.target, 'Solid-line')
        expected_str = '\tJohn->Alice\n'
        self.assertEqual(str(link), expected_str)

    def test_str_with_arrow_type_classe(self):
        link = Link(self.source, self.target, ArrowTypes.SOLID_LINE)
        expected_str = '\tJohn->Alice\n'
        self.assertEqual(str(link), expected_str)

    def test_str_with_activation(self):
        link = Link(self.source,
                    self.target,
                    'Solid-line',
                    activate_target=True)
        expected_str = '\tJohn->Alice\nactivate Alice\n'
        self.assertEqual(str(link), expected_str)

    def test_str_with_deactivation(self):
        link = Link(self.source,
                    self.target,
                    'Solid-line',
                    deactivate_target=True)
        expected_str = '\tJohn->Alice\ndeactivate Alice\n'
        self.assertEqual(str(link), expected_str)
