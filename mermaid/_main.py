import base64
from pathlib import Path
from typing import Union

import requests
from requests import Response

from .graph import Graph


class Mermaid:
    """
    This class represents a Mermaid diagram.

    Attributes:
        _diagram (str): The base64 encoded string of the Mermaid diagram script.
        svg_response (Response): The response from the GET request to the Mermaid SVG API.
        img_response (Response): The response from the GET request to the Mermaid IMG API.
    """
    def __init__(self, graph: Graph):
        """
        The constructor for the Mermaid class.

        Parameters:
            graph (Graph): The Graph object containing the Mermaid diagram script.
        """
        self._diagram = self._process_diagram(graph.script)
        self._make_request_to_mermaid()

    @staticmethod
    def _process_diagram(diagram: str) -> str:
        """
        Process the Mermaid diagram script into a base64 encoded string.

        Parameters:
            diagram (str): The Mermaid diagram script.

        Returns:
            str: The base64 encoded string of the Mermaid diagram script.
        """
        graphbytes = diagram.encode('utf8')
        base64_bytes = base64.b64encode(graphbytes)
        diagram = base64_bytes.decode('ascii')
        return diagram

    def _repr_html_(self) -> str:
        """
        Return the text of the SVG response.

        Returns:
            str: The text of the SVG response.
        """
        return self.svg_response.text

    def _make_request_to_mermaid(self) -> None:
        """
        Make GET requests to the Mermaid SVG and IMG APIs using
        the base64 encoded string of the Mermaid diagram script.
        """
        self.svg_response: Response = requests.get('https://mermaid.ink/svg/' +
                                                   self._diagram)
        self.img_response: Response = requests.get('https://mermaid.ink/img/' +
                                                   self._diagram)

    def to_svg(self, path: Union[str, Path]) -> None:
        """
        Write the SVG response text to a file.

        Parameters:
            path (Union[str, Path]): The path of the file to write to.
        """
        with open(path, 'w', encoding='utf-8') as file:
            file.write(self.svg_response.text)

    def to_png(self, path: Union[str, Path]) -> None:
        """
        Write the IMG response content to a file.

        Parameters:
            path (Union[str, Path]): The path of the file to write to.
        """
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
