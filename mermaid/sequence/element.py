"""Sequence diagram elements."""
from typing import Union

from mermaid._utils import text_to_snake_case


class Actor:
    """Actor class for mermaid sequence diagram.

    Args:
        name (str): Name of the actor.
    """
    def __init__(self, name: str):
        """Initialize actor.

        Args:
            name (str): Name of the actor.
        """
        self.name: str = name
        self.id_: str = text_to_snake_case(self.name)

    def __str__(self):
        """Return actor string.

        Returns:
            str: Actor string.
        """
        return f'\tActor {self.name}\n'


class Participant:
    """Participant class for mermaid sequence diagram.

    Args:
        name (str): Name of the participant.
    """
    def __init__(self, name: str):
        """Initialize participant.

        Args:
            name (str): Name of the participant.
        """
        self.name: str = name
        self.id_: str = text_to_snake_case(self.name)

    def __str__(self):
        """Return participant string.

        Returns:
            str: Participant string.
        """
        return f'\tparticipant {self.id_} as {self.name}\n'


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
