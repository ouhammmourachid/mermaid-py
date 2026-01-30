import unittest

from mermaid import Mermaid
from mermaid.graph import Graph


class TestMermaidWithMalayalam(unittest.TestCase):
    def setUp(self) -> None:
        self.script: str = """
graph TD
    A["കേരളം"] --> B["ഇന്ത്യയുടെ സംസ്ഥാനം"]
    A --> C["തെക്കുപടിഞ്ഞാറേ അറ്റത്തുള്ള സംസ്ഥാനം"]
"""
        self.name: str = "malayalam-graph"
        self.graph: Graph = Graph(self.name, self.script)
        self.mermaid_object = Mermaid(self.graph)

    def test_make_request_to_mermaid_api_for_svg(self):
        self.assertTrue(self.mermaid_object.svg_response.status_code == 200)

    def test_make_request_to_mermaid_api_for_png(self):
        self.assertTrue(self.mermaid_object.img_response.status_code == 200)
