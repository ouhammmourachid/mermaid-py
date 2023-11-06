import base64
from pathlib import Path
from typing import Union

import requests
from requests import Response

from .graph import Graph


class Mermaid:
    def __init__(self, graph: Graph):
        self._diagram = self._process_diagram(graph.script)
        self._make_request_to_mermaid()

    @staticmethod
    def _process_diagram(diagram: str) -> str:
        graphbytes = diagram.encode('utf8')
        base64_bytes = base64.b64encode(graphbytes)
        diagram = base64_bytes.decode('ascii')
        return diagram

    def _repr_html_(self) -> str:
        return self.svg_response.text

    def _make_request_to_mermaid(self) -> None:
        self.svg_response: Response = requests.get('https://mermaid.ink/svg/' +
                                                   self._diagram)
        self.img_response: Response = requests.get('https://mermaid.ink/img/' +
                                                   self._diagram)

    def to_svg(self, path: Union[str, Path]) -> None:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(self.svg_response.text)

    def to_png(self, path: Union[str, Path]) -> None:
        with open(path, 'wb') as file:
            file.write(self.img_response.content)


try:
    from IPython import get_ipython
    if get_ipython() is not None:
        from IPython.core.magic import register_cell_magic
        from IPython.display import Image, display

        @register_cell_magic
        def mermaidjs(line, cell):
            options = line.strip().split()
            script: str = cell.strip()
            graph: Graph = Graph('mermaid diagram', script)
            mermaid: Mermaid = Mermaid(graph)
            if '--img' in options:
                display(Image(mermaid.img_response.content))
            else:
                display(Mermaid(graph))

        get_ipython().register_magic_function(mermaidjs, magic_kind='cell')
except ImportError:
    # TODO: add a suitible handler for exception.
    print('Error acured while importing mermaidjs .')
