from collections.abc import Iterable
from typing import List

from mermaid.graph import Graph
from mermaid.graph.flowchart.link import Link
from mermaid.graph.flowchart.node import Node


class FlowChart(Graph):
    def __init__(self,
                 title: str,
                 nodes: List[Node] = None,
                 links: List[Link] = None) -> None:
        super().__init__(title, '')
        self.nodes: List[Node] = nodes if nodes is not None else []
        self.links: List[Link] = links if links is not None else []
        self._build_script()

    def _build_script(self) -> None:
        script: str = f'---\ntitle: {self.title}\n---'
        script += '\nflowchart'
        for node in self.nodes:
            script += f'\n\t{node}'
        for link in self.links:
            script += f'\n\t{link}'
        self.script = script + '\n'
