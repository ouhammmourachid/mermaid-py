"""Mindmap module.

This module provides the Mindmap class for creating and manipulating mindmap
diagrams.

Classes:
    Mindmap: Represents a mindmap diagram.
"""

from typing import Optional

from mermaid.configuration import Config
from mermaid.graph import Graph

from .level import Level, LevelShape


class Mindmap(Graph):
    """Mindmap class.

    This class represents a mindmap diagram.

    Args:
        title (str): The title of the mindmap.
        levels (Optional[list[Level]]): The levels of the mindmap. Defaults to None.
        shape (Optional[LevelShape]): The shape of the level. Defaults to None.
        config (Optional[Config]): The configuration for the mindmap. Defaults to None.
    """

    def __init__(
        self,
        title: str,
        levels: Optional[list[Level]] = None,
        shape: Optional[LevelShape] = None,
        config: Optional[Config] = None,
    ) -> None:
        """Initialize a new Mindmap.

        Args:
            title (str): The title of the mindmap.
            levels (Optional[list[Level]]): The levels of the mindmap. Defaults to None.
            shape (Optional[LevelShape]): The shape of the level. Defaults to None.
            config (Optional[Config]): The configuration for the mindmap. Defaults to None.
        """
        super().__init__(title, "", config)
        self.levels: list[Level] = levels if levels else []
        self.shape: LevelShape = shape if shape else LevelShape.DEFAULT
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = "\nmindmap"
        script += f"\n\t{self.shape.start}{self.title}{self.shape.end}"
        script += "\n"
        for level in self.levels:
            script += f"{level}"

        # script += '\n'
        self.script += script


__all__ = ["Mindmap", "Level", "LevelShape"]
