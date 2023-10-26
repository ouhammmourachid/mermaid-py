import unittest

from mermaid import Mermaid
from mermaid.graph import Graph


class TestMermaid(unittest.TestCase):
    def setUp(self) -> None:
        script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        graph: Graph = Graph('simple-graph', script)
        self.mermaid_object = Mermaid(graph)

    def test_make_request_to_mermaid_api(self):
        self.assertTrue(self.mermaid_object.response.status_code == 200)
