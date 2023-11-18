import unittest

from mermaid.sequence import Actor, Participant


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
