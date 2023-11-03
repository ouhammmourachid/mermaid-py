from mermaid.graph import Graph

from .entity import Entity
from .link import Link


class ERDiagram(Graph):
    def __init__(self, title: str, entities: list[Entity] = None) -> None:
        super().__init__(title, '')
        self.entities: list[Entity] = entities if entities is not None else []
        self._build_script()
