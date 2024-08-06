"""UserJourney module.

This module provides the UserJourney class for creating and manipulating user journeys.
It also provides the Section and Task classes for representing sections and tasks in a user journey.

Classes:
    UserJourney: Represents a user's journey through a website or application.
    Section: Represents a section in a user's journey.
    Task: Represents a task in a section of a user's journey.
"""

from typing import Optional, Union

from mermaid.configuration import Config
from mermaid.graph import Graph

from .actor import Actor
from .section import Section
from .task import Task


class UserJourney(Graph):
    """UserJourney class.

    This class represents a user's journey through a website or application.

    Attributes:
        title (str): The title of the user's journey.
        sections (list[Union[Section, Task]]): The sections in the user's journey.
        config (Config): The configuration for the user's journey.
    """

    def __init__(
        self,
        title: str,
        sections: list[Union[Section, Task]],
        config: Optional[Config] = None,
    ) -> None:
        """Initialize a new UserJourney.

        Args:
            title (str): The title of the user's journey.
            sections (list[Union[Section, Task]]): The sections in the user's journey.
            config (Optional[Config]): The configuration for the user's journey. Defaults to None.
        """
        super().__init__(title, "", config)
        self.title: str = title
        self.sections: list[Union[Section, Task]] = sections
        self._build_script()

    def _build_script(self) -> None:
        """Build the script for the user's journey."""
        super()._build_script()
        script: str = f"\njourney\n\ttitle {self.title}\n"
        for section in self.sections:
            script += f"{section}\n"
        self.script += script


__all__ = [
    "UserJourney",
    "Section",
    "Task",
    "Actor",
]
