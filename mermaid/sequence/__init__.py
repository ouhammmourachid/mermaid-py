from typing import Union

from mermaid.graph import Graph
from mermaid.sequence.element import Actor, Box, Note, NotePosition, Participant, Rect
from mermaid.sequence.link import ArrowTypes, Link
from mermaid.sequence.logic import Alt, Break, Critical, Loop, Optional, Parallel


class SequenceDiagram(Graph):
    def __init__(self,
                 title: str,
                 elements: list[Union[Actor, Participant, Box, Note, Link, Alt,
                                      Break, Critical, Loop, Optional,
                                      Parallel]],
                 auto_number: bool = False):
        super().__init__(title, '')
        self.elements = elements
        self.auto_number = auto_number
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = '\nsequenceDiagram\n'
        if self.auto_number:
            script += '\tautonumber\n'
        for element in self.elements:
            script += str(element)
        self.script += script
