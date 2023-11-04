from mermaid.graph import Graph

from .entity import Entity
from .link import Link


class ERDiagram(Graph):
    def __init__(self,
                 title: str,
                 entities: list[Entity] = None,
                 links: list[Link] = None) -> None:
        super().__init__(title, '')
        self.entities: list[Entity] = entities if entities is not None else []
        self.links: list[Link] = links if links is not None else []
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = '\nerDiagram'
        for entity in self.entities:
            script += f'\n\t{entity}'
        for link in self.links:
            script += f'\n\t{link}'
        self.script += script + '\n'
