import unittest

from mermaid import Config, Direction
from mermaid.statediagram import (
    Choice,
    Composite,
    Concurrent,
    End,
    Fork,
    Join,
    Start,
    State,
    StateDiagram,
    Transition,
)
from mermaid.style import Style


class TestState(unittest.TestCase):
    def test_simple_state(self):
        state: State = State("My State")
        expect_string: str = "my_state : My State"
        self.assertEqual(expect_string, str(state))

    def test_state_with_content(self):
        state: State = State("My State", "This is my content")
        expect_string: str = "my_state : This is my content"
        self.assertEqual(expect_string, str(state))

    def test_start_state(self):
        start: Start = Start()
        expect_string: str = "[*]"
        self.assertEqual(expect_string, str(start))

    def test_end_state(self):
        end: End = End()
        expect_string: str = "[*]"
        self.assertEqual(expect_string, str(end))

    def test_composite_state(self):
        composite: Composite = Composite("Main State", "This is my content")
        expect_string: str = "main_state : This is my content"
        self.assertEqual(expect_string, str(composite))

    def test_concurrent_state_with_style(self):
        styles = [Style(name="style1", fill="red"), Style(name="style2", color="blue")]
        state: State = State("My State", styles=styles)
        expect_string: str = "my_state : My State\nmy_state:::style1\nmy_state:::style2"
        self.assertEqual(expect_string, str(state))


class TestComposite(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State("First State")
        self.state_2: State = State("Second State")
        self.transition_1: Transition = Transition(
            self.state_1, self.state_2, "This is my label"
        )
        self.transition_2: Transition = Transition(to=self.state_1)
        return super().setUp()

    def test_simple_composite_without_content(self):
        composite: Composite = Composite("Main State")
        expect_string: str = "main_state : Main State"
        self.assertEqual(expect_string, str(composite))

    def test_simple_composite_with_content(self):
        composite: Composite = Composite("Main State", "This is my content")
        expect_string: str = "main_state : This is my content"
        self.assertEqual(expect_string, str(composite))

    def test_state_with_sub_states(self):
        composite: Composite = Composite(
            "Main State",
            sub_states=[self.state_1, self.state_2],
            direction=Direction.LEFT_TO_RIGHT,
        )
        expect_string: str = """main_state : Main State
state main_state {
\tdirection LR
\tfirst_state : First State
\tsecond_state : Second State
}"""
        self.assertEqual(expect_string, str(composite))

    def test_state_with_sub_states_and_str_direction(self):
        composite: Composite = Composite(
            "Main State", sub_states=[self.state_1, self.state_2], direction="LR"
        )
        expect_string: str = """main_state : Main State
state main_state {
\tdirection LR
\tfirst_state : First State
\tsecond_state : Second State
}"""
        self.assertEqual(expect_string, str(composite))

    def test_composite_with_sub_states_and_transitions(self):
        composite: Composite = Composite(
            "Main State",
            sub_states=[self.state_1, self.state_2],
            transitions=[self.transition_1, self.transition_2],
        )
        expect_string: str = """main_state : Main State
state main_state {
\tfirst_state : First State
\tsecond_state : Second State
\tfirst_state --> second_state : This is my label
\t[*] --> first_state
}"""
        self.assertEqual(expect_string, str(composite))

    def test_composite_with_sub_states_and_styles(self):
        styles = [
            Style(name="style1", fill="red", font_weight="bold"),
            Style(name="style2", color="blue"),
        ]
        composite: Composite = Composite(
            "Main State", sub_states=[self.state_1, self.state_2], styles=styles
        )
        expect_string: str = """main_state : Main State
main_state:::style1
main_state:::style2
state main_state {
\tfirst_state : First State
\tsecond_state : Second State
}"""
        self.assertEqual(expect_string, str(composite))


class TestConcurrent(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State("First State")
        self.state_2: State = State("Second State")
        self.state_3: State = State("Third State")
        self.transition_1: Transition = Transition(self.state_1, self.state_2)
        self.transition_2: Transition = Transition(to=self.state_1)
        return super().setUp()

    def test_simple_concurrent_without_content(self):
        concurrent: Concurrent = Concurrent("Main State")
        expect_string: str = "main_state : Main State"
        self.assertEqual(expect_string, str(concurrent))

    def test_simple_concurrent_with_content(self):
        concurrent: Concurrent = Concurrent("Main State", "This is my content")
        expect_string: str = "main_state : This is my content"
        self.assertEqual(expect_string, str(concurrent))

    def test_concurrent_with_sub_goups(self):
        groups = [
            ([self.state_1, self.state_2], [self.transition_1, self.transition_2]),
            ([self.state_1], [self.transition_2]),
        ]
        concurrent: Concurrent = Concurrent("Main State", sub_groups=groups)

        expect_string: str = """main_state : Main State
state main_state {
\tfirst_state : First State
\tsecond_state : Second State
\tfirst_state --> second_state
\t[*] --> first_state
\t--
\tfirst_state : First State
\t[*] --> first_state
}"""
        self.assertEqual(expect_string, str(concurrent))

    def test_concurrent_with_sub_goups_and_styles(self):
        styles = [
            Style(name="style1", fill="red", font_weight="bold"),
            Style(name="style2", color="blue"),
        ]
        groups = [
            ([self.state_1, self.state_2], [self.transition_1, self.transition_2]),
            ([self.state_1], [self.transition_2]),
        ]
        concurrent: Concurrent = Concurrent(
            "Main State", sub_groups=groups, styles=styles
        )

        expect_string: str = """main_state : Main State
main_state:::style1
main_state:::style2
state main_state {
\tfirst_state : First State
\tsecond_state : Second State
\tfirst_state --> second_state
\t[*] --> first_state
\t--
\tfirst_state : First State
\t[*] --> first_state
}"""

        self.assertEqual(expect_string, str(concurrent))


class TestTransition(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State("First State")
        self.state_2: State = State("Second State")
        return super().setUp()

    def test_simple_transition(self):
        transition: Transition = Transition(
            self.state_1, self.state_2, "This is my label"
        )
        expect_string: str = "first_state --> second_state : This is my label"
        self.assertEqual(expect_string, str(transition))

    def test_transition_from_start_to_state(self):
        transition: Transition = Transition(to=self.state_1)
        expect_string: str = "[*] --> first_state"
        self.assertEqual(expect_string, str(transition))

    def test_transition_from_state_to_end(self):
        transition: Transition = Transition(from_=self.state_1)
        expect_string: str = "first_state --> [*]"
        self.assertEqual(expect_string, str(transition))


class TestChoice(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State("First State")
        self.state_2: State = State("Second State")
        self.state_3: State = State("Third State")
        return super().setUp()

    def test_withot_to_and_from_state(self):
        choice: Choice = Choice("My Choice")
        expect_string: str = "state my_choice <<choice>>"
        self.assertEqual(expect_string, str(choice))

    def test_without_to_and_with_from_state(self):
        choice: Choice = Choice("My Choice", self.state_1)
        expect_string: str = "state my_choice <<choice>>\nfirst_state --> my_choice"
        self.assertEqual(expect_string, str(choice))

    def test_with_to_and_without_from_state(self):
        choice: Choice = Choice("My Choice", to=[self.state_1, self.state_2])
        expect_string: str = """state my_choice <<choice>>
my_choice --> first_state
my_choice --> second_state"""
        self.assertEqual(expect_string, str(choice))

    def test_with_to_and_from_state(self):
        choice: Choice = Choice("My Choice", self.state_1, [self.state_2, self.state_3])
        expect_string: str = """state my_choice <<choice>>
first_state --> my_choice
my_choice --> second_state
my_choice --> third_state"""
        self.assertEqual(expect_string, str(choice))

    def test_with_to_and_from_state_with_conditions(self):
        choice: Choice = Choice(
            "My Choice",
            self.state_1,
            [self.state_2, self.state_3],
            ["condition 1", "condition 2"],
        )
        expect_string: str = """state my_choice <<choice>>
first_state --> my_choice
my_choice --> second_state : condition 1
my_choice --> third_state : condition 2"""
        self.assertEqual(expect_string, str(choice))


class TestFork(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State("First State")
        self.state_2: State = State("Second State")
        self.state_3: State = State("Third State")
        return super().setUp()

    def test_without_to_and_from_state(self):
        fork: Fork = Fork("My Fork")
        expect_string: str = "state my_fork <<fork>>"
        self.assertEqual(expect_string, str(fork))

    def test_without_to_and_with_from_state(self):
        fork: Fork = Fork("My Fork", self.state_1)
        expect_string: str = "state my_fork <<fork>>\nfirst_state --> my_fork"
        self.assertEqual(expect_string, str(fork))

    def test_with_to_and_without_from_state(self):
        fork: Fork = Fork("My Fork", to=[self.state_1, self.state_2])
        expect_string: str = """state my_fork <<fork>>
my_fork --> first_state
my_fork --> second_state"""
        self.assertEqual(expect_string, str(fork))

    def test_with_to_and_from_state(self):
        fork: Fork = Fork("My Fork", self.state_1, [self.state_2, self.state_3])
        expect_string: str = """state my_fork <<fork>>
first_state --> my_fork
my_fork --> second_state
my_fork --> third_state"""
        self.assertEqual(expect_string, str(fork))


class TestJoin(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State("First State")
        self.state_2: State = State("Second State")
        self.state_3: State = State("Third State")
        return super().setUp()

    def test_without_to_and_from_state(self):
        join: Join = Join("My Join")
        expect_string: str = "state my_join <<join>>"
        self.assertEqual(expect_string, str(join))

    def test_without_to_and_with_from_state(self):
        join: Join = Join("My Join", [self.state_1])
        expect_string: str = "state my_join <<join>>\nfirst_state --> my_join"
        self.assertEqual(expect_string, str(join))

    def test_with_to_and_without_from_state(self):
        join: Join = Join("My Join", to=self.state_1)
        expect_string: str = """state my_join <<join>>
my_join --> first_state"""
        self.assertEqual(expect_string, str(join))

    def test_with_to_and_from_state(self):
        join: Join = Join("My Join", [self.state_1, self.state_2], self.state_3)
        expect_string: str = """state my_join <<join>>
first_state --> my_join
second_state --> my_join
my_join --> third_state"""
        self.assertEqual(expect_string, str(join))


class TestStateDiagram(unittest.TestCase):
    def setUp(self) -> None:
        self.start: Start = Start()
        self.end: End = End()
        self.state_1: State = State("First State")
        self.state_2: State = State("Second State")
        self.state_3: State = State("Third State")
        self.transition_1: Transition = Transition(
            self.state_1, self.state_2, "This is my label"
        )
        self.transition_2: Transition = Transition(to=self.state_1)
        self.choice: Choice = Choice(
            "My Choice",
            self.state_1,
            [self.state_2, self.state_3],
            ["condition 1", "condition 2"],
        )
        self.fork: Fork = Fork("My Fork", self.state_1, [self.state_2, self.state_3])
        self.join: Join = Join("My Join", [self.state_1, self.state_2], self.state_3)
        self.composite: Composite = Composite(
            "Main State",
            sub_states=[self.state_1, self.state_2],
            transitions=[self.transition_1, self.transition_2],
        )
        self.concurrent: Concurrent = Concurrent(
            "Main State",
            sub_groups=[
                ([self.state_1, self.state_2], [self.transition_1, self.transition_2]),
                ([self.state_1], [self.transition_2]),
            ],
        )

        return super().setUp()

    def test_state_diagram_version(self):
        list_verions = [
            StateDiagram("My State Diagram", [], [], "v1"),
            StateDiagram("My State Diagram", [], [], "v2"),
        ]
        list_expect = ["stateDiagram", "stateDiagram-v2"]

        def get_expected_script(version):
            return f"""---
title: My State Diagram
---
{version}
"""

        for i, version in enumerate(list_verions):
            expect_string = get_expected_script(list_expect[i])
            self.assertEqual(expect_string, version.script)

    def test_state_diagram_with_states(self):
        state_diagram: StateDiagram = StateDiagram(
            "My State Diagram", [self.state_1, self.state_2], []
        )
        expect_string: str = f"""---
title: My State Diagram
---
stateDiagram-v2
\t{self.state_1}
\t{self.state_2}
"""
        self.assertEqual(expect_string, state_diagram.script)

    def test_state_diagram_with_transitions(self):
        state_diagram: StateDiagram = StateDiagram(
            "My State Diagram",
            [self.state_1, self.state_2],
            [self.transition_1, self.transition_2],
        )
        expect_string: str = f"""---
title: My State Diagram
---
stateDiagram-v2
\t{self.state_1}
\t{self.state_2}
\t{self.transition_1}
\t{self.transition_2}
"""
        self.assertEqual(expect_string, state_diagram.script)

    def test_state_diagram_with_composite(self):
        state_diagram: StateDiagram = StateDiagram("My State Diagram", [self.composite])
        expect_string: str = f"""---
title: My State Diagram
---
stateDiagram-v2
\t{self.composite}
"""
        self.assertEqual(expect_string, state_diagram.script)

    def test_state_diagram_with_concurrent(self):
        transition = Transition(from_=self.concurrent, label="This is my label")
        state_diagram: StateDiagram = StateDiagram(
            "My State Diagram", [self.concurrent], [transition]
        )
        expect_string: str = f"""---
title: My State Diagram
---
stateDiagram-v2
\t{self.concurrent}
\t{transition}
"""
        self.assertEqual(expect_string, state_diagram.script)

    def test_state_diagram_with_styles(self):
        styles = [
            Style(name="style1", fill="red", font_weight="bold"),
            Style(name="style2", color="blue"),
        ]

        states = [
            State("First State", styles=[styles[0]]),
            State("Second State", styles=[styles[1]]),
        ]
        styles = list(set(styles))
        state_diagram: StateDiagram = StateDiagram("My State Diagram", states)
        expect_string: str = f"""---
title: My State Diagram
---
stateDiagram-v2
\t{styles[0]}
\t{styles[1]}
\t{states[0]}
\t{states[1]}
"""
        self.assertEqual(expect_string, state_diagram.script)

    def test_state_diagram_with_duplicate_styles(self):
        styles = [
            Style(name="style1", fill="red", font_weight="bold"),
            Style(name="style1", fill="red", font_weight="bold"),
        ]

        states = [
            State("First State", styles=[styles[0]]),
            State("Second State", styles=[styles[1]]),
        ]
        styles = list(set(styles))
        state_diagram: StateDiagram = StateDiagram("My State Diagram", states)
        expect_string: str = f"""---
title: My State Diagram
---
stateDiagram-v2
\t{styles[0]}
\t{states[0]}
\t{states[1]}
"""
        self.assertEqual(expect_string, state_diagram.script)

    def test_state_diagram_with_direction(self):
        state_diagram: StateDiagram = StateDiagram(
            "My State Diagram",
            [self.state_1, self.state_2],
            direction=Direction.LEFT_TO_RIGHT,
        )
        expect_string: str = f"""---
title: My State Diagram
---
stateDiagram-v2
\tdirection LR
\t{self.state_1}
\t{self.state_2}
"""
        self.assertEqual(expect_string, state_diagram.script)

    def test_state_diagram_with_config(self):
        config = Config(primary_color="red")
        state_diagram: StateDiagram = StateDiagram(
            "My State Diagram", [self.state_1, self.state_2], config=config
        )
        sub_string = """---
title: My State Diagram
---
%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t\t"primaryColor": "red"
\t\t}
\t}
}%%
"""
        except_str = f"""{sub_string}
stateDiagram-v2
\t{self.state_1}
\t{self.state_2}
"""
        self.assertEqual(except_str, state_diagram.script)
