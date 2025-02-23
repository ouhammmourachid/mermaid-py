"""Mermaid module.

This module provides the Mermaid class for creating and manipulating Mermaid diagrams.
It also provides utility functions for loading data and converting text to snake case.

Classes:
    Mermaid: Represents a Mermaid diagram.

Functions:
    load(file_path): Load data from a file.
    text_to_snake_case(text): Convert a string of text to snake case.
"""

from enum import Enum

from .__main__ import Mermaid, Position
from .configuration import Config
from .graph import Graph
from .icon import Icon
from .style import Style
from .utils import load, text_to_snake_case

__version__: str = "0.7.1"


class Direction(Enum):
    """Enum for representing the direction of a Mermaid diagram."""

    LEFT_TO_RIGHT = "LR"
    RIGHT_TO_LEFT = "RL"
    TOP_TO_BOTTOM = "TB"
    BOTTOM_TO_TOP = "BT"


__all__ = [
    "Mermaid",
    "load",
    "Direction",
    "Graph",
    "Style",
    "Config",
    "Icon",
    "Position",
    "text_to_snake_case",
]
