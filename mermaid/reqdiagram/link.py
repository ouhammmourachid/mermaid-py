from typing import Union

from .element import Element
from .requirement import Requirement


class Link:
    """Link class.

    This class represents a link between elements or requirements in a requirement diagram.

    Attributes:
        source (Union[Element, Requirement]): The source of the link.
        destination (Union[Element, Requirement]): The destination of the link.
        type_ (str): The type of the link.
    """

    def __init__(
        self,
        source: Union[Element, Requirement],
        destination: Union[Element, Requirement],
        type_: str,
    ) -> None:
        """Initialize a new Link.

        Args:
            source (Union[Element, Requirement]): The source of the link.
            destination (Union[Element, Requirement]): The destination of the link.
            type_ (str): The type of the link.
        """
        self.source: Union[Element, Requirement] = source
        self.destination: Union[Element, Requirement] = destination
        self.type_: str = type_

    def __str__(self) -> str:
        """Return a string representation of the link.

        Returns:
            str: A string representation of the link.
        """
        return f"{self.source.name} - {self.type_} -> {self.destination.name}"
