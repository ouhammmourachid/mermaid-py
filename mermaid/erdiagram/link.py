from .entity import Entity

LIST_CARDINALITIES: dict[str, list[str]] = {
    "zero-or-one": ["|o", "o|"],
    "exactly-one": ["||", "||"],
    "zero-or-more": ["}o", "o{"],
    "one-or-more": ["}|", "|{"],
}


class Link:
    """Link class.

    This class represents a link between entities in an ER diagram.

    Attributes:
        origin (Entity): The origin entity of the link.
        end (Entity): The end entity of the link.
        label (str): The label of the link.
        left_symbol (str): The symbol at the left end of the link.
        right_symbol (str): The symbol at the right end of the link.
        dotted (bool): Whether the link is dotted or not.
    """

    def __init__(
        self,
        origin: Entity,
        end: Entity,
        origin_cardinality: str,
        end_cardinality: str,
        label: str = "",
        dotted: bool = False,
    ) -> None:
        """Initialize a new Link.

        Args:
            origin (Entity): The origin entity of the link.
            end (Entity): The end entity of the link.
            label (str): The label of the link.
            origin_cardinality (str): The cardinality of the origin entity.
            end_cardinality (str): The cardinality of the end entity.
            dotted (bool): Whether the link is dotted or not.
        """
        self.origin: Entity = origin
        self.end: Entity = end
        self.label: str = label
        self.left_symbol: str = LIST_CARDINALITIES[origin_cardinality][0]
        self.right_symbol: str = LIST_CARDINALITIES[end_cardinality][1]
        self.dotted: bool = dotted

    def __str__(self) -> str:
        """Return a string representation of the link.

        The string representation includes the names of the origin and end entities,
        the symbols at both ends of the link, and the label of the link.

        Returns:
            str: A string representation of the link.
        """
        shape: str = ".." if self.dotted else "--"
        return f'{self.origin.name}{self.left_symbol}{shape}{self.right_symbol}{self.end.name} : "{self.label}"'
