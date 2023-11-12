from typing import Union

from mermaid.graph import Graph

from .actor import Actor
from .section import Section
from .task import Task


class UserJourney(Graph):
    def __init__(self, title: str, sections: list[Union[Section,
                                                        Task]]) -> None:
        super().__init__(title, '')
        self.title: str = title
        self.sections: list[Union[Section, Task]] = sections
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = f'\njourney\n\ttitle {self.title}\n'
        for section in self.sections:
            script += f'{section}\n'
        self.script += script
