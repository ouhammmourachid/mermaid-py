"""
StateDiagram class.

This module contains the StateDiagram class.
"""
from typing import Optional

from mermaid.graph import Graph

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
    """
    def __init__(self,
                 title: str,
                 states: Optional[list[State]] = None,
                 transitions: Optional[list[BaseTransition]] = None,
                 version: str = 'v2') -> None:
        """stateDiagram class.

        Args:
            title (str): Title of the stateDiagram.
            states (list[State]): List of states.
            transitions (list[BaseTransition]): List of transitions.
            version (str, optional): Version of the stateDiagram. Defaults to 'v2'.
        """
        super().__init__(title, '')
        self.states: list[State] = states if states is not None else []
        self.transitions: list[
            BaseTransition] = transitions if transitions is not None else []
        self.version: str = version
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        str_version: str = f'-{self.version}' if self.version != 'v1' else ''
        script: str = f'\nstateDiagram{str_version}'
        for state in self.states:
            script += f'\n\t{state}'
        for transition in self.transitions:
            script += f'\n\t{transition}'

        self.script += script + '\n'
