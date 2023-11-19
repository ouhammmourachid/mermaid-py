import unittest
from unittest import mock

from mermaid.sequence import Actor, Box, Participant


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
