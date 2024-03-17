import unittest

from mermaid.statediagram import *


class TestState(unittest.TestCase):
    def test_simple_state(self):
        state: State = State('My State')
        expect_string: str = 'my_state : My State'
        self.assertEqual(expect_string, str(state))

    def test_state_with_content(self):
        state: State = State('My State', 'This is my content')
        expect_string: str = 'my_state : This is my content'
        self.assertEqual(expect_string, str(state))

    def test_start_state(self):
        start: Start = Start()
        expect_string: str = '[*]'
        self.assertEqual(expect_string, str(start))

    def test_end_state(self):
        end: End = End()
        expect_string: str = '[*]'
        self.assertEqual(expect_string, str(end))

    def test_composite_state(self):
        composite: Composite = Composite('Main State', 'This is my content')
        expect_string: str = 'main_state : This is my content'
        self.assertEqual(expect_string, str(composite))


class TestComposite(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State('First State')
        self.state_2: State = State('Second State')
        self.transition_1: Transition = Transition(self.state_1, self.state_2,
                                                   'This is my label')
        self.transition_2: Transition = Transition(to=self.state_1)
        return super().setUp()

    def test_simple_composite_without_content(self):
        composite: Composite = Composite('Main State')
        expect_string: str = 'main_state : Main State'
        self.assertEqual(expect_string, str(composite))

    def test_simple_composite_with_content(self):
        composite: Composite = Composite('Main State', 'This is my content')
        expect_string: str = 'main_state : This is my content'
        self.assertEqual(expect_string, str(composite))

    def test_state_with_sub_states(self):
        composite: Composite = Composite(
            'Main State', sub_states=[self.state_1, self.state_2])
        expect_string: str = """main_state : Main State
state main_state {
\tfirst_state : First State
\tsecond_state : Second State
}"""
        self.assertEqual(expect_string, str(composite))

    def test_composite_with_sub_states_and_transitions(self):
        composite: Composite = Composite(
            'Main State',
            sub_states=[self.state_1, self.state_2],
            transitions=[self.transition_1, self.transition_2])
        expect_string: str = """main_state : Main State
state main_state {
\tfirst_state : First State
\tsecond_state : Second State
\tfirst_state --> second_state : This is my label
\t[*] --> first_state
}"""
        self.assertEqual(expect_string, str(composite))


class TestTransition(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State('First State')
        self.state_2: State = State('Second State')
        return super().setUp()

    def test_simple_transition(self):
        transition: Transition = Transition(self.state_1, self.state_2,
                                            'This is my label')
        expect_string: str = 'first_state --> second_state : This is my label'
        self.assertEqual(expect_string, str(transition))

    def test_transition_from_start_to_state(self):
        transition: Transition = Transition(to=self.state_1)
        expect_string: str = '[*] --> first_state'
        self.assertEqual(expect_string, str(transition))

    def test_transition_from_state_to_end(self):
        transition: Transition = Transition(from_=self.state_1)
        expect_string: str = 'first_state --> [*]'
        self.assertEqual(expect_string, str(transition))


class TestChoice(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State('First State')
        self.state_2: State = State('Second State')
        self.state_3: State = State('Third State')
        return super().setUp()

    def test_withot_to_and_from_state(self):
        choice: Choice = Choice('My Choice')
        expect_string: str = 'state my_choice <<choice>>'
        self.assertEqual(expect_string, str(choice))

    def test_without_to_and_with_from_state(self):
        choice: Choice = Choice('My Choice', self.state_1)
        expect_string: str = 'state my_choice <<choice>>\nfirst_state --> my_choice'
        self.assertEqual(expect_string, str(choice))

    def test_with_to_and_without_from_state(self):
        choice: Choice = Choice('My Choice', to=[self.state_1, self.state_2])
        expect_string: str = """state my_choice <<choice>>
my_choice --> first_state
my_choice --> second_state"""
        self.assertEqual(expect_string, str(choice))

    def test_with_to_and_from_state(self):
        choice: Choice = Choice('My Choice', self.state_1,
                                [self.state_2, self.state_3])
        expect_string: str = """state my_choice <<choice>>
first_state --> my_choice
my_choice --> second_state
my_choice --> third_state"""
        self.assertEqual(expect_string, str(choice))

    def test_with_to_and_from_state_with_conditions(self):
        choice: Choice = Choice('My Choice', self.state_1,
                                [self.state_2, self.state_3],
                                ['condition 1', 'condition 2'])
        expect_string: str = """state my_choice <<choice>>
first_state --> my_choice
my_choice --> second_state : condition 1
my_choice --> third_state : condition 2"""
        self.assertEqual(expect_string, str(choice))


class TestFork(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State('First State')
        self.state_2: State = State('Second State')
        self.state_3: State = State('Third State')
        return super().setUp()

    def test_without_to_and_from_state(self):
        fork: Fork = Fork('My Fork')
        expect_string: str = 'state my_fork <<fork>>'
        self.assertEqual(expect_string, str(fork))

    def test_without_to_and_with_from_state(self):
        fork: Fork = Fork('My Fork', self.state_1)
        expect_string: str = 'state my_fork <<fork>>\nfirst_state --> my_fork'
        self.assertEqual(expect_string, str(fork))

    def test_with_to_and_without_from_state(self):
        fork: Fork = Fork('My Fork', to=[self.state_1, self.state_2])
        expect_string: str = """state my_fork <<fork>>
my_fork --> first_state
my_fork --> second_state"""
        self.assertEqual(expect_string, str(fork))

    def test_with_to_and_from_state(self):
        fork: Fork = Fork('My Fork', self.state_1,
                          [self.state_2, self.state_3])
        expect_string: str = """state my_fork <<fork>>
first_state --> my_fork
my_fork --> second_state
my_fork --> third_state"""
        self.assertEqual(expect_string, str(fork))


class TestJoin(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State('First State')
        self.state_2: State = State('Second State')
        self.state_3: State = State('Third State')
        return super().setUp()

    def test_without_to_and_from_state(self):
        join: Join = Join('My Join')
        expect_string: str = 'state my_join <<join>>'
        self.assertEqual(expect_string, str(join))

    def test_without_to_and_with_from_state(self):
        join: Join = Join('My Join', [self.state_1])
        expect_string: str = 'state my_join <<join>>\nfirst_state --> my_join'
        self.assertEqual(expect_string, str(join))

    def test_with_to_and_without_from_state(self):
        join: Join = Join('My Join', to=self.state_1)
        expect_string: str = """state my_join <<join>>
my_join --> first_state"""
        self.assertEqual(expect_string, str(join))

    def test_with_to_and_from_state(self):
        join: Join = Join('My Join', [self.state_1, self.state_2],
                          self.state_3)
        expect_string: str = """state my_join <<join>>
first_state --> my_join
second_state --> my_join
my_join --> third_state"""
        self.assertEqual(expect_string, str(join))
