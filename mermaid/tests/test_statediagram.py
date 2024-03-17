import unittest

from mermaid.statediagram import State, Start, End, Transition


class TestState(unittest.TestCase):
    
    def test_simple_state_without_content(self):
        state: State = State('First State')
        expect_string: str = 'first_state : First State'
        self.assertEqual(expect_string, str(state))
    
    def test_simple_state_with_content(self):
        state: State = State('First', 'This is my content')
        expect_string: str = 'first : This is my content'
        self.assertEqual(expect_string, str(state))
    
    def test_state_with_sub_states(self):
        state_1: State = State('First State')
        state_2: State = State('Second State')
        state: State = State('Main State', sub_states=[state_1, state_2])
        expect_string: str = """main_state : Main State
state main_state {
\tfirst_state : First State
\tsecond_state : Second State
}"""
        self.assertEqual(expect_string, str(state))
    
    def test_start_state(self):
        start: Start = Start()
        expect_string: str = '[*]'
        self.assertEqual(expect_string, str(start))
    
    def test_end_state(self):
        end: End = End()
        expect_string: str = '[*]'
        self.assertEqual(expect_string, str(end))

class TestTransition(unittest.TestCase):

    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State('First State')
        self.state_2: State = State('Second State')
        return super().setUp()
    
    def test_simple_transition(self):
        transition: Transition = Transition(self.state_1, self.state_2, 'This is my label')
        expect_string: str = 'first_state --> second_state : This is my label'
        self.assertEqual(expect_string, str(transition))
    
    def test_transition_from_start_to_state(self):
        transition: Transition = Transition(to=self.state_1)
        expect_string: str = '[*] --> first_state : '
        self.assertEqual(expect_string, str(transition))

    def test_transition_from_state_to_end(self):
        transition: Transition = Transition(from_=self.state_1)
        expect_string: str = 'first_state --> [*] : '
        self.assertEqual(expect_string, str(transition))


