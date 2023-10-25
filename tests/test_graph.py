import os
import unittest
from pathlib import Path

from mermaid.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        self.graph_test: Graph = Graph('test-graph', script)
        return super().setUp()

    def test_save_graph_without_path(self) -> None:
        self.graph_test.save()
        self.assertTrue(Path.exists(Path('./test-graph.txt')))

    def test_save_graph_with_path(self) -> None:
        self.graph_test.save(Path('./test-graph-file.txt'))
        self.assertTrue(Path.exists(Path('./test-graph-file.txt')))

    def tearDown(self) -> None:
        if os.path.exists('./test-graph.txt'):
            os.remove('./test-graph.txt')
        if os.path.exists('./test-graph-file.txt'):
            os.remove('./test-graph-file.txt')
        return super().tearDown()
