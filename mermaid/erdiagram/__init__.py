"""ERDiagram module.

This module provides the ERDiagram class for creating and manipulating ER diagrams.
It also provides utility classes for representing entities and links in an ER diagram.

Classes:
    ERDiagram: Represents an ER diagram.
    Entity: Represents an entity in an ER diagram.
    Link: Represents a link between entities in an ER diagram.
"""

from typing import Optional

from mermaid.configuration import Config
from mermaid.erdiagram.entity import Entity
from mermaid.erdiagram.link import LIST_CARDINALITIES, Link
from mermaid.graph import Graph


class ERDiagram(Graph):
    """ERDiagram class.

    This class represents an ER diagram.

    Attributes:
        title (str): The title of the ER diagram.
        entities (list[Entity]): The entities of the ER diagram.
        links (list[Link]): The links of the ER diagram.
        config (Optional[Config]): The configuration for the ER diagram.
    """

    def __init__(
        self,
        title: str,
        entities: Optional[list[Entity]] = None,
        links: Optional[list[Link]] = None,
        config: Optional[Config] = None,
    ) -> None:
        """Initialize a new ERDiagram.

        Args:
            title (str): The title of the ER diagram.
            entities (Optional[list[Entity]]): The entities of the ER diagram.
            links (Optional[list[Link]]): The links of the ER diagram.
            config (Optional[Config]): The configuration for the ER diagram.
        """
        super().__init__(title, "", config)
        self.entities: list[Entity] = entities if entities is not None else []
        self.links: list[Link] = links if links is not None else []
        self._build_script()

    def _build_script(self) -> None:
        """Build the script of the ER diagram."""
        super()._build_script()
        script: str = "\nerDiagram"
        for entity in self.entities:
            script += f"\n\t{entity}"
        for link in self.links:
            script += f"\n\t{link}"
        self.script += script + "\n"


__all__ = ["ERDiagram", "Entity", "Link", "LIST_CARDINALITIES"]
