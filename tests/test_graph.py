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
        self.graph_test: Graph = Graph("test-graph", script)
        return super().setUp()

    def test_save_graph_without_path(self) -> None:
        self.graph_test.save()
        self.assertTrue(Path.exists(Path("./test-graph.mmd")))

    def test_save_graph_with_path(self) -> None:
        self.graph_test.save(Path("./test-graph-file.mmd"))
        self.assertTrue(Path.exists(Path("./test-graph-file.mmd")))

    def test_save_graph_with_path_str(self) -> None:
        self.graph_test.save("./test-graph-str-path.mmd")
        self.assertTrue(Path.exists(Path("./test-graph-str-path.mmd")))

    def test_save_graph_name_contain_space(self) -> None:
        self.graph_test.title = "test graph file"
        self.graph_test.save(Path("./test graph file.mmd"))
        self.assertTrue(Path.exists(Path("./test graph file.mmd")))

    def test_save_should_raise_valueerror(self):
        self.graph_test.title = "file-name"
        with self.assertRaises(ValueError):
            self.graph_test.save(Path("./file-name.txt"))

    def tearDown(self) -> None:
        if os.path.exists("./test-graph.mmd"):
            os.remove("./test-graph.mmd")
        if os.path.exists("./test-graph-file.mmd"):
            os.remove("./test-graph-file.mmd")
        if os.path.exists("./test graph file.mmd"):
            os.remove("./test graph file.mmd")
        if os.path.exists("./test-graph-str-path.mmd"):
            os.remove("./test-graph-str-path.mmd")
        return super().tearDown()
