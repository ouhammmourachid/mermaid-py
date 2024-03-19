"""Mindmap module.

This module provides the Mindmap class for creating and manipulating mindmap
diagrams.

Classes:
    Mindmap: Represents a mindmap diagram.
"""
from typing import Optional

from mermaid.graph import Graph

from .level import Level, LevelShape


class Mindmap(Graph):
    """Mindmap class.

    This class represents a mindmap diagram.

    Args:
        title (str): The title of the mindmap.
        levels (Optional[list[Level]]): The levels of the mindmap. Defaults to None.
        shape (Optional[LevelShape]): The shape of the level. Defaults to None.
    """
    def __init__(self,
                 title: str,
                 levels: Optional[list[Level]] = None,
                 shape: Optional[LevelShape] = None) -> None:
        super().__init__(title, '')
        self.levels: list[Level] = levels if levels else []
        self.shape: LevelShape = shape if shape else LevelShape.DEFAULT
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = '\nmindmap'
        script += f'\n\troot{self.shape.start}{self.title}{self.shape.end}'
        script += '\n'
        for level in self.levels:
            script += f'{self.parse_list_str(level.list_str())}\n'

        self.script += script + '\n'

    def parse_list_str(self, list_str: list, depth: int = 2) -> str:
        result: str = ''
        for item in list_str:
            if isinstance(item, list):
                result += self.parse_list_str(item, depth + 1)
            else:
                result += '\t' * depth + item + '\n'
        return result
