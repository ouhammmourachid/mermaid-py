"""ReqDiagram module.

This module provides the ReqDiagram class for creating and manipulating requirement diagrams.
It also provides utility classes for representing elements, links, and requirements in a requirement diagram.

Classes:
    ReqDiagram: Represents a requirement diagram.
    Element: Represents an element in a requirement diagram.
    Link: Represents a link between elements or requirements in a requirement diagram.
    Requirement: Represents a requirement in a requirement diagram.
"""

from typing import Optional

from mermaid.configuration import Config
from mermaid.graph import Graph

from .element import Element
from .link import Link
from .requirement import Requirement, Risk, Type, VerifyMethod


class RequirementDiagram(Graph):
    """RequirementDiagram class.

    This class represents a requirement diagram, which is a type of graph.
    It contains elements, requirements, and links between them.

    Attributes:
        elements (list[Element]): The elements in the diagram.
        requirements (list[Requirement]): The requirements in the diagram.
        links (list[Link]): The links between elements and requirements in the diagram.
        config (Config): The configuration for the requirement diagram.
    """

    def __init__(
        self,
        title: str,
        elements: list[Element],
        requirements: list[Requirement],
        links: list[Link],
        config: Optional[Config] = None,
    ) -> None:
        """Initialize a new RequirementDiagram.

        Args:
            title (str): The title of the diagram.
            elements (list[Element]): The elements in the diagram.
            requirements (list[Requirement]): The requirements in the diagram.
            links (list[Link]): The links between elements and requirements in the diagram.
            config (Optional[Config]): The configuration for the diagram. Defaults to None.
        """
        super().__init__(title, "", config)
        self.elements: list[Element] = elements if elements is not None else []
        self.requirements: list[Requirement] = (
            requirements if requirements is not None else []
        )
        self.links: list[Link] = links if links is not None else []
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = "\nrequirementDiagram\n"
        for element in self.elements:
            script += str(element) + "\n"
        for requirement in self.requirements:
            script += str(requirement) + "\n"

        for link in self.links:
            script += f"{link}\n"
        self.script += script


__all__ = [
    "RequirementDiagram",
    "Element",
    "Link",
    "Requirement",
    "Risk",
    "VerifyMethod",
    "Type",
]
