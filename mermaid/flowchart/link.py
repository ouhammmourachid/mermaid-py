from enum import Enum
from typing import Union

from .node import Node

LINK_SHAPES: dict[str, str] = {
    "normal": "--",
    "dotted": "-.-",
    "thick": "==",
    "hidden": "~~~",
}

LINK_HEADS: dict[str, str] = {
    "none": "",
    "arrow": ">",
    "left-arrow": "<",
    "bullet": "o",
    "cross": "x",
}


class LinkShape(Enum):
    """LinkShape Enum.

    This enum represents the different shapes a link can have in a flowchart.
    """

    NORMAL = "normal"
    DOTTED = "dotted"
    THICK = "thick"
    HIDDEN = "hidden"


class LinkHead(Enum):
    """LinkHead Enum.

    This enum represents the different types of heads a link can have in a flowchart.
    """

    NONE = "none"
    ARROW = "arrow"
    LEFT_ARROW = "left-arrow"
    BULLET = "bullet"
    CROSS = "cross"


class Link:
    """Link class.

    This class represents a link between nodes in a flowchart.

    Attributes:
        origin (Node): The origin node of the link.
        end (Node): The end node of the link.
        shape (Union[str, LinkShape]): The shape of the link.
        head_left (Union[str, LinkHead]): The head of the link at the origin node.
        head_right (Union[str, LinkHead]): The head of the link at the end node.
        message (str): The message of the link.
    """

    def __init__(
        self,
        origin: Node,
        end: Node,
        shape: Union[str, LinkShape] = "normal",
        head_left: Union[str, LinkHead] = "none",
        head_right: Union[str, LinkHead] = "arrow",
        message: str = "",
    ) -> None:
        """Initialize a new Link.

        Args:
            origin (Node): The origin node of the link.
            end (Node): The end node of the link.
            shape (Union[str, LinkShape]): The shape of the link.
            head_left (Union[str, LinkHead]): The head of the link at the origin node.
            head_right (Union[str, LinkHead]): The head of the link at the end node.
            message (str): The message of the link.
        """
        self.origin: Node = origin
        self.end: Node = end
        self.head_left: str = LINK_HEADS[
            head_left if isinstance(head_left, str) else head_left.value
        ]
        self.head_right: str = LINK_HEADS[
            head_right if isinstance(head_right, str) else head_right.value
        ]
        self.shape: str = LINK_SHAPES[shape if isinstance(shape, str) else shape.value]
        self.message: str = f"|{message}|" if message else message

    def __str__(self) -> str:
        """Return a string representation of the link.

        If the link has a message, it includes the message in the string representation.
        Otherwise, it returns a string representation of a link without a message.

        Returns:
            str: A string representation of the link.
        """
        if self.message:
            element: list[str] = [
                self.origin.id_,
                " ",
                self.head_left,
                self.shape,
                self.head_right,
                self.message,
                " ",
                self.end.id_,
            ]
        else:
            element = [
                self.origin.id_,
                " ",
                self.head_left,
                self.shape,
                self.head_right,
                " ",
                self.end.id_,
            ]
        return "".join(element)
