"""
StateDiagram class.

This module contains the StateDiagram class.
"""

from typing import Optional, Union

from mermaid import Direction
from mermaid.configuration import Config
from mermaid.graph import Graph
from mermaid.style import Style

from .base import BaseTransition
from .state import Composite, Concurrent, End, Start, State
from .transition import Choice, Fork, Join, Transition


class StateDiagram(Graph):
    """stateDiagram class.

    Args:
        title (str): Title of the stateDiagram.
        states (list[State]): List of states.
        transitions (list[BaseTransition]): List of transitions.
        version (str, optional): Version of the stateDiagram. Defaults to 'v2'.
        direction (Optional[Union[str,Direction]], optional): Direction of the stateDiagram. Defaults to None.
        config (Optional[Config], optional): Configuration for the stateDiagram. Defaults to None.
    """

    def __init__(
        self,
        title: str,
        states: Optional[list[State]] = None,
        transitions: Optional[list[BaseTransition]] = None,
        version: str = "v2",
        direction: Optional[Union[str, Direction]] = None,
        config: Optional[Config] = None,
    ) -> None:
        """stateDiagram class.

        Args:
            title (str): Title of the stateDiagram.
            states (list[State]): List of states.
            transitions (list[BaseTransition]): List of transitions.
            version (str, optional): Version of the stateDiagram. Defaults to 'v2'.
            direction (Optional[Union[str,Direction]], optional): Direction of the stateDiagram. Defaults to None.
            config (Optional[Config], optional): Configuration for the stateDiagram. Defaults to None.
        """
        super().__init__(title, "", config)
        self.states: list[State] = states if states is not None else []
        self.transitions: list[BaseTransition] = (
            transitions if transitions is not None else []
        )
        self.version: str = version
        self.styles: set[Style] = set()
        for state in self.states:
            self.styles.update(state.styles)

        self.direction: Optional[str] = None

        if direction:
            self.direction = (
                direction if isinstance(direction, str) else direction.value
            )

        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        str_version: str = f"-{self.version}" if self.version != "v1" else ""
        script: str = f"\nstateDiagram{str_version}"
        if self.direction:
            script += f"\n\tdirection {self.direction}"
        for style in self.styles:
            script += f"\n\t{style}"
        for state in self.states:
            script += f"\n\t{state}"
        for transition in self.transitions:
            script += f"\n\t{transition}"

        self.script += script + "\n"


__all__ = [
    "StateDiagram",
    "State",
    "Composite",
    "Concurrent",
    "Start",
    "End",
    "Transition",
    "Choice",
    "Fork",
    "Join",
]
