import base64

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
        return self.response.text

    def _make_request_to_mermaid(self) -> None:
        self.response: Response = requests.get('https://mermaid.ink/svg/' +
                                               self._diagram)
