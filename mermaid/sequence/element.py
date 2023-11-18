"""Sequence diagram elements."""
from dataclasses import dataclass

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
