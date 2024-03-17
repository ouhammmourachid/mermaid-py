from mermaid.graph import Graph

from .base import BaseTransition
from .state import Composite, Concurrent, End, Start, State
from .transition import Choice, Fork, Join, Transition


class StateDiagram(Graph):
    def __init__(self,
                 title: str,
                 states: list[State],
                 transitions: list[BaseTransition],
                 version: str = 'v2') -> None:
        super().__init__(title, '')
        self.states: list[State] = states
        self.transitions: list[BaseTransition] = transitions
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
