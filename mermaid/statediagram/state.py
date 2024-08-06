"""State module.

This module contains the classes to represent the states in a state diagram.
"""

from typing import Optional, Union

from mermaid import Direction, text_to_snake_case
from mermaid.style import Style

from .base import BaseTransition


class State:
    """State class.

    This class represents a state in a state diagram.

    Attributes:
        id_ (str): The id of the state.
        content (str): The content of the state.
        styles (list[Style]): The styles of the state.
    """

    def __init__(
        self, id_: str, content: str = "", styles: Optional[list[Style]] = None
    ) -> None:
        """Initialize a new State.

        Args:
            id_ (str): The id of the state.
            content (str): The content of the state.
            styles (Optional[list[Style]]): The styles of the state.
        """
        self.id_: str = text_to_snake_case(id_)
        self.content: str = content if content else id_
        self.styles: list[Style] = styles if styles is not None else []

    def __str__(self) -> str:
        """Return the string representation of the state."""
        string: str = f"{self.id_} : {self.content}"
        for style in self.styles:
            string += f"\n{self.id_}:::{style.name}"
        return string


class Start(State):
    """Start class.

    This class represents the start state in a state diagram.
    """

    def __init__(self) -> None:
        super().__init__(id_="[*]")
        self.id_: str = "[*]"

    def __str__(self) -> str:
        return f"{self.id_}"


class End(State):
    """End class.

    This class represents the end state in a state diagram.
    """

    def __init__(self) -> None:
        super().__init__(id_="[*]")
        self.id_: str = "[*]"

    def __str__(self) -> str:
        return f"{self.id_}"


class Composite(State):
    """Composite class.

    This class represents a composite state in a state diagram.

    Attributes:
        sub_states (list[State]): The sub states of the composite state.
        transitions (list[BaseTransition]): The transitions of the composite state.
        direction (Union[str,Direction]): The direction of the composite state.
        styles (list[Style]): The styles of the composite state.
    """

    def __init__(
        self,
        id_: str,
        content: str = "",
        sub_states: Optional[list[State]] = None,
        transitions: Optional[list[BaseTransition]] = None,
        direction: Optional[Union[str, Direction]] = None,
        styles: Optional[list[Style]] = None,
    ) -> None:
        """Initialize a new Composite.

        Args:
            id_ (str): The id of the state.
            content (str): The content of the state.
            sub_states (Optional[list[State]]): The sub states of the composite state.
            transitions (Optional[list[BaseTransition]]): The transitions of the composite state.
            styles (Optional[list[Style]]): The styles of the composite state.
        """
        super().__init__(id_, content, styles)
        self.sub_states: list[State] = sub_states if sub_states is not None else []
        self.transitions: list[BaseTransition] = (
            transitions if transitions is not None else []
        )
        self.direction: Optional[str] = (
            direction.value if isinstance(direction, Direction) else direction
        )

    def __str__(self) -> str:
        """Return the string representation of the state."""
        string: str = super().__str__()

        if len(self.sub_states):
            string += f"\nstate {self.id_} {{"
            if self.direction:
                string += f"\n\tdirection {self.direction}"
            for state in self.sub_states:
                string += f"\n\t{str(state)}"

            for transition in self.transitions:
                string += f"\n\t{str(transition)}"

            string += "\n}"

        return string


class Concurrent(Composite):
    """Concurrent class.

    This class represents a concurrent state in a state diagram.

    Attributes:
        groups (list[tuple[list[State],list[BaseTransition]]]): The groups of the concurrent state.
        styles (list[Style]): The styles of the concurrent state.
    """

    def __init__(
        self,
        id_: str,
        content: str = "",
        sub_groups: Optional[list[tuple[list[State], list[BaseTransition]]]] = None,
        styles: Optional[list[Style]] = None,
    ) -> None:
        """Initialize a new Concurrent.

        Args:
            id_ (str): The id of the state.
            content (str): The content of the state.
            sub_groups (Optional[list[tuple[list[State],list[BaseTransition]]]): The groups of the concurrent state.
            styles (Optional[list[Style]]): The styles of the concurrent state.
        """
        super().__init__(id_, content, styles=styles)
        self.groups: list[tuple[list[State], list[BaseTransition]]] = (
            sub_groups if sub_groups is not None else []
        )

    def __str__(self) -> str:
        """Return the string representation of the state."""
        string: str = super().__str__()
        if len(self.groups):
            string += f"\nstate {self.id_} {{"
            for states, transitions in self.groups:
                for state in states:
                    string += f"\n\t{str(state)}"
                for transition in transitions:
                    string += f"\n\t{str(transition)}"
                string += "\n\t--"
            string = string[:-4]
            string += "\n}"
        return string
