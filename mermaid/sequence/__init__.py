from typing import Optional as Option
from typing import Union

from mermaid.configuration import Config
from mermaid.graph import Graph
from mermaid.sequence.element import Actor, Box, Note, NotePosition, Participant, Rect
from mermaid.sequence.link import ArrowTypes, Link
from mermaid.sequence.logic import Alt, Break, Critical, Loop, Optional, Parallel


class SequenceDiagram(Graph):
    """SequenceDiagram class.

    This class represents a sequence diagram.

    Attributes:
        elements (list[Union[Actor, Participant, Box, Note, Link, Alt, Break, Critical, Loop, Optional, Parallel]]):
            The elements in the sequence diagram.
        auto_number (bool): Whether to automatically number the elements in the diagram.
        config (Config): The configuration for the sequence diagram.
    """

    def __init__(
        self,
        title: str,
        elements: list[
            Union[
                Actor,
                Participant,
                Box,
                Note,
                Link,
                Alt,
                Break,
                Critical,
                Loop,
                Optional,
                Parallel,
            ]
        ],
        auto_number: bool = False,
        config: Option[Config] = None,
    ) -> None:
        """Initialize a new SequenceDiagram.

        Args:
            title (str): The title of the sequence diagram.
            elements (list[Union[Actor, Participant, Box, Note, Link, Alt,
                                  Break, Critical, Loop, Optional, Parallel]]):
                The elements in the sequence diagram.
            auto_number (bool): Whether to automatically number the elements in the diagram. Defaults to False.
            config (Optional[Config]): The configuration for the sequence diagram. Defaults to None.
        """
        super().__init__(title, "", config)
        self.elements = elements
        self.auto_number = auto_number
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = "\nsequenceDiagram\n"
        if self.auto_number:
            script += "\tautonumber\n"
        for element in self.elements:
            script += str(element)
        self.script += script


__all__ = [
    "SequenceDiagram",
    "Actor",
    "Participant",
    "Box",
    "Note",
    "NotePosition",
    "Rect",
    "Link",
    "ArrowTypes",
    "Alt",
    "Break",
    "Critical",
    "Loop",
    "Optional",
    "Parallel",
]
