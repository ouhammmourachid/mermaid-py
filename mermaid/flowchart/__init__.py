"""FlowChart module.

This module provides the FlowChart class for creating and manipulating flowcharts.
It also provides utility classes for representing nodes and links in a flowchart.

Classes:
    FlowChart: Represents a flowchart.
    Node: Represents a node in a flowchart.
    Link: Represents a link between nodes in a flowchart.
"""
from typing import Optional

from mermaid.graph import Graph

from .link import Link, LinkHead, LinkShape
from .node import Node


class FlowChart(Graph):
    """FlowChart class.

    This class represents a flowchart.

    Attributes:
        orientation (str): The orientation of the flowchart.
        nodes (list[Node]): The nodes in the flowchart.
        links (list[Link]): The links between nodes in the flowchart.
    """
    def __init__(self,
                 title: str,
                 nodes: Optional[list[Node]] = None,
                 links: Optional[list[Link]] = None,
                 orientation: str = 'TB') -> None:
        """Initialize a new FlowChart.

        Args:
            title (str): The title of the flowchart.
            nodes (Optional[list[Node]]): The nodes in the flowchart.
            links (Optional[list[Link]]): The links between nodes in the flowchart.
            orientation (str): The orientation of the flowchart.
        """
        super().__init__(title, '')
        self.orientation: str = orientation
        self.nodes: list[Node] = nodes if nodes is not None else []
        self.links: list[Link] = links if links is not None else []
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = f'\nflowchart {self.orientation}'
        for node in self.nodes:
            script += f'\n\t{node}'
        for link in self.links:
            script += f'\n\t{link}'
        self.script += script + '\n'
