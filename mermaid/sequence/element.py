"""Sequence diagram elements."""
from enum import Enum
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


class NotePosition(Enum):
    """Note position enum for mermaid sequence diagram.

    Args:
        Enum (str): Note position.
    """
    LEFT_OF = 'left of'
    RIGHT_OF = 'right of'
    OVER = 'over'


class Note:
    """Note class for mermaid sequence diagram.

    Args:
        note (str): Note to be displayed.
        actor (Union[Actor, Participant], optional): Actor or Participant to attach the note to. Defaults to None.
    """
    def __init__(
            self,
            note: str,
            element: Union[list[Union[Actor, Participant]],
                           Union[Actor, Participant]],
            position: Union[NotePosition, str] = NotePosition.OVER) -> None:
        self.note = note
        self.element = element[0] if isinstance(
            element, list) and len(element) == 1 else element
        self.position = position if isinstance(position,
                                               str) else position.value
        if self.position in [
                NotePosition.RIGHT_OF.value, NotePosition.LEFT_OF.value
        ] and isinstance(self.element, list):
            raise ValueError(
                f'Note position {self.position} cannot be used with multiple elements'
            )

    def __str__(self):
        """Return note string.

        Returns:
            str: Note string.
        """
        if isinstance(self.element, list):
            note_str = f'\tNote {self.position} '
            for element in self.element:
                note_str += f'{element.id_},'
            note_str = note_str[:-1]
            note_str += f': {self.note}\n'
            return note_str
        else:
            return f'\tNote {self.position} {self.element.id_}: {self.note}\n'
