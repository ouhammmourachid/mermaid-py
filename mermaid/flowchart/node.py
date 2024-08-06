from dataclasses import dataclass
from typing import Optional, Union

from mermaid import Direction, text_to_snake_case
from mermaid.style import Style


@dataclass
class NodeShape:
    """NodeShape class.

    This class represents the shape of a node in a flowchart.

    Attributes:
        start (str): The start character of the node shape.
        end (str): The end character of the node shape.
    """

    start: str
    end: str


NODE_SHAPES: dict[str, NodeShape] = {
    "normal": NodeShape("[", "]"),
    "round-edge": NodeShape("(", ")"),
    "stadium-shape": NodeShape("([", "])"),
    "subroutine-shape": NodeShape("[[", "]]"),
    "cylindrical": NodeShape("[(", ")]"),
    "circle": NodeShape("((", "))"),
    "label-shape": NodeShape(">", "]"),
    "rhombus": NodeShape("{", "}"),
    "hexagon": NodeShape("{{", "}}"),
    "parallelogram": NodeShape("[/", "/]"),
    "parallelogram-alt": NodeShape("[\\", "\\]"),
    "trapezoid": NodeShape("[/", "\\]"),
    "trapezoid-alt": NodeShape("[\\", "/]"),
    "double-circle": NodeShape("(((", ")))"),
}

HREF_TYPES: dict[str, str] = {
    "blank": "_blank",
    "self": "_self",
    "parent": "_parent",
    "top": "_top",
}


class Node:
    """Node class.

    This class represents a node in a flowchart.

    Attributes:
        id_ (str): The ID of the node.
        content (str): The content of the node.
        shape (str): The shape of the node.
        sub_nodes (list[Node]): The sub-nodes of the node.
        href (str): The hyperlink reference of the node.
        href_type (str): The type of the hyperlink reference of the node.
        styles (list[Style]): The styles of the node.
    """

    def __init__(
        self,
        id_: str,
        content: str = "",
        shape: str = "normal",
        sub_nodes: Optional[list["Node"]] = None,
        href: Optional[str] = None,
        href_type: str = "blank",
        styles: Optional[list[Style]] = None,
        direction: Union[str, Direction] = "LR",
    ) -> None:
        """Initialize a new Node.

        Args:
            id_ (str): The ID of the node.
            content (str): The content of the node.
            shape (str): The shape of the node.
            sub_nodes (Optional[list[Node]]): The sub-nodes of the node.
            href (Optional[str]): The hyperlink reference of the node.
            href_type (str): The type of the hyperlink reference of the node.
            styles (Optional[list[Style]]): The styles of the node.
            direction (Optional[Union[str,Direction]]): The direction of the node in case of a subgraph.
        """
        self.id_: str = text_to_snake_case(id_)
        self.content: str = content if content else id_
        self.shape: NodeShape = NODE_SHAPES[shape]
        self.href: str = href if href is not None else "#"
        self.href_type: str = HREF_TYPES[href_type]
        self.sub_nodes: list["Node"] = sub_nodes if sub_nodes is not None else []
        self.styles: list[Style] = styles if styles is not None else []
        self.direction: str = (
            direction if isinstance(direction, str) else direction.value
        )

    def __str__(self) -> str:
        """Return a string representation of the node.

        If the node has sub-nodes, it returns a string representation of a subgraph.
        Otherwise, it returns a string representation of a single node.

        Returns:
            str: A string representation of the node.
        """
        string: str = ""
        if len(self.sub_nodes):
            string = "\n".join(
                [
                    f'subgraph {self.id_} ["{self.content}"]',
                    f"\tdirection {self.direction}",
                    "\n".join([str(f"\t{node}") for node in self.sub_nodes]),
                    "end",
                ]
            )
        else:
            string = "".join(
                [self.id_, self.shape.start, f'"{self.content}"', self.shape.end]
            )
            if self.href != "#":
                string = "".join(
                    [string, "\n", f'click {self.id_} "{self.href}" {self.href_type}']
                )

        for style in self.styles:
            string += f"\n{self.id_}:::{style.name}"
        return string
