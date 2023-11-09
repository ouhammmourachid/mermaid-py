from mermaid.graph import Graph

from .element import *
from .link import *
from .requirement import *


class RequirementDiagram(Graph):
    def __init__(self, title: str, elements: list[Element],
                 requirements: list[Requirement], links: list[Link]) -> None:
        super().__init__(title, '')
        self.elements: list[Element] = elements if elements is not None else []
        self.requirements: list[
            Requirement] = requirements if requirements is not None else []
        self.links: list[Link] = links if links is not None else []
        self._build_script()

    def _build_script(self) -> None:
        super()._build_script()
        script: str = '\nrequirementDiagram\n'
        for element in self.elements:
            script += str(element) + '\n'
        for requirement in self.requirements:
            script += str(requirement) + '\n'

        for link in self.links:
            script += f'{link}\n'
        self.script += script
