from typing import Optional


class Element:
    """UserJourney module.

    This module provides the UserJourney class for creating and manipulating user journeys.
    It also provides the Section and Task classes for representing sections and tasks in a user journey.

    Classes:
        UserJourney: Represents a user's journey through a website or application.
        Section: Represents a section in a user's journey.
        Task: Represents a task in a section of a user's journey.
    """

    def __init__(self, name: str, type_: str, docRef: Optional[str] = None) -> None:
        """Initialize a new Element.

        Args:
            name (str): The name of the element.
            type_ (str): The type of the element.
            docRef (Optional[str]): The documentation reference for the element.
        """
        self.name: str = name
        self.type_: str = type_
        self.docRef: Optional[str] = docRef

    def __str__(self) -> str:
        """Return a string representation of the element.

        Returns:
            str: A string representation of the element.
        """
        string: str = f"element {self.name} {{\n"
        string += f'\ttype: "{self.type_}"\n'
        string += f"\tdocRef: {self.docRef}\n" if self.docRef else ""
        string += "}\n"
        return string
