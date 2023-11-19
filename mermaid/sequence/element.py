"""Sequence diagram elements."""
from dataclasses import dataclass
from typing import Union

from mermaid._utils import text_to_snake_case


@dataclass
class Actor:
    """Actor class for mermaid sequence diagram.

    Args:
        name (str): Name of the actor.
    """
    name: str

    def __str__(self):
        """Return actor string.

        Returns:
            str: Actor string.
        """
        return f'\tActor {self.name}\n'


@dataclass
class Participant:
    """Participant class for mermaid sequence diagram.

    Args:
        name (str): Name of the participant.
    """
    name: str

    def __str__(self):
        """Return participant string.

        Returns:
            str: Participant string.
        """
        self.id = text_to_snake_case(self.name)
        return f'\tparticipant {self.id} as {self.name}\n'


class Box:
    """Box class for mermaid sequence diagram.

    Args:
        elements (List[Union[Actor, Participant]]): List of Actor or Participant objects.
        name (str): Name of the box.
    """
    def __init__(self, name: str, elements: list[Union[Actor, Participant]]):
        self.elements = elements
        self.name = name

    def __str__(self):
        """Return box string.

        Returns:
            str: Box string.
        """
        box_str = f'\tbox {self.name}\n'
        for element in self.elements:
            box_str += str(element)
        box_str += '\tend\n'
        return box_str
