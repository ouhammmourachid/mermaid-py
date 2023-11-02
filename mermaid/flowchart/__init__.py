from mermaid.graph import Graph

from .link import Link
from .node import Node


class FlowChart(Graph):
    def __init__(self,
                 title: str,
                 nodes: list[Node] = None,
                 links: list[Link] = None,
                 orientation: str = 'TB') -> None:
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
