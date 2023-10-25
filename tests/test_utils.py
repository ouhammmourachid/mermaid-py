import unittest

import mermaid as md
from mermaid.graph import Graph


class TestUtils(unittest.TestCase):
    def test_read_file_should_raise_error(self):
        with self.assertRaises(FileNotFoundError):
            md.read_file('./file.txt')

    def test_read_file(self):
        graph: Graph = md.read_file('./tests/test-graph.txt')
        expect_name: str = 'test-graph'
        expect_script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        self.assertEqual(graph.name, expect_name)
        self.assertEqual(graph.script, expect_script)
