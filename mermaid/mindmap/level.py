"""Module for the Level class

This module contains the Level class which represents a level in a mindmap.

Example:
    >>> # Create a level with the name 'Level 1' and a circle shape
    >>> Level('Level 1', LevelShape.CIRCLE)])
    >>> # Create a level with the name 'Level 1' and a circle shape with an icon
    >>> Level('Level 1', LevelShape.CIRCLE, Icon('fa', 'fa-book'))
"""

from enum import Enum
from typing import Optional

from mermaid import text_to_snake_case
from mermaid.icon import Icon


class LevelShape(Enum):
    """Enum for the shape of a level

    Args:
        start (str): The start of the shape
        end (str): The end of the shape
    """

    SQUARE = ("[", "]")
    ROUNDED_SQUARE = ("(", ")")
    CIRCLE = ("((", "))")
    BANG = ("))", "((")
    CLOUD = (")", "(")
    HEXAGON = ("{{", "}}")
    DEFAULT = ("", "")

    def __init__(self, start: str, end: str) -> None:
        """Constructor for the LevelShape class

        Args:
            start (str): the start of the shape.
            end (str): the end of the shape.
        """
        self.end: str = end
        self.start: str = start


class Level:
    """Class for a level in a mindmap"""

    def __init__(
        self,
        name: str,
        children: Optional[list["Level"]] = None,
        shape: Optional[LevelShape] = None,
        icon: Optional[Icon] = None,
    ) -> None:
        """Constructor for the Level class

        Args:
            name (str): The name of the level
            children (Optional[list[Level]], optional): The children of the level. Defaults to None.
            shape (Optional[LevelShape], optional): The shape of the level. Defaults to None.
            icon (Optional[Icon], optional): The icon of the level. Defaults to None.

        example:
        >>> # Create a level with the name 'Level 1' and a circle shape
        >>> Level('Level 1', LevelShape.CIRCLE)])
        >>> # Create a level with the name 'Level 1' and a circle shape with an icon
        >>> Level('Level 1', LevelShape.CIRCLE, Icon('fa', 'fa-book'))

        """
        self.id_: str = text_to_snake_case(name)
        self.name: str = name
        self.children: list["Level"] = children if children else []
        self.shape: LevelShape = shape if shape else LevelShape.DEFAULT
        self.icon: Optional[Icon] = icon

    def add_child(self, child: "Level") -> None:
        """Add a child to the level

        Args:
            child (Level): The child to add
        """
        self.children.append(child)

    def __str__(self) -> str:
        """String representation of the level

        Returns:
            str: The string representation of the level
        """
        return self.list_str_to_str(self.list_str())

    def list_str(self) -> list:
        """List representation of the level

        Returns:
            list: The list representation of the level
        """
        string: str = f"{self.shape.start}{self.name}{self.shape.end}"
        if not len(self.children):
            if self.icon:
                return [string, f"::icon({self.icon.type_} {self.icon.name})"]
            return [string]

        list_str: list = []
        for child in self.children:
            list_str += child.list_str()
        return [string, list_str]

    def list_str_to_str(self, list_str: list, depth: int = 2) -> str:
        """Convert a list representation of a level to a string

        Args:
            list_str (list): The list representation of the level
            depth (int, optional): The depth of the level. Defaults to 2.

        Returns:
            str: [description]
        """
        result: str = ""
        for item in list_str:
            if isinstance(item, list):
                result += self.list_str_to_str(item, depth + 1)
            else:
                result += "\t" * depth + item + "\n"
        return result
